from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
MLFLOW_EXPERIMENT = "churn_telco"
RANDOM_STATE = 42
TEST_SIZE = 0.2
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_FILE = PROCESSED_DIR / "telco_churn_clean.csv"
