# Applied Data Science & Quantitative Modeling Portfolio

**Author:** Gia Bao Huynh  
**Focus Areas:** Econometric Time-Series Forecasting · Hedonic Spatial Valuation · Imbalanced Classification · Unsupervised Wealth Segmentation · Production ML Microservices

---

## Overview

This repository contains an end-to-end collection of eight applied data science, statistical modeling, and machine learning systems built on real-world empirical datasets across emerging and developed markets. Each module addresses a concrete domain problem—from hedonic real estate pricing in Latin America and urban particulate matter ($\text{PM}_{2.5}$) forecasting in East Africa to post-seismic structural damage assessment in the Himalayas, corporate bankruptcy prediction in Central Europe, U.S. household balance-sheet segmentation, automated A/B experimentation pipelines, and a production GARCH(1,1) equity volatility microservice deployed with FastAPI.

---

## Repository Architecture

| Module | Domain & Empirical Dataset | Methodology & Engineering Stack |
| :--- | :--- | :--- |
| **[`01-mexico-real-estate-analytics`](./01-mexico-real-estate-analytics)** | **Mexican Residential Property Market** (`21,000+` listings across Mexican states & Distrito Federal) | Tabular data cleaning, geospatial scatter mapping (`Mapbox`), regional price-per-$\text{m}^2$ distributions, Pearson correlation analysis |
| **[`02-buenos-aires-hedonic-housing-pipeline`](./02-buenos-aires-hedonic-housing-pipeline)** | **Buenos Aires Urban Real Estate** (`Properati` multi-wave property records, Capital Federal) | Automated `wrangle()` ingestion, IQR outlier trimming, multicollinearity diagnostics, spatial interpolation, `OneHotEncoder` + `Ridge` ($L_2$) regularization |
| **[`03-nairobi-pm25-air-quality-forecasting`](./03-nairobi-pm25-air-quality-forecasting)** | **Nairobi Urban Air Quality Telemetry** (`SensorAfrica` high-frequency IoT $\text{PM}_{2.5}$ sensor logs) | MongoDB document extraction, UTC-to-`Africa/Nairobi` localization, hourly resampling, ACF/PACF lag identification, $\text{ARMA}(2, 1)$ time-series forecasting |
| **[`04-nepal-seismic-structural-damage-modeling`](./04-nepal-seismic-structural-damage-modeling)** | **2015 Gorkha Earthquake Building Assessment** (Open Data Nepal relational SQLite survey across Kavrepalanchok & Gorkha) | Multi-table SQL joins, binary damage target construction, `LogisticRegression` & `DecisionTreeClassifier` depth tuning, Gini feature importance, cross-district generalization |
| **[`05-corporate-bankruptcy-imbalanced-ensemble`](./05-corporate-bankruptcy-imbalanced-ensemble)** | **Polish Corporate Financial Statements** (`64` accounting & liquidity ratios under `<5%` insolvency rate) | Compressed JSON ingestion, median imputation (`SimpleImputer`), `RandomOverSampler` vs. `RandomUnderSampler`, `RandomForestClassifier`, `GradientBoostingClassifier`, Precision-Recall curve thresholding |
| **[`06-household-wealth-unsupervised-clustering`](./06-household-wealth-unsupervised-clustering)** | **U.S. Survey of Consumer Finances (SCF)** (Federal Reserve triennial household balance-sheet survey) | Credit-constrained subpopulation filtering, `StandardScaler` + `KMeans` clustering, Silhouette & inertia diagnostics, `PCA` 2D latent factor projection, interactive `Dash` web analytics app |
| **[`07-ab-experimentation-etl-conversion-engine`](./07-ab-experimentation-etl-conversion-engine)** | **Digital Applicant Conversion Funnel** (NoSQL user telemetry & randomized treatment assignment logs) | Custom MongoDB ETL pipeline (`extract`, `transform`, `load`), `statsmodels` power analysis (`GofChisquarePower`), contingency table $\chi^2$ independence testing (`scipy.stats.chi2_contingency`) |
| **[`08-financial-volatility-garch-microservice`](./08-financial-volatility-garch-microservice)** | **Indian Equity Market Volatility** (`AMBUJACEM.BSE` & `SUZLON.BSE` daily OHLCV histories via AlphaVantage) | Test-driven `AlphaVantageAPI` & `SQLRepository` persistence layer, `arch` $\text{GARCH}(1, 1)$ conditional variance estimation, walk-forward expanding-window validation, `FastAPI` + `Pydantic` `/fit` and `/predict` REST microservice |

