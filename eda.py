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
df.groupby(df.index.year)['code'].nunique()

plt.plot()
