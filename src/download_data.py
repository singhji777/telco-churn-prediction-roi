"""Downloads the public IBM 'Telco Customer Churn' sample dataset into ../data/telco_churn.csv.
Usage:  python src/download_data.py
"""
import sys, urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "data" / "telco_churn.csv"
OUT.parent.mkdir(parents=True, exist_ok=True)
urllib.request.urlretrieve(URL, OUT)
print(f"saved {OUT} ({OUT.stat().st_size/1e3:.0f} KB)")
