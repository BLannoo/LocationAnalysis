import json
import math

import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Point


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
    df["hour"] = pd.DatetimeIndex(df.date).hour

    df["time_of_day"] = (df.timestampMs % (1000*60*60*24)) / (1000*60*60)
    df["date_diff"] = df.timestampMs.diff()*-1
    df['duration'] = (df.timestampMs.shift(1) - df.timestampMs.shift(-1)) / 2 / (1000 * 60 * 60)

    return df


def load_geo_data(data_file_name: str) -> gpd.GeoDataFrame:
    df = load_data(data_file_name)
    gdf = gpd.GeoDataFrame(
        df, geometry=[
            Point(xy)
            for xy in zip(
                df.longitudeE7 / 10_000_000,
                df.latitudeE7 / 10_000_000
            )
        ]
    )

    # Setting the geometry by hand: http://geopandas.org/projections.html
    gdf.crs = {'init': 'epsg:4326'}
    return gdf


def show_data_density(
        df: pd.DataFrame,
        title: str,
        long_min: int = -1_000_000_000,
        long_max: int = 1_000_000_000,
        lat_min: int = -1_000_000_000,
        lat_max: int = 1_000_000_000
):
    selection = df[
        (df.longitudeE7 > long_min)
        & (df.longitudeE7 < long_max)
        & (df.latitudeE7 > lat_min)
        & (df.latitudeE7 < lat_max)
        ]

    plt.figure(figsize=(16, 10))
    _, _, _, img = plt.hist2d(
        x=selection.longitudeE7,
        y=selection.latitudeE7,
        bins=300,
        norm=mpl.colors.LogNorm()
    )
    plt.title(title, fontdict={"color": "lightgreen", "size": 20})


def plot_single_day(
        df: pd.DataFrame,
        year: int,
        month: int,
        day: int
):
    df_part = pd.DataFrame(df[
                               (df.accuracy < 100)
                               & (df.year == year)
                               & (df.month == month)
                               & (df.day == day)
                               ])

    df_part["duration"] = df_part.timestampMs.diff() * -1
    sqrt_duration = df_part.apply(lambda row: math.sqrt(row.duration), axis=1)

    df_part.plot.scatter(
        x="longitudeE7",
        xerr=df_part.accuracy * 200,
        y="latitudeE7",
        c="time_of_day",
        s=sqrt_duration,
        figsize=(16, 10),
        colormap="viridis"
    )


def movement(df: pd.DataFrame) -> pd.Series:
    dx = df.longitudeE7.diff()
    dy = df.latitudeE7.diff()
    return np.sqrt(dx * dx + dy * dy)


def log(series: pd.Series, epsilon: float = 0.0001) -> pd.Series:
    return np.log(np.abs(series) + epsilon)
