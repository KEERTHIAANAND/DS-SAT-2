"""Reproduce the Use Case 24 analysis from the included CSVs.
Note: bundled datasets are synthetic demonstration data, not company records.
"""
from pathlib import Path
import pandas as pd
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
raw = ROOT / "data" / "raw"
production = pd.read_csv(raw/"production.csv").drop_duplicates("batch", keep="first")
machines = pd.read_csv(raw/"machines.csv")
process = pd.read_csv(raw/"process.csv")
materials = pd.read_csv(raw/"materials.csv")
inspection = pd.read_csv(raw/"inspection.csv")
labels = {"surface crack":"Surface Crack","dimensional error":"Dimensional Error","porosity":"Porosity","burr":"Burr","weld defect":"Weld Defect","no defect":"No Defect"}
inspection["defect_type"] = inspection["defect_type"].astype(str).str.strip().str.lower().map(labels).fillna(inspection["defect_type"])
process.loc[~process["temperature"].between(120,260), "temperature"] = np.nan
process.loc[~process["pressure"].between(30,120), "pressure"] = np.nan
process.loc[~process["speed"].between(40,200), "speed"] = np.nan
clean = production.merge(machines,on="batch",how="left").merge(process,on="batch",how="left").merge(materials,on="batch",how="left").merge(inspection,on="batch",how="left")
clean["material_match"] = clean["supplier"].notna()
for c in ["temperature","pressure","speed"]: clean[c] = clean[c].fillna(clean[c].median())
clean["defect_rate_pct"] = clean["defect_count"] / clean["quantity"] * 100
clean["high_defect_flag"] = (clean["defect_rate_pct"] >= clean["defect_rate_pct"].quantile(.75)).astype(int)
clean["machine_hours_band"] = pd.cut(clean["operating_hours"],[0,3000,6000,9000,12000],labels=["0-3k","3k-6k","6k-9k","9k+"],include_lowest=True)
clean["process_deviation_score"] = np.sqrt(((clean["temperature"]-185)/12)**2+((clean["pressure"]-72)/7)**2+((clean["speed"]-115)/14)**2)
out = ROOT/"data"/"processed"/"cleaned_manufacturing_quality.csv"
out.parent.mkdir(parents=True,exist_ok=True); clean.to_csv(out,index=False)
print(f"Saved {len(clean)} batches to {out}")
