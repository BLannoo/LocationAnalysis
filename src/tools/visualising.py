import geopandas as gpd
import matplotlib.pyplot as plt


# TODO find the data from the root of the git-repo
BELGIAN_ROADS_FILE_NAME = "../../data/raw/Belgium/belgium-roads-shape/roads.shp"
BELGIAN_ROADS_CACHE = None


def show_data_over_roads(gdf: gpd.GeoDataFrame, zorder_roads: float = -1):
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
    belgian_roads_cache: gpd.GeoDataFrame = BELGIAN_ROADS_CACHE,
):
    if belgian_roads_cache == None:
        # takes around 4s
        belgian_roads_cache = gpd.read_file(belgian_roads_file_name)
        belgian_roads_cache.crs = "epsg:4326"
    return belgian_roads_cache