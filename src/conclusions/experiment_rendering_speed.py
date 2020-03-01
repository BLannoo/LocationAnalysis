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

import matplotlib.pyplot as plt

sys.path.append(root_location)

from src.tools.pre_processing import read_csv_as_geopandas
from src.tools.visualising import (
    load_or_get_belgium_roads,
    determine_extrema_with_border,
)

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/samples/year_2018_country_Belgium.csv"

# %% [markdown]
# # Load data

# %%
gdf = read_csv_as_geopandas(input_file_name)

# %% [markdown]
# # Select 1 day of data (2018/12/01)

# %%
selection = gdf[(gdf.month == 12) & (gdf.day == 1)]

# %% [markdown]
# # Render all roads of Belgium

# %%
# %%time

(
    x_max_with_border,
    x_min_with_border,
    y_max_with_border,
    y_min_with_border,
) = determine_extrema_with_border(selection)

ax = load_or_get_belgium_roads(repository_root_location=root_location).plot(
    edgecolor="gray", figsize=(10, 6), zorder=-1
)
selection.plot(ax=ax, marker="o", color="red", markersize=15, zorder=0)

# plt.xlim([x_min_with_border, x_max_with_border])
# plt.ylim([y_min_with_border, y_max_with_border])

# %% [markdown]
# # Render only the roads that are near to the data

# %%
# %%time

(
    x_max_with_border,
    x_min_with_border,
    y_max_with_border,
    y_min_with_border,
) = determine_extrema_with_border(selection)

gdf_belgian_roads = load_or_get_belgium_roads(repository_root_location=root_location)

ax = gdf_belgian_roads.cx[x_min_with_border:x_max_with_border, y_min_with_border:y_max_with_border].plot(
    edgecolor="gray", figsize=(10, 6), zorder=-1
)
selection.plot(ax=ax, marker="o", color="red", markersize=15, zorder=0)

# plt.xlim([x_min_with_border, x_max_with_border])
# plt.ylim([y_min_with_border, y_max_with_border])

# %%
