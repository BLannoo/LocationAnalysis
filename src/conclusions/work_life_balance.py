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

import pandas as pd

# %% [markdown]
# # Parameters

# %%
root_location = "../../"

input_file_name = root_location + "data/samples/year_2018.csv"

# %% [markdown]
# # Load data

# %%
# %%time

df = pd.read_csv(input_file_name)

# %% [markdown]
# # Analysis

# %%
min_x_kunlabora = 47_126_000
max_x_kunlabora = 47_140_000
min_y_kunlabora = 508_831_000
max_y_kunlabora = 508_838_000

hours_at_work = (
    df[
        (df.longitudeE7 > min_x_kunlabora)
        & (df.longitudeE7 < max_x_kunlabora)
        & (df.latitudeE7 > min_y_kunlabora)
        & (df.latitudeE7 < max_y_kunlabora)
    ]
    .groupby(["year", "month", "day"])
    .agg({"duration": ["sum"]})
)

hours_at_work.hist(bins=50, figsize=(16, 10))

hours_at_work.describe()

# %%
