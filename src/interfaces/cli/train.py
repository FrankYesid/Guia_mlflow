from src.config import settings
from src.infrastructure.repositories.csv_churn_dataset_repository import CSVChurnDatasetRepository
from src.application.use_cases.train_churn_model import train_and_log
import mlflow


def main():
    mlflow.set_experiment(settings.MLFLOW_EXPERIMENT)
    repo = CSVChurnDatasetRepository(settings.DATA_FILE)
    df = repo.load()
    acc, auc = train_and_log(df, run_name="baseline")
    if auc is None:
        print(f"accuracy={acc:.4f}")
    else:
        print(f"accuracy={acc:.4f} roc_auc={auc:.4f}")


if __name__ == "__main__":
    main()
