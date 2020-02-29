import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib as mpl
import math


# TODO find the data from the root of the git-repo
BELGIAN_ROADS_FILE_NAME = "data/raw/Belgium/belgium-roads-shape/roads.shp"
BELGIAN_ROADS_CACHE = None


def show_data_over_roads(gdf: gpd.GeoDataFrame, zorder_roads: float = -1, ax=None):
    if ax is None:
        _, ax = plt.subplots()

    (
        x_max_with_border,
        x_min_with_border,
        y_max_with_border,
        y_min_with_border,
    ) = determine_extrema_with_border(gdf)

    ax = load_or_get_belgium_roads().plot(
        edgecolor="gray", figsize=(10, 6), zorder=zorder_roads
    )
    gdf.plot(ax=ax, marker="o", color="red", markersize=15, zorder=0)

    plt.xlim([x_min_with_border, x_max_with_border])
    plt.ylim([y_min_with_border, y_max_with_border])


def determine_extrema_with_border(
    gdf, relative_border_size=0.1, absolute_border_size=0.01
):
    bounds = gdf.geometry.bounds

    x_min = bounds.minx.min()
    x_max = bounds.maxx.max()
    x_border = max((x_max - x_min) * relative_border_size, absolute_border_size)
    x_min_with_border = x_min - x_border
    x_max_with_border = x_max + x_border

    y_min = bounds.miny.min()
    y_max = bounds.maxy.max()
    y_border = max((y_max - y_min) * relative_border_size, absolute_border_size)
    y_min_with_border = y_min - y_border
    y_max_with_border = y_max + y_border

    return (x_max_with_border, x_min_with_border, y_max_with_border, y_min_with_border)


def load_or_get_belgium_roads(
    belgian_roads_file_name: str = BELGIAN_ROADS_FILE_NAME,
    repository_root_location: str = "../../",
) -> gpd.GeoDataFrame:
    global BELGIAN_ROADS_CACHE
    if BELGIAN_ROADS_CACHE is None:
        # takes around 4s
        BELGIAN_ROADS_CACHE = gpd.read_file(
            repository_root_location + belgian_roads_file_name
        )
        BELGIAN_ROADS_CACHE.crs = "epsg:4326"
    return BELGIAN_ROADS_CACHE


def show_data_density(
    df: pd.DataFrame,
    title: str,
    long_min: int = -1_000_000_000,
    long_max: int = 1_000_000_000,
    lat_min: int = -1_000_000_000,
    lat_max: int = 1_000_000_000,
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
        norm=mpl.colors.LogNorm(),
    )
    plt.title(title, fontdict={"color": "lightgreen", "size": 20})


def plot_single_day(df: pd.DataFrame, year: int, month: int, day: int):
    selection = pd.DataFrame(
        df[
            (df.accuracy < 100)
            & (df.year == year)
            & (df.month == month)
            & (df.day == day)
        ]
    )

    sqrt_duration = selection.apply(
        lambda row: math.sqrt(row.duration * (1000 * 60 * 60)), axis=1
    )

    selection.plot.scatter(
        x="longitudeE7",
        xerr=selection.accuracy * 200,
        y="latitudeE7",
        c="time_of_day",
        s=sqrt_duration,
        figsize=(16, 10),
        colormap="viridis",
    )
