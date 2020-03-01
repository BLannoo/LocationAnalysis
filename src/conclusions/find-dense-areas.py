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
import pandas as pd
import geopandas as gpd
import matplotlib as mpl
import numpy as np

from src.tools.pre_processing import read_csv_as_geopandas, transform_to_geo_data
from src.tools.visualising import show_data_over_roads

# %matplotlib inline

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
# # Visualisation

# %% [markdown]
# ## Heatmap to find dense areas

# %%
# %%time

count, x, y, _ = plt.hist2d(
        x=gdf.longitudeE7,
        y=gdf.latitudeE7,
        bins=3000,
        norm=mpl.colors.LogNorm()
    )

# %%
LIMIT = 300
sum(sum(count > LIMIT))


# %%
def select_and_render(ix, iy, ax=None, gdf=gdf):
    selection = gdf[
        (gdf.longitudeE7 > x[ix])
        & (gdf.longitudeE7 < x[ix + 1])
        & (gdf.latitudeE7 > y[iy])
        & (gdf.latitudeE7 < y[iy + 1])
    ]
    show_data_over_roads(selection, ax=ax, repository_root_location=root_location)


# %%
locations = tuple(zip(*np.where(count > LIMIT)))

# %% [markdown]
# ## 1 Example (example 0 is in the middle of nowhere)

# %%
# %%time
select_and_render(*locations[1])

# %% [markdown]
# ## Rest of the examples
# (sqrt_num_figs = 2) demonstrates what this does in 27s  
# (sqrt_num_figs = 6) shows all (30) cases in 10min

# %%
# %%time

sqrt_num_figs = 2

fig, axes = plt.subplots(sqrt_num_figs, sqrt_num_figs, figsize=(5 * sqrt_num_figs, 4 * sqrt_num_figs))

for (fig_num, (ix, iy)) in enumerate(locations[:sqrt_num_figs**2]):
    print(f"start rendering figure {fig_num}")
    %time select_and_render(ix, iy, axes[fig_num // sqrt_num_figs][fig_num % sqrt_num_figs])
    print(f"done rendering figure {fig_num}")

# %% [markdown]
# ## Dense locations on Belgian map

# %%
fig, ax = plt.subplots()

show_data_over_roads(
    transform_to_geo_data(
        pd.DataFrame(
            {
                "longitudeE7": x[[loc[0] for loc in locations]],
                "latitudeE7": y[[loc[1] for loc in locations]],
            }
        )
    ),
    ax=ax,
    repository_root_location=root_location,
)

# %% [markdown]
# ## Coordinates of locations for checking on google maps

# %%
tuple(
    zip(
        y[[loc[1] for loc in locations]] / 10_000_000,
        x[[loc[0] for loc in locations]] / 10_000_000,
    )
)

# %%
