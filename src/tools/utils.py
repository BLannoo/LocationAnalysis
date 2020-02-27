from datetime import datetime
import pandas as pd
import numpy as np


def as_timestampMs(date_string: str, date_format: str = "%Y-%m-%dT%H:%M:%S"):
    date = datetime.strptime(date_string, date_format)
    return date.timestamp() * 1000


def approx_abs_log(series: pd.Series, epsilon: float = 0.0001) -> pd.Series:
    return np.log(np.abs(series) + epsilon)
