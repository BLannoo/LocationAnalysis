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

from src.tools.pre_processing import enrich_data

# %% [markdown]
# # Parameters

# %%
input_file_name = root_location + "data/raw_csv/full.csv"

output_file_name = root_location + "data/processed/enriched.csv"

# %% [markdown]
# # Enrich data (and save)

# %%
# %%time

df = pd.read_csv(input_file_name)
df = enrich_data(df)
df.to_csv(output_file_name, index=False)

# %%
