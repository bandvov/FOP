# Virtual FOP – Computational Model of Fibrodysplasia Ossificans Progressiva

**A multi-compartment, stochastic systems-biology model for exploring disease mechanisms and therapeutic strategies in FOP.**

---

## Overview

This project implements a computational (“virtual”) model of **Fibrodysplasia Ossificans Progressiva (FOP)**, a rare genetic disorder caused by gain-of-function mutations in the *ACVR1/ALK2* gene. The model simulates:

- Systemic and local inflammation
- Canonical (Smad) and non-canonical (mTOR / YAP / PI3K / NF-κB) signaling
- Progenitor (FAP-like) activation and differentiation
- Cumulative heterotopic ossification (HO)
- Homeostatic repair capacity (normal bone / soft-tissue healing)

It supports **stochastic flare/trauma events** (Poisson process), **protective genetic modifiers**, and **realistic gene-therapy delivery** (partial transduction efficiency, rise time, escape/dilution, residual activity).

The model is designed for rapid *in silico* experimentation of therapeutic strategies before wet-lab or clinical testing.

---

## Key Features

| Feature | Description |
|---------|-------------|
| **Multi-compartment dynamics** | Systemic inflammation → local tissue → signaling → progenitors → HO |
| **Stochastic flares** | Acute trauma events generated as a Poisson process (unpredictable real-world injury) |
| **Protective Modifier module** | Simulates natural genetic buffering (mild phenotypes) |
| **Gene-therapy realism** | Incomplete efficiency, delayed onset, slow escape, residual mutant activity |
| **Homeostatic repair score** | Explicit penalty for strategies that destroy normal healing |
| **CUDA acceleration** | Automatic GPU support via PyTorch when available; falls back to SciPy/CPU |
| **Monte-Carlo ensembles** | Hundreds/thousands of independent realizations for robust statistics |

---

## Model Structure

### State Variables (8-dimensional)

| Index | Name | Meaning |
|-------|------|---------|
| 0 | `I_sys` | Systemic inflammation |
| 1 | `I_loc` | Local tissue inflammation |
| 2 | `S` | Canonical Smad1/5/8 signaling |
| 3 | `noncan` | Aggregated non-canonical signaling |
| 4 | `FAPa` | Activated progenitors |
| 5 | `H` | Cumulative heterotopic ossification volume |
| 6 | `repair` | Homeostatic repair / normal healing capacity |
| 7 | `corrected` | Fraction of progenitors successfully gene-edited |

### Core Parameters

**Disease & Intervention**
- `mut` – gain-of-function strength of mutant ACVR1 (classic ≈ 5.0)
- `sil` – residual mutant expression after silencing (1.0 = none)
- `inh_k` – kinase / canonical pathway inhibition (1.0 = none)
- `inh_noncan` – non-canonical pathway inhibition

**Protective Modifiers** (1.0 = no protection)
- `prot_inflam` – inflammation → signaling coupling (lower = protective)
- `prot_phos` – phosphatase / negative regulation strength (higher = protective)
- `prot_fap` – progenitor activation rate (lower = protective)
- `prot_noncan` – non-canonical amplification (lower = protective)
- `prot_repair` – basal repair capacity (higher = protective)

**Gene Therapy Delivery**
- `gt_efficiency` – maximum fraction of cells that can be corrected (0–1)
- `gt_onset` – time when gene therapy is administered
- `gt_rise_time` – time constant for correction to rise
- `gt_escape_rate` – slow loss of correction over time
- `residual_activity` – remaining mutant activity inside corrected cells

---

## Installation

```bash
# Required
pip install numpy scipy

# Optional but recommended (for CUDA acceleration)
pip install torch
```
By default the script runs 200 realizations and prints summary statistics.Important settings (inside if __name__ == "__main__")python

```python
results = run_ensemble(
    n_realizations=200,   # increase to 1000+ for publication-quality stats
    T_end=100.0,          # simulation time horizon
    seed=42,              # reproducibility
    use_cuda=True         # set False to force CPU
)
```

## Example Scenarios Included

|Scenario|Description|
|--------|-----------|
|Classic FOP||Untreated disease (R206H-like)|
|Realistic GT (55%)|Gene therapy with 55% efficiency + slow escape|
|Mild protective modifier|Natural genetic buffering (mild patient phenotype)|
You can easily add new scenarios by editing the `scenarios` dictionary in `run_ensemble()`.

## Interpreting Results
Typical output:

======================================================================
Scenario                        HO mean   HO std   Repair mean
----------------------------------------------------------------------
Classic FOP                       11.xxx    2.xxx        0.64x
Realistic GT (55%)                 8.xxx    2.xxx        1.5x
Mild protective modifier           3.xxx    0.9xx        2.2x


- **HO mean / std** – average final heterotopic bone volume and variability across random flare sequences  
- **Repair mean** – average homeostatic capacity (higher is better)  
- Strong control is usually defined as low HO **while** maintaining a good repair score

## Extending the Model

Adding a new interventionpython
```python
"My new strategy": {
    "mut": 5.0,
    "sil": 0.12,
    "inh_k": 0.40,
    "gt_efficiency": 0.60,
    "gt_onset": 15.0,
    # ... other parameters
}
```

## Changing flare frequencypython
```python
generate_poisson_flares(T_end, rate_per_unit=0.07)  # more frequent flares
```

## Combining protective background + gene therapy
Just set both the `prot_*` and `gt_*` parameters in the same scenario dictionary.
---

Biological Background (short)
FOP is caused by heterozygous gain-of-function mutations in ACVR1 (most commonly R206H). The mutant receptor becomes responsive to Activin A and drives inappropriate BMP signaling, converting soft-tissue progenitors into bone after inflammatory triggers.The model captures:
- Ligand-dependent and inflammation-driven signaling
- Both canonical and non-canonical pathways implicated in HO expansion
- The critical trade-off between stopping pathological bone formation and preserving normal repair

---
## Limitations & Future Directions
### Current limitations
- Single well-mixed tissue compartment (no spatial anatomy yet)
- Fixed-step integrator on GPU (can be replaced by adaptive solvers)
- Simplified non-canonical aggregation

### Suggested next improvements
- Spatial / multi-site model (axial vs appendicular)
- Lifetime-scale simulations (map time units → years)
- Full pharmacokinetic/pharmacodynamic layers for real drugs
- Global sensitivity analysis (Sobol indices)
- Coupling to patient-specific CT natural-history data
---
## License
This is a research / educational computational model.
You are free to use, modify, and extend it for any purposes.





