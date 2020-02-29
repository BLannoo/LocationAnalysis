import json
import math

import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Point

# takes around 4s
BELGIUM_ROADS = gpd.read_file("../data/raw/Belgium/belgium-roads-shape/roads.shp")
BELGIUM_ROADS.crs = "epsg:4326"


# deprecated: only enhance the data if you need it
def load_data(data_file_name: str) -> pd.DataFrame:
    df = load_primary_data(data_file_name)
    df = enhance_with_derived_data(df)
    return df


def load_primary_data(data_file_name: str):
    with open(data_file_name) as data_file:
        data_json = json.load(data_file)
    df = pd.DataFrame({
        "timestampMs": [int(p["timestampMs"]) for p in data_json["locations"]],
        "latitudeE7": [p["latitudeE7"] for p in data_json["locations"]],
        "longitudeE7": [p["longitudeE7"] for p in data_json["locations"]],
        "accuracy": [p["accuracy"] for p in data_json["locations"]]
    })
    return df


def enhance_with_derived_data(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df.timestampMs, unit="ms")
    df["year"] = pd.DatetimeIndex(df.date).year
    df["month"] = pd.DatetimeIndex(df.date).month
    df["day"] = pd.DatetimeIndex(df.date).day
    df["hour"] = pd.DatetimeIndex(df.date).hour

    df["time_of_day"] = (df.timestampMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    df["duration"] = (df.timestampMs.shift(1) - df.timestampMs.shift(-1)) / 2 / (1000 * 60 * 60)

    return df


# deprecated: load the data yourself
def load_geo_data(data_file_name: str) -> gpd.GeoDataFrame:
    df = load_data(data_file_name)
    return transform_to_geo_data(df)


def transform_to_geo_data(df):
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
    gdf.crs = "epsg:4326"
    return gdf


def enhance_with_countries(gdf: pd.DataFrame) -> gpd.GeoDataFrame:
    if type(gdf) != gpd.GeoDataFrame:
        gdf = transform_to_geo_data(gdf)

    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    world.crs = "epsg:4326"
    world.rename(columns={"name": "country"}, inplace=True)

    gdf_with_countries = gpd.sjoin(gdf, world, how="inner", op="intersects")

    gdf_with_countries.drop(
        ["index_right", "pop_est", "gdp_md_est", "iso_a3", "continent"]
        , axis=1, inplace=True
    )

    return gdf_with_countries


def filter_points_in_belgium(gdf: pd.DataFrame) -> gpd.GeoDataFrame:
    gdf_with_countries = enhance_with_countries(gdf)

    return gdf_with_countries[gdf_with_countries["country"] == "Belgium"]


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


def determine_extrema_with_border(
        gdf,
        relative_border_size=0.1,
        absolute_border_size=0.01
):
    bounds = gdf.geometry.bounds

    x_min = bounds.minx.min()
    x_max = bounds.maxx.max()
    x_border = max(
        (x_max - x_min) * relative_border_size,
        absolute_border_size
    )
    x_min_with_border = x_min - x_border
    x_max_with_border = x_max + x_border

    y_min = bounds.miny.min()
    y_max = bounds.maxy.max()
    y_border = max(
        (y_max - y_min) * relative_border_size,
        absolute_border_size
    )
    y_min_with_border = y_min - y_border
    y_max_with_border = y_max + y_border

    return (
        x_max_with_border,
        x_min_with_border,
        y_max_with_border,
        y_min_with_border
    )


def show_data_over_roads(
        gdf: gpd.GeoDataFrame,
        zorder_roads: float = -1,
        ax=None
):
    if ax is None:
        _, ax = plt.subplots()
    
    (
        x_max_with_border,
        x_min_with_border,
        y_max_with_border,
        y_min_with_border
    ) = determine_extrema_with_border(gdf)

    BELGIUM_ROADS.plot(
        ax=ax,
        edgecolor="gray",
        zorder=zorder_roads
    )
    gdf.plot(
        ax=ax,
        marker="o",
        color="red",
        markersize=15,
        zorder=0
    )

    ax.set_xlim([x_min_with_border, x_max_with_border])
    ax.set_ylim([y_min_with_border, y_max_with_border])


def movement(df: pd.DataFrame) -> pd.Series:
    dx = df.longitudeE7.diff()
    dy = df.latitudeE7.diff()
    return np.sqrt(dx * dx + dy * dy)


def log(series: pd.Series, epsilon: float = 0.0001) -> pd.Series:
    return np.log(np.abs(series) + epsilon)
