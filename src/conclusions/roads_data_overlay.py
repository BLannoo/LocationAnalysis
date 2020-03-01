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

from src.tools.pre_processing import read_csv_as_geopandas
from src.tools.visualising import show_data_over_roads

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/samples/year_2018_country_Belgium.csv"

# %% [markdown]
# # Load data

# %%
# %%time

gdf = read_csv_as_geopandas(input_file_name)

# %% [markdown]
# # Show gps data against Belgian roads

# %%
# %%time

show_data_over_roads(gdf)

# %% [markdown]
# # Show Leuven

# %%
# %%time

show_data_over_roads(gdf, zorder_roads=1)

plt.xlim([46_700_000 / 10_000_000, 47_400_000 / 10_000_000])
plt.ylim([508_400_000 / 10_000_000, 509_000_000 / 10_000_000])

# %% [markdown]
# # Show 1 day

# %%
# %%time

show_data_over_roads(gdf[(gdf.year == 2018) & (gdf.month == 12) & (gdf.day == 25)])

# %%
