# Module 03: Urban Air Quality (PM2.5) Autoregressive Forecasting in Nairobi

## Overview
High-frequency environmental time-series modeling of particulate matter ($\text{PM}_{2.5}$) concentrations in **Nairobi, Kenya** using IoT sensor telemetry from the `SensorAfrica` network.

## Analytical Workflow
- **`01_SensorAfrica_ARMA_Time_Series_Forecasting.ipynb`** — Extracts nested sensor documents from MongoDB, localizes timestamps to `Africa/Nairobi`, resamples readings to 1-hour intervals, diagnoses autocorrelation structure via ACF/PACF plots, and fits an $\text{ARMA}(2, 1)$ forecasting model evaluated against a naive persistence benchmark.

*Dataset & problem formulation credited to WorldQuant University.*
