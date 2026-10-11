import json
import csv
from pathlib import Path
from datetime import datetime
import numpy as np


def save_results(results, output_dir="results"):
    """
    Save Monte-Carlo results in three ways:
    1. Full raw data → JSON
    2. Summary statistics → single CSV
    3. One detailed CSV per strategy (every realization)
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Create a subfolder for per-strategy files
    detail_path = output_path / "per_strategy"
    detail_path.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # -------------------------------------------------
    # 1. Full raw results as JSON
    # -------------------------------------------------
    json_file = output_path / f"fop_results_{timestamp}.json"

    serializable = {}
    for name, data in results.items():
        serializable[name] = {
            "HO": [float(x) for x in data["HO"]],
            "repair": [float(x) for x in data["repair"]],
        }
        if "n_flares" in data:
            serializable[name]["n_flares"] = [int(x) for x in data["n_flares"]]

    with open(json_file, "w") as f:
        json.dump(serializable, f, indent=2)
    print(f"Full results saved to: {json_file}")

    # -------------------------------------------------
    # 2. Summary statistics CSV
    # -------------------------------------------------
    csv_summary = output_path / f"fop_summary_{timestamp}.csv"

    with open(csv_summary, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Strategy",
            "HO_mean", "HO_std", "HO_median", "HO_q05", "HO_q95",
            "Repair_mean", "Repair_std",
            "N_realizations"
        ])

        for name, data in results.items():
            ho = np.array(data["HO"])
            rep = np.array(data["repair"])

            writer.writerow([
                name,
                f"{ho.mean():.4f}",
                f"{ho.std():.4f}",
                f"{np.median(ho):.4f}",
                f"{np.percentile(ho, 5):.4f}",
                f"{np.percentile(ho, 95):.4f}",
                f"{rep.mean():.4f}",
                f"{rep.std():.4f}",
                len(ho)
            ])

    print(f"Summary saved to: {csv_summary}")

    # -------------------------------------------------
    # 3. One detailed CSV per strategy
    # -------------------------------------------------
    for name, data in results.items():
        # Clean filename
        safe_name = "".join(c if c.isalnum() or c in (
            "-", "_") else "_" for c in name)
        detail_file = detail_path / f"{safe_name}_{timestamp}.csv"

        ho = data["HO"]
        repair = data["repair"]
        n_flares = data.get("n_flares", [None] * len(ho))

        with open(detail_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["realization", "HO", "repair", "n_flares"])

            for i in range(len(ho)):
                writer.writerow([
                    i + 1,
                    f"{float(ho[i]):.6f}",
                    f"{float(repair[i]):.6f}",
                    n_flares[i] if n_flares[i] is not None else ""
                ])

        print(f"  Detailed results: {detail_file}")

    print(f"\nAll per-strategy files are in: {detail_path}/")
    return json_file, csv_summary, detail_path
