import json

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def load_data(data_file_name: str) -> pd.DataFrame:
    with open(data_file_name) as data_file:
        data_json = json.load(data_file)

    df = pd.DataFrame({
        "raw": data_json["locations"],
        "timestampMs": [int(p["timestampMs"]) for p in data_json["locations"]],
        "latitudeE7": [p["latitudeE7"] for p in data_json["locations"]],
        "longitudeE7": [p["longitudeE7"] for p in data_json["locations"]],
        "accuracy": [p["accuracy"] for p in data_json["locations"]]
    })

    # Derivatives
    df["date"] = pd.to_datetime(df.timestampMs, unit="ms")
    df["year"] = pd.DatetimeIndex(df.date).year
    df["month"] = pd.DatetimeIndex(df.date).month
    df["day"] = pd.DatetimeIndex(df.date).day

    df["time_of_day"] = (df.timestampMs % (1000*60*60*24)) / (1000*60*60)
    df["date_diff"] = df.timestampMs.diff()*-1

    return df


def show_data_density(
        df: pd.DataFrame,
        title: str,
        long_min: int = -1_000_000_000,
        long_max: int = 1_000_000_000,
        lat_min: int = -1_000_000_000,
        lat_max: int = 1_000_000_000
):
    selection_long = (df.longitudeE7 > long_min) & (df.longitudeE7 < long_max)
    selection_lat = (df.latitudeE7 > lat_min) & (df.latitudeE7 < lat_max)
    selection = selection_long & selection_lat

    plt.figure(figsize=(16, 10))
    _, _, _, img = plt.hist2d(
        x=df[selection].longitudeE7,
        y=df[selection].latitudeE7,
        bins=300,
        norm=mpl.colors.LogNorm()
    )
    plt.title(title, fontdict={"color": "lightgreen", "size": 20})
