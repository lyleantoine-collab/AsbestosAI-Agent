#!/usr/bin/env python3
"""
AsbestosAI-Agent: Dene-built fungal bioremediation simulator
Gift to Dr. Martin Pritchard & Leeds Beckett University
Author: Lyle Antoine | Natekco Labs
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv
import os

# === Leeds-Inspired Strain Data (Chrysotile Degradation) ===
strains = {
    'Aspergillus_niger': {
        'degrad_rate': 0.045,      # % mass loss per day
        'toxin_reduction': 0.40,   # 40% toxin mobility drop
        'temp_opt': 28,            # °C
        'name': 'Aspergillus niger'
    },
    'Penicillium_chrysogenum': {
        'degrad_rate': 0.035,
        'toxin_reduction': 0.52,
        'temp_opt': 25,
        'name': 'Penicillium chrysogenum'
    }
}

def simulate_degradation(strain_name='Aspergillus_niger', days=180, initial_fibers=1000):
    """Simulate fungal asbestos fiber degradation over time."""
    if strain_name not in strains:
        print(f"Warning: Strain '{strain_name}' not found. Using 'Aspergillus_niger'.")
        strain_name = 'Aspergillus_niger'
    
    strain = strains[strain_name]
    x = np.arange(days + 1)
    y = initial_fibers * np.exp(-strain['degrad_rate'] * x)

    # Risk Score: (toxin_reduction_factor * % fiber reduction)
    final_reduction = (initial_fibers - y[-1]) / initial_fibers * 100
    risk_score = strain['toxin_reduction'] * (final_reduction / 100)

    # === Plot ===
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"{strain['name']}", linewidth=2.5, color='#1f77b4')
    plt.title(f"Asbestos Fiber Degradation: {strain['name']}", fontsize=14, pad=15)
    plt.xlabel("Days", fontsize=12)
    plt.ylabel("Fibers Remaining", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig("degradation_plot.png", dpi=300)
    plt.close()

    # === CSV Report ===
    os.makedirs("output", exist_ok=True)
    with open("output/degradation_report.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Day', 'Fibers_Remaining', 'Reduction_%'])
        for i in range(0, days + 1, 30):  # Sample every 30 days
            reduction = (initial_fibers - y[i]) / initial_fibers * 100
            writer.writerow([i, round(y[i], 2), round(reduction, 2)])

    # === Final Output ===
    print(f"\nFinal Reduction: {final_reduction:.1f}%")
    print(f"Risk Score: {risk_score:.3f} (lower = safer)")
    print("Plot saved: degradation_plot.png")
    print("CSV saved: output/degradation_report.csv\n")

    return y, final_reduction, risk_score

# === CLI ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AsbestosAI-Agent: Fungal Bioremediation Simulator")
    parser.add_argument('--strain', type=str, default='Aspergillus_niger',
                        choices=list(strains.keys()), help="Fungal strain to simulate")
    parser.add_argument('--days', type=int, default=180, help="Simulation duration in days")
    parser.add_argument('--initial_fibers', type=int, default=1000, help="Initial fiber mass (arbitrary units)")
    
    args = parser.parse_args()
    simulate_degradation(args.strain, args.days, args.initial_fibers)
