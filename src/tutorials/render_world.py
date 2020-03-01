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
import geopandas as gpd

# %matplotlib inline

# %%
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(cmap='Set3', figsize=(10, 6))

# %%
