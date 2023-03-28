import kaggle
import pandas as pd
import pymysql
import sqlalchemy

'''
Setup steps to use this ETL processor:

1. you must have a kaggle.json file in /.kaggle/kaggle.json your home directory
the following line is the exact content needed for the file (file also provided):
{"username":"ryangrayson","key":"ff71ca5843ee7c2766618b7faee5e6f9"}

2. you must also have a mysql database connection set up at localhost with the following credentials:
(or you can change the credentials in the code below to use a different setup)
host: localhost
user: ds2002
password: UVA!1819

3. you must have a database named 'employees' loaded locally which can be setup at the following link:
https://github.com/datacharmer/test_db

4. pip install all imported packages, above

'''

try:
    kaggle.api.authenticate()
except:
    print('Could not authenticate kaggle api')
    exit(1)
dataset = 'kyanyoga/sample-sales-data'
# fetch sales data via kaggle api
try:
    kaggle.api.dataset_download_files(dataset, path='./data/', unzip=True)
except:
    print('Could not fetch sales data from api')
    exit(1)

# read sales data into df
try:
    sales_df = pd.read_csv('data/sales_data_sample.csv', encoding='latin-1')
except:
    print('Could not read sales_data_sample.csv')
    exit(1)

# read ports data into df
try:
    ports_df = pd.read_csv('data/port_data.csv')
except:
    print('Could not read port_data.csv')
    exit(1)

# read employees data from db into df
host, user, password, database = 'localhost', 'ds2002', 'UVA!1819', 'employees'
try:
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
except:
    print("DB read connection failed")
    exit(1)


# here we select from employees, and natural join with salaries to add the salary as a column
# this will be more efficient because future queries will not need to join with salaries
query = "SELECT emp_no, birth_date, first_name, last_name, gender, hire_date, salary FROM employees NATURAL JOIN salaries ORDER BY salary DESC LIMIT 1000"
try:
    employees_df = pd.read_sql(query, conn)
except:
    print("Could not read employees data")
    exit(1)

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

# get list of unique employee ids
employee_ids = sorted(list(employees_df['emp_no']))

assert(len(employee_ids) == N, "Error, number of employee ids expected to be " + str(N))

sales_df['EMPLOYEE_ID'] = sales_df['ORDERNUMBER'].apply(lambda x: employee_ids[(x * 7) % N])

# trim unneeded columns to prep for sql insertion
sales_df = sales_df[['ORDERNUMBER', 'QUANTITYORDERED', 'SALES', 'ORDERDATE', 'COUNTRY', 'EMPLOYEE_ID']]
ports_df = ports_df[['Country', 'Vessels in Port', 'Port Name', 'Area Global']]

# rename to lowercase with underscores format
sales_df.columns = ['order_no', 'quantity_ordered', 'sale_type', 'order_date', 'country', 'emp_no']
ports_df.columns = ['country', 'vessels', 'port_name', 'area_global']


# write these tables to sql db
def insert_sqlalchemy_dataframe(user_id, pwd, host_name, db_name, df, table_name):
    conn_str = f"mysql+pymysql://{user_id}:{pwd}@{host_name}/{db_name}"
    sqlEngine = sqlalchemy.create_engine(conn_str, pool_recycle=3600)
    connection = sqlEngine.connect()
    df.to_sql(table_name, con=connection, if_exists='replace') #, index_label='product_id');  'append'
    connection.close()


db = "wahoo_nation_vehicles"

# create new db called wahoo_nation_vehicles
try:
    # check if database exists, create if it does not
    conn = pymysql.connect(host=host, user=user, password=password)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + db)
    conn.close()

except:
    print("Could not create new database")
    exit(1)

insert_sqlalchemy_dataframe(user, password, host, db, employees_df, 'employees')
insert_sqlalchemy_dataframe(user, password, host, db, sales_df, 'sales')
insert_sqlalchemy_dataframe(user, password, host, db, ports_df, 'ports')
