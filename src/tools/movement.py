import pandas as pd
import numpy as np


def movement(df: pd.DataFrame) -> pd.Series:
    dx = df.longitudeE7.diff()
    dy = df.latitudeE7.diff()
    return np.sqrt(dx * dx + dy * dy)
