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

import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from src.tools.pre_processing import read_csv_as_geopandas
from src.tools.visualising import show_data_over_roads

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
len(gdf)

# %%
X = list(zip(gdf.latitudeE7, gdf.longitudeE7, gdf.timestampMs))
X = StandardScaler().fit_transform(X)

# %%
# %%time

db = DBSCAN(eps=0.01, min_samples=100).fit(X)

# %%
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

# %%
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()

# %%
gdf["DBSCAN"] = db.labels_

# %%
gdf["DBSCAN"].value_counts()

# %%
# %%time

sqrt_num_figs = 2

fig, axes = plt.subplots(sqrt_num_figs, sqrt_num_figs, figsize=(5 * sqrt_num_figs, 4 * sqrt_num_figs))

for cluster in range(sqrt_num_figs**2):
    print(f"start rendering cluster {cluster}")
    selection = gdf[gdf["DBSCAN"] == cluster]
    %time show_data_over_roads(selection, ax=axes[cluster // sqrt_num_figs][cluster % sqrt_num_figs])
    print(f"done rendering cluster {cluster}")

# %%
