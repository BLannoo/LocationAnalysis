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
from src.tools import utils

# %% [markdown]
# # Parameter

# %%
file_name_in = root_location + "data/processed/enriched.csv"

samples = (
    {"year": 2018},
    {"year": 2019},
    {"year": 2020, "month": 1},
    {"year": 2018, "country": "Belgium"},
    {"year": 2018, "month": 12, "country": "Belgium"},
)
output_folder = root_location + "data/samples/"

# %% [markdown]
# # Load data

# %%
# %%time

df = pd.read_csv(file_name_in)

# %% [markdown]
# # Save all requested samples

# %%
# %%time

for sample in samples:
    selection = True
    file_name = ""
    for key, value in sample.items():
        selection = selection & (df[key] == value)
        file_name += "_" + str(key) + "_" + str(value)
    df[selection].to_csv(output_folder + file_name[1:] + ".csv", index=False)

# %%
