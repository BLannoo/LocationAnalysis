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

import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

from src.tools.utils import approx_abs_log
from src.tools.movement import movement

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
# # Analysis

# %%
grouped = df.groupby(["year", "month", "day", "hour"]).agg(
    {
        "latitudeE7": ["median", "var", "count"],
        "longitudeE7": ["median", "var", "count"],
    }
)

approx_abs_log(grouped.latitudeE7["var"]).hist(bins=100, figsize=(16, 10))

# %%
approx_abs_log(df.movement).rolling(5, center=True).mean().hist(
    bins=100, figsize=(16, 10)
)

# %%
df.plot(
    x="time_of_day",
    y="duration",
    alpha=0.2,
    kind="scatter",
    logy=True,
    figsize=(16, 10),
)

# %%
df.hist(column=["time_of_day"], bins=100)

# %%
