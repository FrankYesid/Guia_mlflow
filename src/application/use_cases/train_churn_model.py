from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import mlflow
import mlflow.sklearn
from src.infrastructure.pipelines.preprocessing import build_pipeline
from src.config import settings
import pandas as pd


def train_and_log(df: pd.DataFrame, run_name: str):
    X, y, model = build_pipeline(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=settings.TEST_SIZE, random_state=settings.RANDOM_STATE, stratify=y
    )
    with mlflow.start_run(run_name=run_name):
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("test_size", settings.TEST_SIZE)
        mlflow.log_param("random_state", settings.RANDOM_STATE)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        try:
            y_prob = model.predict_proba(X_test)[:, 1]
            auc = roc_auc_score(y_test, y_prob)
        except Exception:
            auc = None
        mlflow.log_metric("accuracy", acc)
        if auc is not None:
            mlflow.log_metric("roc_auc", auc)
        mlflow.sklearn.log_model(model, artifact_path="model")
        return acc, auc
