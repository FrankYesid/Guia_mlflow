from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import pandas as pd


def build_pipeline(df: pd.DataFrame):
    y = df["Churn"].map({"Yes": 1, "No": 0})
    X = df.drop(columns=["Churn", "customerID"])
    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
    num_cols = X.select_dtypes(exclude=["object"]).columns.tolist()
    cat_transform = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    num_transform = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
        ]
    )
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", cat_transform, cat_cols),
            ("num", num_transform, num_cols),
        ]
    )
    clf = LogisticRegression(max_iter=1000)
    model = Pipeline(steps=[("preprocessor", preprocessor), ("clf", clf)])
    return X, y, model
