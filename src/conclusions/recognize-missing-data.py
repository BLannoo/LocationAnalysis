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

import matplotlib.pyplot as plt
import pandas as pd

# %matplotlib inline

# %% [markdown]
# # Summary (TL;DR)
# * duration > 3h are very rare (19 cases)
# * duration > 2h are rare (82 cases)
# * duration > 6min mostly during the night (and are mathematically the outliers)

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
# # Analysis: What duration's are outliers?
# * fig1: somwhere between 2h and 4h
# * fig2: mathematically alot of outliers
# * fig3: from closer cut off seems 3h
# * fig4: mathematically outliers around 0.1h == 6min

# %%
plt.figure(figsize=(10, 8))

plt.subplot(221)
df.duration.hist(bins=300)
plt.yscale("log")

plt.subplot(222)
df.boxplot(column="duration")

plt.subplot(223)
df[df.duration < 4].duration.hist(bins=50)
plt.yscale("log")

plt.subplot(224)
df.boxplot(column="duration", showfliers=False)

# %%
for threshold in (4, 3, 2, 0.1):
    outliers_count = len(df[df.duration > threshold])
    print(f"{outliers_count:6} outliers found for threshold {threshold}")

# %% [markdown]
# # When (time_of_day) do the outliers occur?

# %%
plt.figure(figsize=(10, 8))

plt.subplot(221)
df.time_of_day.hist(bins=96)
plt.title("All data (mostly during the day)")

plt.subplot(222)
df[df.duration > 2].time_of_day.hist(bins=24)
plt.title("Visual outliers (2h)")

plt.subplot(223)
df[df.duration > 0.1].time_of_day.hist(bins=96)
plt.title("Mathematical outliers (0.1h)")

plt.subplot(224)
df[df.duration > 15 / 60].time_of_day.hist(bins=96)
plt.title("Duration > 15 min (mostly during the night)")

# %%
