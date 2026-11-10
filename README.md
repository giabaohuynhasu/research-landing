# Third Order Audit

Structural auditing framework for research papers.

This project evaluates:

1. Falsification conditions
2. External checkability
3. Revision patterns

It does NOT assess whether claims are true.

---

## Installation

```bash
pip install -r requirements.txt
```

Set API key:

```bash
export OPENAI_API_KEY="YOUR_KEY"
```

Run:

```bash
python app.py
```

Paste a paper and terminate with:

```text
END
```

---

## Output

### Order 1

- Claims
- Falsification conditions

### Order 2

- External checkability analysis

### Order 3

- Revision classifications
- Ratio calculations

### Summary

- Pass/Fail overview
# Gia Bao Huynh
Independent Researcher — Political Philosophy, Bioethics, Philosophy of Technology

Gia Bao Huynh is an independent researcher based in Ho Chi Minh City, Vietnam, working across political philosophy, bioethics, and the philosophy of technology. His research is developed through an explicit, documented collaboration with AI systems rather than presented as conventional unaided scholarship. Everything listed below is posted as timestamped preprints — not peer-reviewed publications — so the sequence of the argument, not just its conclusions, is preserved.

## Research focus
- **Longevity & Political Legitimacy** — As AI-driven biotech starts to make extra years of healthy life partly a function of wealth, this strand asks what that does to distributive justice, the welfare state, and the assumption that everyone eventually dies on comparable terms.
- **AI Personhood** — Whether self-improving AI systems force existing theories of personhood, rights, and moral status to confront a boundary they were never built to resolve — and whether humans have unilateral authority to draw that line in the first place.
- **Diffusion & Bottlenecks** — Uses queueing theory to model how scarce, life-altering technologies — AI capability, longevity treatments — actually diffuse through a population, and what happens to access and legitimacy when demand outpaces supply.
- **Institutions & History** — A comparative-historical project, borrowing selection logic from evolutionary biology, on why some institutions survive collapse and regime change across centuries while structurally similar ones don't.
- **Academic Politics** — A historical account of how scholarly gatekeeping — peer review, grant panels, hiring networks — evolved out of older patronage systems, and how much of today's "merit-based" selection still runs on that logic.
- **Method & Epistemology** — A reflective strand on the work's own process: what standards of evidence and trust should apply to philosophy produced in real-time collaboration with an AI system.

## Selected work
- *War Correspondent Philosophy: Method, Evidence, and the Ethics of Research Under a Closing Window* (6-volume monograph, book) — DOI: https://doi.org/10.5281/zenodo.22822023 · PhilPapers: [HUYWCP-3](https://philpapers.org/rec/HUYWCP-3) · Academia: [Academia #175807018](https://www.academia.edu/175807018/War_Correspondent_Philosophy_Method_Evidence_and_the_Ethics_of_Research_Under_a_Closing_Window)  
  - *Vol. I: The Embedded Witness* — DOI: https://doi.org/10.5281/zenodo.22822028 · PhilPapers: [HUYTEW-2](https://philpapers.org/rec/HUYTEW-2) · Academia: [Academia #175806150](https://www.academia.edu/175806150/War_Correspondent_Philosophy_Vol_I_The_Embedded_Witness)  
  - *Vol. II: Falsification and Epistemic Self-Governance* — DOI: https://doi.org/10.5281/zenodo.22822030 · PhilPapers: [HUYFAE](https://philpapers.org/rec/HUYFAE) · Academia: [Academia #175779803](https://www.academia.edu/175779803/War_Correspondent_Philosophy_Vol_II_Falsification_and_Epistemic_Self_Governance)  
  - *Vol. III: Corpus Temporalism* — DOI: https://doi.org/10.5281/zenodo.22822032 · PhilPapers: [HUYCTT](https://philpapers.org/rec/HUYCTT) · Academia: [Academia #175780429](https://www.academia.edu/175780429/War_Correspondent_Philosophy_Vol_III_Corpus_Temporalism)  
  - *Vol. IV: Human–AI Epistemology* — DOI: https://doi.org/10.5281/zenodo.22822034 · PhilPapers: [HUYHES](https://philpapers.org/rec/HUYHES) · Academia: [Academia #175780492](https://www.academia.edu/175780492/War_Correspondent_Philosophy_Vol_IV_Human_AI_Epistemology)  
  - *Vol. V: Mechanism Transfer and Domain Portability* — DOI: https://doi.org/10.5281/zenodo.22822036 · PhilPapers: [HUYMTA](https://philpapers.org/rec/HUYMTA) · Academia: [Academia #175801301](https://www.academia.edu/175801301/War_Correspondent_Philosophy_Vol_V_Mechanism_Transfer_and_Domain_Portability)  
  - *Vol. VI: The Prospective and Self-Revising Life of a Framework* — DOI: https://doi.org/10.5281/zenodo.22822038 · PhilPapers: [HUYTPA-3](https://philpapers.org/rec/HUYTPA-3) · Academia: [Academia #175806753](https://www.academia.edu/175806753/War_Correspondent_Philosophy_Vol_VI_The_Prospective_and_Self_Revising_Life_of_a_Framework)  
