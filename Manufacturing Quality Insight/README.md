# CH24 — Manufacturing Quality Insight (Rounds 2–4)

## Important dataset note
The supplied `CH24.pdf` specifies five input datasets (`production.csv`, `machines.csv`, `process.csv`, `materials.csv`, `inspection.csv`) but does **not** contain the actual CSV data. The raw CSVs in this ZIP are **synthetic demonstration data created to match the field descriptions and data-quality issues in the PDF**. Do not submit the synthetic results as actual company findings. Replace the raw CSVs with the official datasets and rerun the notebook.

## Folder structure
- `data/raw/`: five source-shaped CSV files
- `data/processed/`: cleaned merged dataset, feature-selection scores, PCA variance
- `notebooks/round2_eda_feature_engineering.ipynb`: Round 2 workflow
- `reports/`: interpretation report and charts
- `excel/Manufacturing_Quality_Analysis.xlsx`: Round 3 workbook with cleaned data, grouped analysis tables, charts, feature scores, PCA, and summary sheet
- `presentation/Manufacturing_Quality_Insights.pptx`: Round 4 business pitch
- `src/analyze.py`: reproducible cleaning script
- `requirements.txt`: Python dependencies

## Run
From this folder:
```bash
pip install -r requirements.txt
cd notebooks
jupyter notebook round2_eda_feature_engineering.ipynb
```
Or run the cleaning script:
```bash
python src/analyze.py
```

## Rounds covered
- Round 2: data quality checks, cleaning, joins, EDA, visualizations, engineered features, feature selection and PCA demonstration.
- Round 3: Excel workbook with summary, defect rate by line, defect-type Pareto data, shift comparison, process analysis, supplier comparison, machine-hours analysis and charts.
- Round 4: short pitch deck with evidence, caveats and recommended priorities.
Round 1 quiz is excluded as requested ("from Round 2").
