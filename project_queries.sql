use wahoo_nation_vehicles;

SELECT AVG(quantity_ordered) AS "qty", country AS "Country"
FROM sales GROUP BY country;

SELECT country, SUM(quantity_ordered) FROM sales GROUP BY country ORDER BY SUM(quantity_ordered) DESC;

SELECT e.emp_no, e.first_name, e.last_name, SUM(s.quantity_ordered), e.salary, SUM(s.quantity_ordered) / e.salary AS "throughput"
FROM sales s NATURAL JOIN employees e 
GROUP BY e.emp_no, e.first_name, e.last_name
ORDER BY SUM(s.quantity_ordered) / e.salary 
DESC LIMIT 1;





