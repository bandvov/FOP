#!/usr/bin/env python3
"""
Virtual FOP Monte-Carlo Ensemble
--------------------------------
Supports CUDA acceleration via PyTorch when available.
Falls back to SciPy (CPU) otherwise.

Features included:
- Stochastic Poisson flares
- Protective Modifier module
- Gene-therapy delivery realism (efficiency, rise time, escape, residual activity)
- Homeostatic repair score
"""

import json
from pathlib import Path
import time

from save_results import save_results
from silencing_sweep import silencing_scenarios
from top8_scenarios import top8_scenarios
from combined_sweep import combined_sweep_scenarios
from baselines import baseline_scenarios
import numpy as np
from scipy.integrate import odeint
import warnings
warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# Device detection
# ------------------------------------------------------------
try:
    import torch
    TORCH_AVAILABLE = True
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"PyTorch {torch.__version__} | Device: {DEVICE}")
except ImportError:
    TORCH_AVAILABLE = False
    DEVICE = "cpu"
    print("PyTorch not found – using SciPy (CPU only)")


def save_checkpoint(results, processed, total, checkpoint_dir="checkpoints"):
    """Save current progress so the run can be resumed later."""
    Path(checkpoint_dir).mkdir(parents=True, exist_ok=True)

    checkpoint = {
        "processed": processed,
        "total": total,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "results": {}
    }

    for name, data in results.items():
        checkpoint["results"][name] = {
            "HO": [float(x) for x in data["HO"]],
            "repair": [float(x) for x in data["repair"]],
        }
        if "n_flares" in data:
            checkpoint["results"][name]["n_flares"] = [
                int(x) for x in data["n_flares"]]

    path = Path(checkpoint_dir) / "fop_checkpoint.json"
    with open(path, "w") as f:
        json.dump(checkpoint, f)

    print(f"  → Checkpoint saved ({processed}/{total} realizations)")


def load_checkpoint(checkpoint_dir="checkpoints"):
    """Load previous progress if a checkpoint exists."""
    path = Path(checkpoint_dir) / "fop_checkpoint.json"
    if not path.exists():
        return None, 0

    with open(path, "r") as f:
        checkpoint = json.load(f)

    results = {}
    for name, data in checkpoint["results"].items():
        results[name] = {
            "HO": data["HO"],
            "repair": data["repair"],
        }
        if "n_flares" in data:
            results[name]["n_flares"] = data["n_flares"]

    processed = checkpoint["processed"]
    print(f"Resuming from checkpoint: {processed} realizations already done.")
    return results, processed

# ============================================================
# 1. Stochastic flare generator
# ============================================================


