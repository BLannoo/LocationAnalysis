import json
import pandas as pd

def json_to_csv(input_file_name: str) -> pd.DataFrame:
    with open(input_file_name) as file:
        data = json.load(file)['locations']
        return pd.DataFrame(
            {
                'timestampMs': [
                    data_point['timestampMs']
                    for data_point in data
                ],
                'latitudeE7': [
                    data_point['latitudeE7']
                    for data_point in data
                ],
                'longitudeE7': [
                    data_point['longitudeE7']
                    for data_point in data
                ],
                'accuracy': [
                    data_point['accuracy']
                    for data_point in data
                ],
                'activity': [
                    # get returns None for absent fields
                    data_point.get('activity')
                    for data_point in data
                ],
            }
        )
    
def enrich_data(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df.timestampMs, unit="ms")
    df["year"] = pd.DatetimeIndex(df.date).year
    df["month"] = pd.DatetimeIndex(df.date).month
    df["day"] = pd.DatetimeIndex(df.date).day
    df["hour"] = pd.DatetimeIndex(df.date).hour

    df["time_of_day"] = (
        df.timestampMs % (1000 * 60 * 60 * 24)
    ) / (1000 * 60 * 60)
    
    df["duration"] = (
        df.timestampMs.shift(1) - df.timestampMs.shift(-1)
    ) / 2 / (1000 * 60 * 60)

    return df