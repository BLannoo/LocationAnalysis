# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# auto format code at cell execution
# %load_ext lab_black

root_location = "../../"
import sys

sys.path.append(root_location)

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

from src.tools.pre_processing import transform_to_geo_data

# %matplotlib inline

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/samples/year_2018.csv"

# %% [markdown]
# # Load data

# %%
# %%time

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# %%
# %%time

gdf = transform_to_geo_data(pd.read_csv(input_file_name))

# %% [markdown]
# # Show gps data against world map

# %%
# %%time

gdf.plot(
    ax=world.plot(facecolor="lightgray", edgecolor="gray", figsize=(10, 6)),
    marker="o",
    color="red",
    markersize=15,
)

bounds = gdf.geometry.bounds

plt.xlim([bounds.minx.min() - 5, bounds.maxx.max() + 5])
plt.ylim([bounds.miny.min() - 5, bounds.maxy.max() + 5])

# %% [markdown]
# # Show time spend in each country

# %%
# %%time

country_summary = (
    gpd.sjoin(gdf, world, how="inner", op="intersects")
    .groupby("name")
    .agg({"duration": "sum"})
)

tot_duration = country_summary.duration.sum()

country_summary["%"] = country_summary.apply(
    lambda row: row.duration / tot_duration * 100, axis=1
)

country_summary.sort_values("duration", ascending=False)

# %%
