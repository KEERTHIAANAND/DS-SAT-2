# Manufacturing Quality Insight — Analysis Report

## Scope and data provenance
The supplied PDF describes five input CSVs but does not include the actual CSV datasets. To provide a complete runnable deliverable, the included raw CSVs are **synthetic demonstration data generated for this package**, not PrimeForge production records. Replace them with the official datasets before presenting results as real findings.

## Cleaning and preparation
- Raw files: `production.csv`, `machines.csv`, `process.csv`, `materials.csv`, `inspection.csv`.
- Production duplicate batches removed using `batch` as the key.
- Defect labels normalized to consistent title case.
- Process readings outside broad plausibility bounds were treated as missing; remaining missing process values were median-imputed for analysis.
- Tables joined at one row per batch. Unmatched material records remain visible through `material_match`.
- Engineered `defect_rate_pct`, `high_defect_flag`, `machine_hours_band`, `temperature_band`, and `process_deviation_score`.

## Demonstration findings (synthetic data)
- Overall defect rate: **7.34%**.
- Highest line defect rate: **Line C (10.39%)**.
- Highest shift defect rate: **Night (9.78%)**.
- Highest supplier defect rate among matched material records: **Crest Industrial (9.43%)**.
- These are descriptive associations, not proof that a condition causes defects. Confirm with actual data and process owners before acting.

## Feature engineering and selection
Categorical fields are one-hot encoded for the feature-selection table. `SelectKBest` with an F-test ranks candidate features against defect rate. PCA is demonstrated on standardized numeric process, machine-hour, quantity, and deviation features; inspect `pca_explained_variance.csv` to decide how many components are useful. PCA is exploratory rather than required if interpretability is more important.

## Recommended management priorities
1. Investigate the line, shift, and supplier groups with the highest observed defect rates.
2. Review process control limits and sensor calibration for temperature, pressure, and speed.
3. Check whether defect spikes cluster by machine operating-hours band and machine age.
4. Use a Pareto view to prioritize the defect categories accounting for the largest share.
5. Validate recommendations on official production data and monitor rates with consistent denominators.
