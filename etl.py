import os
import kaggle
import pandas as pd
import collections

# I know this is a security risk but I'm not worried about it and this is easier than setting up a config file on every machine
# kaggle_json = '{"username":"ryangrayson","key":"ff71ca5843ee7c2766618b7faee5e6f9"}'

# try:
#     with open(os.path.expanduser('~/.kaggle/kaggle.json'), 'w') as f:
#         f.write(kaggle_json)
# except:
#     print('Could not write kaggle.json')
#     exit(1)

# try:
#     kaggle.api.authenticate()
# except:
#     print('Could not authenticate kaggle api')
#     exit(1)
# dataset = 'kyanyoga/sample-sales-data'
# # fetch data via kaggle api
# try:
#     kaggle.api.dataset_download_files(dataset, path='./data/', unzip=True)
# except:
#     print('Could not fetch sales data from api')
#     exit(1)

# read sales data into df
try:
    sales_df = pd.read_csv('data/sales_data_sample.csv', encoding='latin-1')
except:
    print('Could not read sales_data_sample.csv')
    exit(1)

# read the data into df
try:
    ports_df = pd.read_csv('data/port_data.csv')
except:
    print('Could not read port_data.csv')
    exit(1)


# TODO READ employees data into df with sqlalchemy here

# for each country, keep the port with the maximum vessels, each country should have one port for this process
ports_df = ports_df.sort_values(by=['Country', 'Vessels in Port'], ascending=False)
ports_df = ports_df.drop_duplicates(subset=['Country'], keep='first')

# get unique countries that have ports
countries = set(ports_df['Country'].unique())

# for this process we only care about the sales that are associated with a country that has a port
# remove all rows in sales_df that are not associated with a country that has a port
sales_df = sales_df[sales_df['COUNTRY'].isin(countries)]

# add a column to match with employee ids, of which there are N distinct values
# for security reasons, The employee id can be obtained as follows:
# consider the unique employee ids to be a list of N elements, indexed from 0 to N-1, sorted in ascending order
# Then, employee_id = (order_id * 7) % N
N = 1000

# sales_df['EMPLOYEE_ID'] = employee_ids[(sales_df['ORDERNUMBER'] * 7) % N]






