# Module 05: Corporate Bankruptcy Prediction Under Severe Class Imbalance

## Overview
Ensemble machine learning pipeline predicting corporate insolvency from 64 financial statement ratios of Polish manufacturing firms, addressing severe class imbalance (`<5%` bankruptcy incidence) and asymmetric misclassification costs.

## Analytical Workflow
1. **`01_Compressed_Financial_Statement_Ingestion.ipynb`** — Automated decompression (`gzip`) and JSON schema validation of corporate balance-sheet records.
2. **`02_Severe_Class_Imbalance_and_Resampling_Strategies.ipynb`** — Comparative evaluation of `RandomUnderSampler` and `RandomOverSampler` (`imbalanced-learn`) coupled with `DecisionTreeClassifier`.
3. **`03_Random_Forest_and_Precision_Recall_Thresholding.ipynb`** — `GridSearchCV` hyperparameter optimization of `RandomForestClassifier` and Precision-Recall trade-off analysis for regulatory capital allocation.
4. **`04_Gradient_Boosting_Insolvency_Classifier.ipynb`** — Boosted tree ensemble (`GradientBoostingClassifier`) optimization and `pickle` model serialization.

*Dataset & problem formulation credited to WorldQuant University.*
