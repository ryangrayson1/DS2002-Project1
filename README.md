# DS 2002 - Project 1
## *Team members: Ryan, Lexi & Caitlin*

### Data Sources 
- [Employees Sample Database](https://dev.mysql.com/doc/employee/en/) from MySQL
- [Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data) fetched via Kaggle API
- [Shipping Ports Around the World](https://www.kaggle.com/datasets/sanjeetsinghnaik/ship-ports) downloaded CSV from Kaggle

### Deliverable 1 - Design a dimensional data mart that represents a simple business process of your choosing
Our team used the Employees Sample Database, along with Sample Sales Data & Shipping Ports Around the World, to design a dimensional data mart that tracks business operations. The fact table 'sales', along with dimension tables 'employees' and 'ports' are present in our design of the data mart. Overall, this reflects interaction between retailers & customers in order for a company to make informed decisions about its commercial sales process.

Here is an image of our schema. Notice that the employee table is linked to the sales table via the 'emp_no' column, and the ports table is linked to the sales table via the 'country' column, which is a unique primary key in the ports table.

We also created a date dimension table to have more detailed date information for each sale. This table is linked to the sales table by a date key column, which is a unique primary key in the date dimension table.

<img width="417" alt="Screen Shot 2023-03-26 at 6 15 38 PM" src="https://user-images.githubusercontent.com/123029506/227807998-bb5ea286-6711-4212-868f-abd35eb2280e.png">

### Deliverable 2 - Develop an ETL pipeline that extracts, transforms, and loads data into your data mart
Here's some notes on our process for the ETL pipeline:
- Extracted Employees Sample Database from MySQL, using the tables 'employees' and 'salaries', and joined them to optimize future queries
- Retrieved Sample Sales Data & Shipping Ports Around the World to eventually be converted into the SQL database tables 'sales' and 'ports'
- Added a column 'emp_no' (details commented in etl.py) to the sales dataframe to link each sale to an employee.
- Provided try..catch blocks and error messages to ensure functional API calls and data loading
- More specific details commented in etl.py
*Note: before running etl.py, check the comments at the top of the file for setup instructions*
*Note: After running etl.py, run create_sale_date_dim.sql and integrate_sale_date_dim.sql to create the date dimension table that links to sales.

### Deliverable 3 - Author one or more SQL queries (SELECT statements) to demonstrate proper functionality
- See project_queries.sql
