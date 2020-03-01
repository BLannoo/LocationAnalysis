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

import matplotlib.pyplot as plt
import shapely.geometry as geometry

from src.tools.pre_processing import read_csv_as_geopandas
from src.tools.visualising import (
    determine_extrema_with_border,
    load_or_get_belgium_roads,
)

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/samples/year_2018_month_12_country_Belgium.csv"

# %% [markdown]
# # Load data

# %%
# %%time
gdf = read_csv_as_geopandas(input_file_name)

# %%
gdf.head()

# %% [markdown]
# # Backup geometry data

# %%
gdf["point"] = gdf.geometry

# %% [markdown]
# # Generate a context to each data point

# %%
# %%time

context_size = 25

for i in range(1, context_size):
    gdf["next-" + str(i)] = gdf.point.shift(i)
    
gdf.dropna(inplace=True)
gdf["geometry"] = gdf.apply(
    lambda row: geometry.LineString(
        [
            row["next-" + str(i)] 
            for i 
            in range(1, context_size)
        ]
    )
    , axis=1
)

gdf.drop(
    [
        "next-" + str(i)
        for i 
        in range(1, context_size)
    ],
    axis=1,
    inplace=True
)

# %%
gdf.head()

# %% [markdown]
# # Visualize 1 example

# %%
# %%time

partial_gdf = gdf.sample(1, random_state=0)

x_max_with_border, x_min_with_border, y_max_with_border, y_min_with_border = (
    determine_extrema_with_border(partial_gdf, absolute_border_size=0.003)
)

ax = load_or_get_belgium_roads(repository_root_location=root_location).plot(edgecolor="gray", figsize=(10, 6), zorder=-1)
partial_gdf.plot(ax=ax, edgecolor="red", zorder=0, linewidth=5)

plt.xlim([x_min_with_border, x_max_with_border])
plt.ylim([y_min_with_border, y_max_with_border])

partial_gdf.geometry

# %%
