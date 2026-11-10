# Module 02: Hedonic Housing Price Modeling in Buenos Aires

## Overview
End-to-end automated regression pipeline predicting apartment valuations (`price_aprox_usd`) in **Capital Federal, Buenos Aires** using physical dimensions, geospatial coordinates, and neighborhood (`barrio`) fixed effects.

## Analytical Workflow
1. **`01_Univariate_Surface_Area_Regression.ipynb`** — Baseline `LinearRegression` modeling property price as a function of covered surface area (`surface_covered_in_m2`) with interdecile outlier trimming.
2. **`02_Geospatial_Coordinate_Price_Modeling.ipynb`** — Spatial price surface modeling over latitude/longitude grids with `SimpleImputer` handling missing coordinate records.
3. **`03_Neighborhood_Encoding_and_Ridge_Regularization.ipynb`** — Categorical neighborhood encoding (`OneHotEncoder`) and $L_2$-penalized `Ridge` regression to mitigate high-dimensional overfitting.
4. **`04_Multivariate_Hedonic_Valuation_Pipeline.ipynb`** — Full multivariate feature engineering, collinearity filtering, and interactive prediction deployment.

*Dataset & problem formulation credited to WorldQuant University.*
