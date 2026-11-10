# Module 06: Unsupervised Segmentation of Credit-Constrained U.S. Households

## Overview
Unsupervised clustering and latent factor extraction on the **U.S. Federal Reserve Survey of Consumer Finances (SCF)**, profiling the balance sheets, income, and debt burdens of credit-constrained American households.

## Analytical Workflow
1. **`01_Federal_Reserve_SCF_Credit_Constraint_Exploration.ipynb`** — Demographic and balance-sheet comparison between credit-denied/discouraged (`TURNFEAR == 1`) and unconstrained households.
2. **`02_KMeans_Household_Balance_Sheet_Segmentation.ipynb`** — Feature standardization (`StandardScaler`) and `KMeans` clustering across net worth, total debt, home value, and income, optimizing cluster count $k$ via inertia and Silhouette scores.
3. **`03_PCA_Dimensionality_Reduction_and_Interpretation.ipynb`** — Principal Component Analysis (`PCA`) projecting multi-dimensional balance sheets onto a 2D visualization plane.
4. **`04_Interactive_Dash_Wealth_Segmentation_App.ipynb`** — Reactive `Plotly Dash` analytical web application for interactive feature selection and cluster exploration.

*Dataset & problem formulation credited to WorldQuant University (source data from the Board of Governors of the Federal Reserve System).*