def generate_poisson_flares(T, rate_per_unit=0.05, intensity=2.6, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    times = []
    t = 0.0
    while t < T:
        t += rng.exponential(1.0 / rate_per_unit)
        if t < T:
            times.append(t)
    return np.array(times, dtype=np.float32), intensity


# ============================================================
# 2. SciPy version of the model (CPU fallback)
# ============================================================
def fop_model_scipy(y, t, p, flare_times, flare_intensity):
    I_sys, I_loc, S, noncan, FAPa, H, repair, corrected = np.maximum(y, 0.0)
    corrected = np.clip(corrected, 0.0, 1.0)

    gt_eff = p.get("gt_efficiency", 0.0)
    gt_onset = p.get("gt_onset", 9999.0)
    gt_rise = p.get("gt_rise_time", 8.0)
    escape = p.get("gt_escape_rate", 0.0)
    residual = p.get("residual_activity", 0.05)

    if t >= gt_onset:
        d_corrected = (gt_eff - corrected) / gt_rise - escape * corrected
    else:
        d_corrected = 0.0

    effective_mut = p["mut"] * \
        (1.0 - corrected * (1.0 - residual)) * p.get("sil", 1.0)

    inh_k = p.get("inh_k", 1.0)
    inh_nc = p.get("inh_noncan", 1.0)

    prot_inflam = p.get("prot_inflam", 1.0)
    prot_phos = p.get("prot_phos", 1.0)
    prot_fap = p.get("prot_fap", 1.0)
    prot_noncan = p.get("prot_noncan", 1.0)
    prot_repair = p.get("prot_repair", 1.0)

    flare_force = 0.0
    for ft in flare_times:
        if abs(t - ft) < 1.0:
            flare_force += flare_intensity * np.exp(-((t - ft)**2) / 0.4)

    dI_sys = 0.08 * (0.35 + 0.4 * np.sin(t / 22.0)) - \
        0.28 * I_sys + flare_force
    dI_loc = 0.32 * I_sys - 0.42 * I_loc + 0.04 * S

    signal = effective_mut * (0.55 + 0.45 * I_loc * prot_inflam) * inh_k
    dS = 0.75 * signal - 0.55 * S * prot_phos
    d_noncan = 0.48 * signal * I_loc * inh_nc * prot_noncan - 0.42 * noncan

    total_osteo = S + 0.65 * noncan
    d_FAPa = 0.14 * I_loc * prot_fap * (1.8 - FAPa) - 0.11 * total_osteo * FAPa
    dH = 0.038 * total_osteo * FAPa * (1.0 + 0.18 * I_loc)

    inhibition_penalty = (
        (1.0 - inh_k) * 0.65 +
        (1.0 - inh_nc) * 0.45 +
        (1.0 - p.get("sil", 1.0)) * 0.30
    )
    d_repair = (
        0.55 * prot_repair * (1.0 - 0.55 * inhibition_penalty)
        - 0.14 * repair
        - 0.07 * total_osteo * repair
    )

    return [dI_sys, dI_loc, dS, d_noncan, d_FAPa, dH, d_repair, d_corrected]


# ============================================================
# 3. Batched PyTorch version (CUDA / CPU)
# ============================================================
def fop_rhs_torch(y, t, p, flare_times_list, flare_intensity):
    """
    y shape: (batch, 8)
    t is a Python float
    """
    I_sys = y[:, 0]
    I_loc = y[:, 1]
    S = y[:, 2]
    noncan = y[:, 3]
    FAPa = y[:, 4]
    H = y[:, 5]
    repair = y[:, 6]
    corrected = torch.clamp(y[:, 7], 0.0, 1.0)

    batch_size = y.shape[0]
    device = y.device

    # ----- Gene therapy -----
    gt_eff = p["gt_efficiency"]
    gt_onset = p["gt_onset"]
    gt_rise = p["gt_rise_time"]
    escape = p["gt_escape_rate"]
    residual = p["residual_activity"]

    # Fixed: t is a float, so use normal Python comparison
    if t >= gt_onset:
        d_corrected = (gt_eff - corrected) / gt_rise - escape * corrected
    else:
        d_corrected = torch.zeros(batch_size, device=device)

    effective_mut = p["mut"] * (1.0 - corrected * (1.0 - residual)) * p["sil"]

    # ----- Flare force -----
    flare_force = torch.zeros(batch_size, device=device)
    for b in range(batch_size):
        for ft in flare_times_list[b]:
            if abs(t - ft) < 1.0:
                flare_force[b] += flare_intensity * torch.exp(
                    torch.tensor(-((t - ft)**2) / 0.4, device=device)
                )

    # ----- Dynamics -----
    dI_sys = 0.08 * (0.35 + 0.4 * torch.sin(torch.tensor(t / 22.0, device=device))) \
        - 0.28 * I_sys + flare_force
    dI_loc = 0.32 * I_sys - 0.42 * I_loc + 0.04 * S

    signal = effective_mut * (0.55 + 0.45 * I_loc *
                              p["prot_inflam"]) * p["inh_k"]
    dS = 0.75 * signal - 0.55 * S * p["prot_phos"]
    d_noncan = 0.48 * signal * I_loc * \
        p["inh_noncan"] * p["prot_noncan"] - 0.42 * noncan

    total_osteo = S + 0.65 * noncan
    d_FAPa = 0.14 * I_loc * p["prot_fap"] * \
        (1.8 - FAPa) - 0.11 * total_osteo * FAPa
    dH = 0.038 * total_osteo * FAPa * (1.0 + 0.18 * I_loc)

    inhibition_penalty = (
        (1.0 - p["inh_k"]) * 0.65 +
        (1.0 - p["inh_noncan"]) * 0.45 +
        (1.0 - p["sil"]) * 0.30
    )
    d_repair = (
        0.55 * p["prot_repair"] * (1.0 - 0.55 * inhibition_penalty)
        - 0.14 * repair
        - 0.07 * total_osteo * repair
    )

    return torch.stack(
        [dI_sys, dI_loc, dS, d_noncan, d_FAPa, dH, d_repair, d_corrected],
        dim=1
    )


def rk4_step(y, t, dt, p, flare_times_list, flare_intensity):
    k1 = fop_rhs_torch(y, t,           p, flare_times_list, flare_intensity)
    k2 = fop_rhs_torch(y + 0.5*dt*k1, t + 0.5*dt, p,
                       flare_times_list, flare_intensity)
    k3 = fop_rhs_torch(y + 0.5*dt*k2, t + 0.5*dt, p,
                       flare_times_list, flare_intensity)
    k4 = fop_rhs_torch(y + dt*k3,     t + dt,     p,
                       flare_times_list, flare_intensity)
    return y + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


def integrate_batch_torch(y0_batch, t_eval, p, flare_times_list, flare_intensity, device):
    """
    Simple fixed-step RK4 for a batch of trajectories.
    y0_batch: (batch, 8)
    """
    dt = t_eval[1] - t_eval[0]
    y = y0_batch.clone()
    results = [y.clone()]

    for i in range(1, len(t_eval)):
        t = t_eval[i-1].item()
        y = rk4_step(y, t, dt, p, flare_times_list, flare_intensity)
        y = torch.clamp(y, min=0.0)          # keep non-negative
        results.append(y.clone())

    return torch.stack(results, dim=1)       # (batch, time, 8)


# ============================================================
# 4. Ensemble runner
# ============================================================
def run_ensemble(n_realizations=200, T_end=100.0, seed=42, use_cuda=True,
                 checkpoint_every=500, checkpoint_dir="checkpoints"):
    """
    Monte-Carlo ensemble with periodic checkpointing.

    checkpoint_every : save progress every N realizations
    """
    rng = np.random.default_rng(seed)
    t_eval = np.linspace(0, T_end, 300)

    y0 = np.array([0.35, 0.18, 0.08, 0.04, 0.45,
                  0.0, 0.55, 0.0], dtype=np.float32)

    # ----- Define your scenarios here -----
    scenarios = {
        **baseline_scenarios,
        **silencing_scenarios,
        **top8_scenarios,
        **combined_sweep_scenarios
    }

    # Try to resume from checkpoint
    results, already_done = load_checkpoint(checkpoint_dir)
    if results is None:
        results = {name: {"HO": [], "repair": []} for name in scenarios}
        already_done = 0

    remaining = n_realizations - already_done
    if remaining <= 0:
        print("All realizations already completed.")
        return results

    use_gpu = TORCH_AVAILABLE and use_cuda and torch.cuda.is_available()

    if use_gpu:
        print(f"Running on CUDA | remaining: {remaining} realizations")
        device = torch.device("cuda")
        t_torch = torch.tensor(t_eval, dtype=torch.float32, device=device)
        batch_size = 128          # adjust to your GPU memory

        processed = already_done
        while processed < n_realizations:
            current_batch = min(batch_size, n_realizations - processed)
            print(f"  Batch {processed}-{processed + current_batch}")

            flare_lists = []
            for _ in range(current_batch):
                ft, _ = generate_poisson_flares(T_end, rng=rng)
                flare_lists.append(ft)

            y0_batch = torch.tensor(y0, dtype=torch.float32, device=device).unsqueeze(
                0).repeat(current_batch, 1)

            for name, p in scenarios.items():
                p_torch = {k: float(v) for k, v in p.items()}
                traj = integrate_batch_torch(
                    y0_batch, t_torch, p_torch, flare_lists, 2.6, device)
                final = traj[:, -1, :]
                results[name]["HO"].extend(final[:, 5].cpu().numpy().tolist())
                results[name]["repair"].extend(
                    final[:, 6].cpu().numpy().tolist())

            processed += current_batch

            # ----- Checkpoint -----
            if processed % checkpoint_every < batch_size or processed >= n_realizations:
                save_checkpoint(results, processed,
                                n_realizations, checkpoint_dir)

    else:
        # CPU fallback with checkpointing
        print(f"Running on CPU | remaining: {remaining} realizations")
        for i in range(already_done, n_realizations):
            if (i + 1) % 50 == 0:
                print(f"  {i+1}/{n_realizations}")
            flare_times, flare_int = generate_poisson_flares(T_end, rng=rng)

            for name, p in scenarios.items():
                sol = odeint(fop_model_scipy, y0, t_eval,
                             args=(p, flare_times, flare_int),
                             atol=1e-5, rtol=1e-5)
                results[name]["HO"].append(sol[-1, 5])
                results[name]["repair"].append(np.mean(sol[:, 6]))

            if (i + 1) % checkpoint_every == 0 or (i + 1) == n_realizations:
                save_checkpoint(results, i + 1, n_realizations, checkpoint_dir)

    return results


# ============================================================
# 5. Main
# ============================================================
if __name__ == "__main__":
    results = run_ensemble(
        # save every 1000 realizations
        n_realizations=10000,
        T_end=100.0,
        seed=42,
        use_cuda=True,
        checkpoint_every=1000,
        checkpoint_dir="checkpoints"
    )

    print("\n" + "=" * 70)
    print(f"{'Scenario':<30} {'HO mean':>10} {'HO std':>8} {'Repair mean':>12}")
    print("-" * 70)
    for name, data in results.items():
        ho = np.array(data["HO"])
        rep = np.array(data["repair"])
        print(f"{name:<30} {ho.mean():10.3f} {ho.std():8.3f} {rep.mean():12.3f}")

    print("\nDone.")

    # Save everything
    json_path, summary_path, detail_dir = save_results(
        results, output_dir="results")

    print("\nDone. Results stored successfully.")
