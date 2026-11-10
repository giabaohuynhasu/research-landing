# Module 04: Post-Earthquake Structural Damage Classification in Nepal

## Overview
Supervised classification of severe building damage resulting from the **April 2015 Gorkha Earthquake** in Nepal, utilizing post-disaster engineering survey records stored in a relational SQLite database.

## Analytical Workflow
1. **`01_Relational_SQL_Extraction_and_Feature_Engineering.ipynb`** — Multi-table SQL joins across municipal mapping, structural attributes, and damage grades to construct a binary severe-damage indicator.
2. **`02_Bivariate_Seismic_Vulnerability_Exploration.ipynb`** — Empirical risk analysis across foundation types, roof materials, plinth area, and building height.
3. **`03_Logistic_Regression_Damage_Classifier.ipynb`** — Linear classification with one-hot encoded structural features and coefficient odds-ratio interpretation.
4. **`04_Decision_Tree_Structural_Risk_Optimization.ipynb`** — Non-linear tree classification with validation-curve hyperparameter tuning (`max_depth`) and Gini feature importance ranking.
5. **`05_Cross_District_Model_Generalization_Gorkha_Kavre.ipynb`** — Socioeconomic vulnerability analysis and cross-district transferability testing between Kavrepalanchok and Gorkha.

*Dataset & problem formulation credited to WorldQuant University (data originally collected by Open Data Nepal / Central Bureau of Statistics).*
