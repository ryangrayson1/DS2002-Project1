use wahoo_nation_vehicles;

-- query 1: What is the average quantity per order of vehicles in each country?
SELECT AVG(quantity_ordered) AS "avg_qty", country AS "Country"
FROM sales
GROUP BY country;

-- query 2: what is the total number of vehicles sold in each country?
SELECT country, SUM(quantity_ordered) 
FROM sales GROUP BY country 
ORDER BY SUM(quantity_ordered) DESC;

-- run this before the next one
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

-- query 3: who were the top 3 the most productive employees, in terms of their sales per cost (productivity_score = quantity sold to salary ratio)?
SELECT e.emp_no, e.first_name, e.last_name, SUM(s.quantity_ordered), e.salary, SUM(s.quantity_ordered) / e.salary AS "productivity_score"
FROM sales s NATURAL JOIN employees e 
GROUP BY e.emp_no, e.first_name, e.last_name
ORDER BY SUM(s.quantity_ordered) / e.salary DESC
LIMIT 3;

-- query 4: which port had the maximum total sales quantity?
SELECT p.port_name, SUM(s.quantity_ordered) AS "total_sales_quantity"
FROM sales s NATURAL JOIN ports p
GROUP BY p.port_name
ORDER BY SUM(s.quantity_ordered) DESC
LIMIT 1;

-- query 5: when was the first sale, and which employee made the sale?
SELECT MIN(full_date), e.first_name, e.last_name
FROM sales s NATURAL JOIN sale_date_dim d NATURAL JOIN employees e
ORDER BY full_date ASC
LIMIT 1;

-- query 6: what was the maximum total price of an order (price_each * quantity_ordered)?
SELECT MAX(price_each * quantity_ordered) AS "max_total_price"
FROM sales;




