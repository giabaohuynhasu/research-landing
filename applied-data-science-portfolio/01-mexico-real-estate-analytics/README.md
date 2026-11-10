# Module 01: Mexican Residential Real Estate Valuation & Spatial Analytics

## Overview
An empirical investigation of residential property valuations across Mexico (`21,000+` listings), examining the relative explanatory power of structural property size (`area_m2`) versus regional and geospatial location (`state`, `lat`, `lon`).

## Analytical Workflow
1. **`01_Tabular_Data_Ingestion_and_Cleaning.ipynb`** — Multi-source CSV ingestion, currency normalization (`MXN` to `USD`), coordinate parsing, and schema standardization.
2. **`02_Exploratory_Spatial_and_Price_Analysis.ipynb`** — Geospatial distribution visualization (`Mapbox`), histograms, and boxplot diagnostics of property size and valuation.
3. **`03_Regional_Market_Valuation_Comparison.ipynb`** — State-level aggregation comparing mean prices and price-per-square-meter across Mexican states.
4. **`04_Surface_Area_vs_Location_Determinants.ipynb`** — Sub-market correlation analysis contrasting high-density urban markets (`Distrito Federal`) with resort/regional states (`Guerrero`, `Morelos`).

*Dataset & problem formulation credited to WorldQuant University.*