---

## Key Technical Highlights

### 1. Spatial & Hedonic Econometrics (Modules 01–02)
- Processed raw multi-file Latin American real estate listings, resolving currency standardization, missing coordinate records, and extreme surface-area outliers (filtering to the middle 80% interdecile range).
- Addressed severe multicollinearity between total/covered surface area and latitude/longitude coordinates by combining `SimpleImputer`, `OneHotEncoder` (for `barrio` fixed effects), and `Ridge` regression inside unified `scikit-learn` pipelines.

### 2. High-Frequency Time-Series & Econometric Volatility (Modules 03 & 08)
- **Environmental Telemetry ($\text{PM}_{2.5}$):** Engineered a MongoDB-backed ingestion pipeline for Nairobi IoT particulate sensors, applying 1-hour mean resampling with forward-fill interpolation and fitting an $\text{ARMA}(2, 1)$ specification benchmarked against a persistence baseline.
- **Financial Volatility ($\text{GARCH}(1, 1)$):** Built a modular Python package (`config.py`, `data.py`, `model.py`, `main.py`) that ingests daily equity returns into SQLite, fits $\text{GARCH}(1, 1)$ models on log/percentage returns, evaluates out-of-sample performance via 500-step expanding-window walk-forward validation, serializes trained artifacts with `joblib`, and serves business-day ISO 8601 volatility forecasts over a `FastAPI` REST interface.

### 3. Post-Disaster Risk & Corporate Insolvency Classification (Modules 04–05)
- **Seismic Structural Vulnerability:** Extracted building-level engineering attributes (`foundation_type`, `roof_type`, `ground_floor_type`, `age_building`, `height_ft_pre_eq`, `plinth_area_sq_ft`) via relational SQL queries across `id_map`, `building_structure`, `building_damage`, and `household_demographics` tables to predict severe structural collapse following the 2015 Gorkha earthquake.
- **Imbalanced Financial Distress:** Mitigated extreme class skew in corporate bankruptcy records using non-parametric resampling (`imbalanced-learn`) and cost-sensitive threshold selection across `RandomForest` and `GradientBoosting` ensembles.

### 4. Unsupervised Balance-Sheet Segmentation & Statistical Experimentation (Modules 06–07)
- **Household Wealth Clustering:** Segmented credit-constrained U.S. households from the Federal Reserve's Survey of Consumer Finances (`SCF`) across debt-to-income, net worth, asset holdings, and age, projecting high-dimensional financial profiles onto orthogonal principal components (`PCA`) inside a reactive `Plotly Dash` dashboard.
- **Automated A/B Experimentation:** Architected a reusable `MongoRepository` and ETL workflow that aggregates daily registration cohorts, computes statistical power for target effect sizes, and executes Pearson $\chi^2$ contingency tests on treatment vs. control conversion rates.

---

## Setup & Reproducibility

```bash
# Clone the repository
git clone https://github.com/giabaohuynhasu/applied-data-science-portfolio.git
cd applied-data-science-portfolio

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

To launch the **Financial Volatility Forecasting API** (Module 08):

```bash
cd 08-financial-volatility-garch-microservice
uvicorn main:app --host 0.0.0.0 --port 8008
```

---

## Acknowledgments & Attribution

Special credit and appreciation to **[WorldQuant University](https://www.wqu.edu/)** and its **Applied Data Science Lab** faculty and curriculum engineering team for curating the foundational empirical datasets, domain problem formulations, and research infrastructure upon which these analytical pipelines and production implementations are built.

---

## License

This project is released under the [MIT License](./LICENSE).
