# Longevity Resonance Queueing Simulation (Evo 2 & λ-Generative Event)

This repository contains a runnable Monte Carlo simulation and technical notes that implement a queueing-based model of how fast frontier biological discoveries can widen the gap in healthy life years between early adopters and the rest of the population. The model integrates the post‑August 2026 "Evo 2" shift — an empirical change in discovery dynamics that adds a rapidly growing, de‑novo generative component to the event arrival rate — into a time‑varying arrival process and a limited diffusion capacity.

This document is a short technical readme that explains the model, simulation parameters, how to run the code, and the core policy implications reported by the simulation.

---

## Model overview

- The gap Δ(t) in expected healthy life years is modeled as the virtual waiting time (workload) of a queueing process.
- Random discovery events arrive with a time‑varying rate λ(t). Each event produces a positive jump in Δ(t) (a benefit captured by a jump size δ).
- Diffusion of the benefit through the population is modeled as continuous service that reduces Δ(t) at rate μ (years of benefit diffused per year).
- Evo 2 introduces a second, de‑novo generative component to the arrival rate so that
  λ(t) = λ_BZM(t) + λ_gen(t),
  where λ_BZM(t) is the exponentially growing discovery rate seen before Evo 2, and λ_gen(t) is a de‑novo component that activates at the Evo 2 time and grows rapidly.
- The system becomes permanently unstable (the gap can grow without bound) when the effective traffic intensity exceeds 1. Writing μ' = μ / E[δ], instability occurs when λ(t) > μ'. The critical time t* solves λ(t*) = μ'.

---

## Calibration and default parameters

The code uses the following default calibration (chosen for demonstration and to reproduce the figures from the analysis):

- Baseline discovery rate: λ_0 = 0.5 events/year
- Frontier growth rate: r_A = 1.85 year^{-1}
- De‑novo generation baseline: λ_gen,0 = 0.15 events/year (activates at Evo 2)
- De‑novo growth rate: r_gen = 2.20 year^{-1}
- Evo 2 activation time: t_Evo2 = 0.15 years (≈ 06/08/2026 relative to the chosen baseline)
- Mean jump size: E[δ] = 1.5 years (lognormal distribution, variance = 0.25)
- Baseline gap at t=0: 7.3 years (used as an initial condition)

Scenarios for diffusion capacity (expressed as μ' in event‑equivalents/year):
1. Modest capacity: μ' = 1.5
2. Expanded capacity: μ' = 5.0
3. High capacity: μ' = 15.0

---

## How to run

Requirements:

```bash
python 3.10+
pip install numpy scipy matplotlib pandas
```

Run the simulation (default runs 100 Monte Carlo paths, draws quantile bands, and computes t*):

```bash
python3 alrp_simulation_model.py
```

Output:
- A plot (PNG) showing arrival rates and the expected gap Δ(t) for each scenario.
- A text summary printed to stdout with solved t* and mean gaps at selected times.

---

## Key simulation findings (illustrative)

Using the default calibration the simulation reproduces the following qualitative results:

- Modest capacity (μ' = 1.5): t* ≈ 0.47 years (roughly November 2026)
- Expanded capacity (μ' = 5.0): t* ≈ 1.10 years (roughly July 2027)
- High capacity (μ' = 15.0): t* ≈ 1.66 years (roughly February 2028)

Interpretation: large increases in diffusion capacity push the instability threshold outward only modestly; the critical time window for anticipatory governance is compressed.

---

## Reproducibility

The simulation uses a fixed random seed (seed=42) so results are reproducible. The code is intentionally simple and well‑documented to facilitate verification and modification.

---

## Repository structure (suggested)

```
alrp-longevity-simulation/
├── alrp_simulation_model.py    # Monte Carlo simulator (Python)
├── alrp_simulation_readme.md   # This document (English)
└── alrp_simulation_chart.png   # Example output chart (PNG)
```

Note: I will add the Python file and this English readme to the branch. If you want the PNG included as well, please confirm and either upload the binary here (base64) or allow me to add it from the workspace; otherwise I will provide instructions to add it manually through the GitHub web UI.
