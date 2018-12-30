import json

import pandas as pd


def load_data(data_file_name: str) -> pd.DataFrame:
    with open(data_file_name) as data_file:
        data_json = json.load(data_file)

    df = pd.DataFrame({
        "raw": data_json["locations"],
        "timestampMs": [int(p['timestampMs']) for p in data_json["locations"]],
        "latitudeE7": [p['latitudeE7'] for p in data_json["locations"]],
        "longitudeE7": [p['longitudeE7'] for p in data_json["locations"]],
        "accuracy": [p['accuracy'] for p in data_json["locations"]]
    })

    # Derivatives
    df['date'] = pd.to_datetime(df['timestampMs'], unit='ms')
    df['year'] = pd.DatetimeIndex(df["date"]).year
    df['month'] = pd.DatetimeIndex(df["date"]).month
    df['day'] = pd.DatetimeIndex(df["date"]).day

    df['time_of_day'] = (df['timestampMs'] % (1000*60*60*24)) / (1000*60*60)
    df['date_diff'] = df['timestampMs'].diff()*-1

    return df
