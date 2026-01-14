from typing import Protocol
import pandas as pd


class DatasetRepository(Protocol):
    def load(self) -> pd.DataFrame:
        ...
