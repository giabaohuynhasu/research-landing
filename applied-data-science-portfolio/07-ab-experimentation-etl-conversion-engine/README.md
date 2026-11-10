# Module 07: Automated NoSQL ETL & Statistical A/B Experimentation Engine

## Overview
End-to-end experimentation and ETL system evaluating whether a structured orientation intervention significantly increases applicant conversion rates.

## Analytical Workflow
1. **`01_MongoDB_NoSQL_Cohort_Aggregation_Pipeline.ipynb`** — PyMongo aggregation pipelines extracting daily applicant sign-ups from semi-structured NoSQL documents.
2. **`02_Contingency_Table_ChiSquare_Hypothesis_Testing.ipynb`** — $2 \times 2$ contingency table construction and Pearson $\chi^2$ test of independence (`scipy.stats.chi2_contingency`) quantifying treatment lift and $p$-value significance.
3. **`03_Statistical_Power_and_Sample_Size_Simulation.ipynb`** — Experimental design and statistical power calculation (`GofChisquarePower`) determining required sample sizes across target effect sizes ($\alpha = 0.05$, $\text{power} = 0.80$).
4. **`04_Automated_ETL_and_Experimentation_Repository.ipynb`** — Object-oriented `MongoRepository` and `Experiment` runner automating participant assignment, ETL transformation, and statistical inference.

*Dataset & problem formulation credited to WorldQuant University.*
