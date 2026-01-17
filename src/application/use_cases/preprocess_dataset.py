from pathlib import Path
from src.infrastructure.repositories.csv_churn_dataset_repository import CSVChurnDatasetRepository
from src.infrastructure.services.processing_utils import clean_telco_df
from src.config import settings


def preprocess_and_save(output_path: Path | None = None) -> Path:
    repo = CSVChurnDatasetRepository(settings.DATA_FILE)
    df = repo.load()
    df_clean = clean_telco_df(df)
    out = output_path or settings.PROCESSED_FILE
    out.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(out, index=False)
    return out
