import pandas as pd

# Convert Lists.xlsx to lists.csv
### Change to bash script later.
### Normalize for upload into database.
df = pd.read_excel('datalake/Lists.xlsx')
df.columns = map(str.lower, df.columns)
df.to_csv('data/lists.csv')
