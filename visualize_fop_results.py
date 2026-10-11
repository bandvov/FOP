#!/usr/bin/env python3
"""
Virtual FOP – Results Visualization Script
------------------------------------------
Reads the summary CSV (or JSON) produced by the Monte-Carlo model
and generates useful plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import argparse

# Optional: make plots look nicer
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams["figure.figsize"] = (14, 8)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13


def load_summary(csv_path: str) -> pd.DataFrame:
    """Load the summary CSV produced by save_results()."""
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} strategies from {csv_path}")
    return df


def plot_ho_vs_repair(df: pd.DataFrame, output_dir: Path):
    """Scatter plot: HO mean vs Repair mean (main overview)."""
    plt.figure(figsize=(12, 9))

    scatter = plt.scatter(
        df["HO_mean"],
        df["Repair_mean"],
        s=120,
        c=df["HO_mean"],
        cmap="viridis_r",
        edgecolors="k",
        alpha=0.85
    )

    # Annotate the best points
    for _, row in df.nsmallest(8, "HO_mean").iterrows():
        plt.annotate(
            row["Strategy"],
            (row["HO_mean"], row["Repair_mean"]),
            textcoords="offset points",
            xytext=(8, 5),
            fontsize=8,
            alpha=0.9
        )

    plt.colorbar(scatter, label="HO mean")
    plt.xlabel("HO mean (lower is better)")
    plt.ylabel("Repair mean (higher is better)")
    plt.title("Virtual FOP – HO vs Repair Capacity")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    out = output_dir / "ho_vs_repair.png"
    plt.savefig(out, dpi=200)
    print(f"Saved: {out}")
    plt.close()


def plot_top_strategies(df: pd.DataFrame, output_dir: Path, top_n: int = 15):
    """Horizontal bar charts for the best strategies."""
    # Rank by a simple balanced score
    df = df.copy()
    df["Score"] = (11.2 - df["HO_mean"]) * df["Repair_mean"]
    top = df.nlargest(top_n, "Score").sort_values("Score")

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # HO
    axes[0].barh(top["Strategy"], top["HO_mean"], color="salmon")
    axes[0].set_xlabel("HO mean")
    axes[0].set_title(f"Top {top_n} Strategies – HO (lower better)")
    axes[0].invert_yaxis()

    # Repair
    axes[1].barh(top["Strategy"], top["Repair_mean"], color="mediumseagreen")
    axes[1].set_xlabel("Repair mean")
    axes[1].set_title(f"Top {top_n} Strategies – Repair (higher better)")
    axes[1].invert_yaxis()

    plt.tight_layout()
    out = output_dir / "top_strategies.png"
    plt.savefig(out, dpi=200)
    print(f"Saved: {out}")
    plt.close()


def plot_silencing_sweep(df: pd.DataFrame, output_dir: Path):
    """Plot pure silencing depth effect (if present)."""
    sil_rows = df[df["Strategy"].str.startswith("Sil_0.") &
                  ~df["Strategy"].str.contains("Kin")].copy()

    if sil_rows.empty:
        print("No pure silencing sweep found – skipping this plot.")
        return

    # Extract numeric sil value
    sil_rows["sil_value"] = sil_rows["Strategy"].str.extract(
        r"Sil_(\d+\.\d+)").astype(float)
    sil_rows = sil_rows.sort_values("sil_value")

    fig, ax1 = plt.subplots(figsize=(11, 6))

    color = "tab:red"
    ax1.set_xlabel("Silencing depth (sil)")
    ax1.set_ylabel("HO mean", color=color)
    ax1.plot(sil_rows["sil_value"], sil_rows["HO_mean"],
             "o-", color=color, linewidth=2, markersize=8)
    ax1.tick_params(axis="y", labelcolor=color)
    ax1.invert_xaxis()  # deeper silencing on the left

    ax2 = ax1.twinx()
    color = "tab:green"
    ax2.set_ylabel("Repair mean", color=color)
    ax2.plot(sil_rows["sil_value"], sil_rows["Repair_mean"],
             "s-", color=color, linewidth=2, markersize=8)
    ax2.tick_params(axis="y", labelcolor=color)

    plt.title("Effect of Silencing Depth (pure silencing)")
    fig.tight_layout()
    out = output_dir / "silencing_sweep.png"
    plt.savefig(out, dpi=200)
    print(f"Saved: {out}")
    plt.close()


def plot_heatmap_sil_kin(df: pd.DataFrame, output_dir: Path):
    """Heatmap of Silencing × Kinase combinations (robust version)."""

    # Keep only rows that look like Sil_X_Kin_Y
    mask = df["Strategy"].str.contains(r"Sil_0\.\d+_Kin_0\.\d+", na=False)
    sub = df[mask].copy()

    if sub.empty:
        print("No Sil×Kin grid found – skipping heatmap.")
        return

    # Extract numeric values
    sub["sil"] = sub["Strategy"].str.extract(r"Sil_(\d+\.\d+)").astype(float)
    sub["kin"] = sub["Strategy"].str.extract(r"Kin_(\d+\.\d+)").astype(float)

    # Remove any rows where extraction failed
    sub = sub.dropna(subset=["sil", "kin"])

    # ---- FIX: handle duplicates ----
    # If the same (sil, kin) pair appears more than once, keep the one with lowest HO
    sub = sub.sort_values("HO_mean").drop_duplicates(
        subset=["sil", "kin"], keep="first")

    if sub.empty:
        print("No valid Sil×Kin data after cleaning – skipping heatmap.")
        return

    # Create pivot tables
    pivot_ho = sub.pivot(index="sil", columns="kin", values="HO_mean")
    pivot_repair = sub.pivot(index="sil", columns="kin", values="Repair_mean")

    # Sort axes nicely
    pivot_ho = pivot_ho.sort_index().sort_index(axis=1)
    pivot_repair = pivot_repair.sort_index().sort_index(axis=1)

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.heatmap(
        pivot_ho,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd_r",
        ax=axes[0],
        linewidths=0.5
    )
    axes[0].set_title("HO mean (Silencing × Kinase)")
    axes[0].set_ylabel("Silencing depth (sil)")
    axes[0].set_xlabel("Kinase inhibition (inh_k)")

    sns.heatmap(
        pivot_repair,
        annot=True,
        fmt=".2f",
        cmap="YlGn",
        ax=axes[1],
        linewidths=0.5
    )
    axes[1].set_title("Repair mean (Silencing × Kinase)")
    axes[1].set_ylabel("Silencing depth (sil)")
    axes[1].set_xlabel("Kinase inhibition (inh_k)")

    plt.tight_layout()
    out = output_dir / "sil_kin_heatmap.png"
    plt.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved: {out}")
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Visualize Virtual FOP Monte-Carlo results")
    parser.add_argument("csv", type=str, help="Path to the summary CSV file")
    parser.add_argument("--outdir", type=str, default="plots",
                        help="Output directory for plots")
    args = parser.parse_args()

    output_dir = Path(args.outdir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_summary(args.csv)

    print("\nGenerating plots...")
    plot_ho_vs_repair(df, output_dir)
    plot_top_strategies(df, output_dir, top_n=15)
    plot_silencing_sweep(df, output_dir)
    plot_heatmap_sil_kin(df, output_dir)

    print("\nAll plots saved to:", output_dir.resolve())


if __name__ == "__main__":
    main()
