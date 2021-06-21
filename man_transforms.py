import pandas as pd

# Convert Lists.xlsx to lists.csv
### Change to bash script later.
### Normalize for upload into database.
df = pd.read_excel('datalake/Lists.xlsx')
df.columns = map(str.lower, df.columns)
df.to_csv('data/lists.csv')

# Convert PTC_24_hours to timeseries format.
df = pd.read_csv('datalake/PTC_all_24hours.csv')
df.drop(columns=['date.1', 'year', 'month'], inplace=True)
df = df.melt(id_vars=df.columns[:6], var_name='hour', value_name='vehicle_count')
df['vehicle_count'] = df['vehicle_count'].astype(int)
df['hour'] = df['hour'].str.replace(pat='hour_', repl='')
df['date'] = df['date'].str.replace(pat='T00:00:00Z', repl='')
df['date'] = pd.to_datetime(df['date']+' '+df['hour'])
df.drop(columns='hour', inplace=True)
df = df.set_index('date')
df.to_csv('data/ptc_24_hours_timeseries.csv')
### Once converted, upload file into influx db