- *Till Death Tear Us Apart: A Structural Analysis of the Longevity Asymmetry and the Closing Window* (book) — https://zenodo.org/records/20777406  
- *In the Name of Merit: Six Gatekeeping Mechanisms, from the Hundred Schools of Thought to the Algorithmic Archive* (book) — https://zenodo.org/records/21599600

## Contact
- Email: huynhbao@asu.edu  
- LinkedIn: http://www.linkedin.com/in/baojunhuynh  
- ORCID: https://orcid.org/0009-0008-2372-5852  
- PhilPeople: https://philpeople.org/profiles/gia-bao-huynh  
- Academia: https://independent.academia.edu/GiaB%E1%BA%A3oHu%E1%BB%B3nh30  
- Google Scholar: https://scholar.google.com/citations?user=P52UxDMAAAAJ&hl=en


---

## 📊 Applied Data Science & Econometric Modeling Systems

An end-to-end collection of eight quantitative data science, econometric forecasting, and machine learning systems built on real-world empirical datasets across Latin America, East Africa, South Asia, Central Europe, and North America ([`applied-data-science-portfolio/`](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio)):

| System Module | Empirical Dataset & Domain | Econometric & ML Architecture |
| :--- | :--- | :--- |
| **[01 · Mexican Real Estate Valuation](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/01-mexico-real-estate-analytics)** | `21,000+` residential property listings across Mexican states & Distrito Federal | Multi-source tabular normalization, geospatial Mapbox visualization, regional price-per-$\text{m}^2$ distributions, Pearson correlation analysis |
| **[02 · Buenos Aires Hedonic Pricing Pipeline](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/02-buenos-aires-hedonic-housing-pipeline)** | Urban apartment listings across Capital Federal (`Properati` dataset) | Interdecile outlier trimming, spatial coordinate surface modeling, `OneHotEncoder` neighborhood fixed effects, $L_2$-penalized `Ridge` regression |
| **[03 · Nairobi PM2.5 Air Quality Forecasting](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/03-nairobi-pm25-air-quality-forecasting)** | High-frequency IoT particulate telemetry (`SensorAfrica` Nairobi sensor network) | MongoDB document ingestion, `Africa/Nairobi` timezone localization, 1-hour mean resampling, ACF/PACF diagnostics, $\text{ARMA}(2, 1)$ forecasting |
| **[04 · Nepal Seismic Structural Damage Modeling](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/04-nepal-seismic-structural-damage-modeling)** | Post-2015 Gorkha Earthquake engineering survey across Kavrepalanchok & Gorkha | Multi-table SQLite relational joins, `LogisticRegression` odds ratios, `DecisionTreeClassifier` depth tuning, Gini importance, cross-district transferability |
| **[05 · Corporate Bankruptcy Imbalanced Ensembles](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/05-corporate-bankruptcy-imbalanced-ensemble)** | `64` accounting & liquidity ratios of Polish firms (`<5%` insolvency rate) | Compressed JSON ingestion, `RandomOverSampler` / `RandomUnderSampler`, `RandomForest` & `GradientBoosting` ensembles, Precision-Recall threshold optimization |
| **[06 · U.S. Household Wealth Segmentation](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/06-household-wealth-unsupervised-clustering)** | U.S. Federal Reserve Survey of Consumer Finances (`SCF`) balance-sheet microdata | Credit-constrained household profiling, `StandardScaler` + `KMeans` segmentation, Silhouette diagnostics, `PCA` 2D latent factor extraction, interactive `Dash` app |
| **[07 · Automated NoSQL A/B Experimentation Engine](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/07-ab-experimentation-etl-conversion-engine)** | Digital applicant funnel telemetry & randomized treatment logs | Custom `MongoRepository` ETL pipeline (`extract`, `transform`, `load`), statistical power analysis (`GofChisquarePower`), contingency table Pearson $\chi^2$ testing |
| **[08 · Equity Volatility GARCH(1,1) Microservice](https://github.com/giabaohuynhasu/research-landing/tree/main/applied-data-science-portfolio/08-financial-volatility-garch-microservice)** | Indian equity market daily OHLCV histories (`AMBUJACEM.BSE`, `SUZLON.BSE`) | Test-driven `AlphaVantageAPI` & `SQLRepository` layer, `arch` $\text{GARCH}(1, 1)$ conditional variance estimation, 500-step walk-forward validation, `FastAPI` `/fit` & `/predict` service |

> **Data & Research Attribution:** Empirical datasets, domain problem formulations, and foundational research infrastructure are credited to **[WorldQuant University](https://www.wqu.edu/)** (*Applied Data Science Lab*).
