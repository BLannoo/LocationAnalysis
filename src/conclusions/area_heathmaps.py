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

from src.tools.visualising import show_data_density

# %matplotlib inline

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/samples/year_2018.csv"

# %% [markdown]
# # Load data

# %%
# %%time

df = pd.read_csv(input_file_name)

# %% [markdown]
# # Visualisations

# %% [markdown]
# ## Full data

# %%
# %%time

show_data_density(df, "Full data")

# %% [markdown]
# ## Georgia

# %%
# %%time

show_data_density(df, "Georgia", 410_000_000, 470_000_000, 410_000_000, 430_000_000)
show_data_density(df, "Tbilisi", 447_200_000, 448_800_000, 410_000_000, 418_500_000)
show_data_density(df, "Tbilisi core", 447_400_000, 448_200_000, 410_000_000, 417_400_000)
show_data_density(df, "Lili's", 447_600_000, 447_850_000, 417_080_000, 417_200_000)

# %% [markdown]
# ## Europe

# %%
# %%time

show_data_density(df, "Europe", 10_000_000, 400_000_000, 400_000_000, 700_000_000)

# %% [markdown]
# ## Belgium
# Remark: roads_data_overlay.ipynb does something similar

# %%
# %%time

show_data_density(df, "Belgium", 10_000_000, 70_000_000, 505_000_000, 515_000_000)
show_data_density(df, "Brabant", 42_000_000, 49_000_000, 507_000_000, 510_000_000)
show_data_density(df, "Brussel", 42_750_000, 45_000_000, 508_000_000, 509_250_000)
show_data_density(df, "Leuven", 46_700_000, 47_400_000, 508_400_000, 509_000_000)
show_data_density(df, "Leuven centrum", 46_800_000, 47_200_000, 508_605_000, 508_900_000)
show_data_density(df, "Bankstraat", 46_870_000, 46_940_000, 508_700_000, 508_800_000)
show_data_density(df, "Alf. Delaunois.", 47_100_000, 47_200_000, 508_700_000, 508_750_000)
show_data_density(df, "Kunlabora", 47_126_000, 47_140_000, 508_831_000, 508_838_000)

# %%
