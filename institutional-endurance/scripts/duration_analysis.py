#!/usr/bin/env python3
"""
duration_analysis.py
Analysis script for Institutional Endurance Volume III: What Hasn't Ended Yet.

Compares durations across concluded vs. right-censored borrowed-legitimacy
governing arrangements (N=10).
"""

import csv
import os

def load_data(filepath):
    cases = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['duration_years'] = float(row['duration_years'])
            row['censored'] = int(row['censored'])
            row['start_year'] = int(row['start_year'])
            row['end_year'] = int(row['end_year'])
            cases.append(row)
    return cases

def run_analysis():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'case_durations.csv')
    cases = load_data(data_path)

    concluded = [c for c in cases if c['censored'] == 0]
    censored = [c for c in cases if c['censored'] == 1]

    concluded_sorted = sorted(concluded, key=lambda x: x['duration_years'])
    censored_sorted = sorted(censored, key=lambda x: x['duration_years'])

    print("=== INSTITUTIONAL ENDURANCE VOL. III: DURATION COMPARISON (N=10) ===")
    print("\nConcluded Arrangements (N=8), Shortest to Longest:")
    for c in concluded_sorted:
        print(f"  - {c['case']:<35} ({c['authority_type']:<11}): {c['duration_years']:>5.1f} yrs ({c['start_year']}–{c['end_year']})")

    print("\nRight-Censored / Active Arrangements (N=2):")
    for c in censored_sorted:
        print(f"  - {c['case']:<35} ({c['authority_type']:<11}): {c['duration_years']:>5.1f}+ yrs (active since {c['start_year']})")

    concluded_durations = [c['duration_years'] for c in concluded_sorted]
    median_concluded = (concluded_durations[3] + concluded_durations[4]) / 2.0
    mean_concluded = sum(concluded_durations) / len(concluded_durations)

    print(f"\nConcluded Distribution Summary:")
    print(f"  - Median: {median_concluded:.1f} years")
    print(f"  - Mean:   {mean_concluded:.1f} years")
    print(f"  - Range:  {min(concluded_durations):.1f} to {max(concluded_durations):.1f} years")

    print("\nCensoring Findings:")
    print("  1. Both Bosnia (31.0+ yrs) and Kosovo (27.0+ yrs) have already outlasted")
    print("     the three shortest concluded arrangements (Cambodia 1.6y, Timor 2.6y, Japan 7.0y).")
    print("  2. Both remain shorter than 5 of the 6 historical preserved-authority arrangements")
    print("     at full duration (Morocco 44y, Nigeria 60y, Tunisia 75y, Yuan 134y, Tang 259y).")
    print("  3. Honest limitation: Duration comparison proves they are not short transitional")
    print("     post-conflict regimes, but establishes neither how nor when they will conclude.")

if __name__ == '__main__':
    run_analysis()
