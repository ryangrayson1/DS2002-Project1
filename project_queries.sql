use wahoo_nation_vehicles;

-- query 1: What is the average quantity per order of vehicles in each country?
SELECT AVG(quantity_ordered) AS "avg_qty", country AS "Country"
FROM sales
GROUP BY country;

-- query 2: what is the total number of vehicles sold in each country?
SELECT country, SUM(quantity_ordered) 
FROM sales GROUP BY country 
ORDER BY SUM(quantity_ordered) DESC;

-- query 3: who were the top 3 the most productive employees, in terms of their sales per cost (productivity_score = quantity sold to salary ratio)?
SELECT e.emp_no, e.first_name, e.last_name, SUM(s.quantity_ordered), e.salary, SUM(s.quantity_ordered) / e.salary AS "productivity_score"
FROM sales s NATURAL JOIN employees e 
GROUP BY e.emp_no, e.first_name, e.last_name
ORDER BY SUM(s.quantity_ordered) / e.salary DESC
LIMIT 3;

-- query 4: when was the first sale, and which employee made the sale?
SELECT sale_date AS "first_sale_date", e.first_name, e.last_name
FROM sales s NATURAL JOIN employees e
ORDER BY sale_date ASC
LIMIT 1;





