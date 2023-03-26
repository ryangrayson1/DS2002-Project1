# get daat from data/Port_Data.csv

import pandas as pd

ports_df = pd.read_csv('data/Port_Data.csv')


# get list of unique countries

countries = set(ports_df['Country'].unique())



# unique countries from data/sales_data_sample.csv
dfs = pd.read_csv('data/sales_data_sample.csv')
countries2 = dfs['COUNTRY'].unique()
print(countries2)

# countries in salses data but not in port data)
print(set(countries2) - set(countries))