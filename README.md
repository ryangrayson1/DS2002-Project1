# DS 2002 - Project 1
## *Team members: Ryan, Lexi & Caitlin*

### Data Sources 
- [Employees Sample Database](https://dev.mysql.com/doc/employee/en/) from MySQL
- [Sample Sales Data](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data) from Kaggle pulled using API
- [Shipping Ports Around the World](https://www.kaggle.com/datasets/sanjeetsinghnaik/ship-ports) from Kaggle using .csv format

### Deliverable 1 - Design a dimensional data mart that represents a simple business process of your choosing
Our team used the Employees Sample Database, along with Sample Sales Data & Shipping Ports Around the World, to design a dimensional data mart that reflects business operations procedures. The fact table 'sales', along with dimension tables 'employees' and ports' are present in our design of the data mart. Overall, this reflects interaction between retailers & customers in order for a company to make informed decisions about its commercial shipping process.

### Deliverable 2 - Develop an ETL pipeline that extracts, transforms, and loads data into your data mart
Here's some notes on our process for the ETL pipeline:
- Extracted Employees Sample Database from MySQL, using only the database table 'employees' 
- Retrieved Sample Sales Data & Shipping Ports Around the World to convert into the SQL database tables 'sales' and 'ports'
- Modified column 'order_no' from sales table to link with 'emp_no' from employees table 
- *Provided error messages to (STILL NEED TO ADD)*

Here is an image of our schema: 

<img width="478" alt="Screen Shot 2023-03-26 at 5 31 35 PM" src="https://user-images.githubusercontent.com/123029506/227805860-bc5cb17a-9629-41dc-980a-771bc65f7fe7.png">



### Deliverable 3 - Author one or more SQL queries (SELECT statements) to demonstrate proper functionality

- See SQL File
