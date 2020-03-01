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

from src.tools.visualising import plot_single_day

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
# # Visualising

# %%
for i in range(1, 7):
    plot_single_day(df, 2018, 7, i)

# %%
