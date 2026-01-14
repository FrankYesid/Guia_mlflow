from pathlib import Path
import pandas as pd
from src.domain.repositories.dataset_repository import DatasetRepository


class CSVChurnDatasetRepository:
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.path)
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df = df.dropna(subset=["TotalCharges"])
        return df
