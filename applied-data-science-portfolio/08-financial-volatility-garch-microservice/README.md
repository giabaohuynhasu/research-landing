# Module 08: Financial Volatility Modeling with GARCH(1,1) & FastAPI Deployment

## Overview
Production-ready financial econometrics microservice that ingests daily equity OHLCV prices (`AMBUJACEM.BSE`, `SUZLON.BSE`), persists records in SQLite, fits $\text{GARCH}(1, 1)$ conditional volatility models, validates forecasts via expanding-window walk-forward validation, and serves real-time volatility predictions over a `FastAPI` REST interface.

## Module Architecture
- **`config.py`** — Centralized application configuration (`db_name`, `model_directory`).
- **`data.py`** — `AlphaVantageAPI` client and `SQLRepository` database abstraction layer for reading and writing OHLCV time series.
- **`model.py`** — `GarchModel` lifecycle manager encapsulating `wrangle_data`, `fit`, `predict_volatility`, `dump`, and `load`.
- **`main.py`** — `FastAPI` service with `FitIn`/`FitOut` and `PredictIn`/`PredictOut` Pydantic schemas and `/hello`, `/fit`, and `/predict` endpoints.

## Analytical Notebooks
1. **`01_Equity_Return_Dynamics_and_Volatility_Clustering.ipynb`** — Log/percentage return properties, excess kurtosis, skewness, and 21-day rolling volatility dynamics.
2. **`02_Market_Data_Ingestion_and_SQLite_Repository.ipynb`** — Unit-tested implementation of `AlphaVantageAPI` and `SQLRepository`.
3. **`03_GARCH_1_1_Volatility_Modeling_and_Walk_Forward_Validation.ipynb`** — Squared-return ACF/PACF diagnostics, $\text{GARCH}(1, 1)$ estimation, standardized residual diagnostics, and 500-step walk-forward validation.
4. **`04_FastAPI_Volatility_Forecasting_Service.ipynb`** — End-to-end integration testing of model serialization (`joblib`) and REST API endpoints.

*Dataset & problem formulation credited to WorldQuant University.*
