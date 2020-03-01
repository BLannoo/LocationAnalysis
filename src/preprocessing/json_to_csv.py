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

import json
import pandas as pd

from src.tools.pre_processing import json_to_csv

# %% [markdown]
# # Parameters

# %%
input_file_name = (
    root_location
    + "data/raw/MyGoogleData/"
    + "Takeout/Location History/"
    + "Location History.json"
)
file_name_out = root_location + "data/raw_csv/full.csv"

# %% [markdown]
# # Load data

# %%
# %%time

df = json_to_csv(input_file_name)

# %% [markdown]
# # Save as csv

# %%
df.to_csv(file_name_out, index=False)

# %% [markdown]
# # Test Loading speed

# %%
# %%time

df = pd.read_csv(file_name_out)

# %%
