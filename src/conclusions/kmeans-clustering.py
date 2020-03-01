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

from src.tools.pre_processing import read_csv_as_geopandas, transform_to_geo_data
from src.tools.visualising import show_data_over_roads

# %matplotlib inline

# %% [markdown]
# # Kmeans clustering of just the latitudeE7 and longitudeE7
#
# Works in first approximation,
# but at higher number of clusters centroids are more likely to be send to the middle of long trips then to split up two close to each other important locations.

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
# # Analyse

# %%
gdf.head()

# %%
show_data_over_roads(gdf, repository_root_location=root_location)

# %%
len(gdf)

# %% [markdown]
# # Kmeans clustering

# %%
from sklearn.cluster import KMeans
from sklearn import preprocessing

# %%
samples = gdf[["latitudeE7", "longitudeE7"]].copy()

scaler = preprocessing.MinMaxScaler()
samples = scaler.fit_transform(samples)
k_mean = KMeans(n_clusters=20)
k_mean.fit(samples)

# %%
show_data_over_roads(
    transform_to_geo_data(
        pd.DataFrame(
            scaler.inverse_transform(k_mean.cluster_centers_),
            columns=["latitudeE7", "longitudeE7"],
        )
    ),
    repository_root_location=root_location,
)

# %%
