from numpy import dtype
import pandas as pd
from pandas.core.indexes import category
import matplotlib.pyplot as plt

# Ingest the timeseries csv in pandas dataframe
types = {'code':'category', 'traffic_direction_seq':'category',
    'cardinal_direction_seq':'category',
    'station_key':'category', 'station_id':'category'}
df = pd.read_csv('data/ptc_24_hours_timeseries.csv', index_col=0, parse_dates=True, dtype=types)

# EDA
df_codes = pd.DataFrame(df.groupby(df.index.year)['code'].agg(['nunique', 'count']))
df_codes.plot(kind='bar', secondary_y='count', rot=90)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('year')
ax1.set_ylabel('volume', color=color)
ax1.plot(df_codes.index, df_codes['count'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('counters', color=color)  # we already handled the x-label with ax1
ax2.plot(df_codes.index, df_codes['count'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

10 %% 2

[*range(1,20,2)]  # Kristina's first line of code.