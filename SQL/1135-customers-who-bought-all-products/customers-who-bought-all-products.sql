SELECT customer_id FROM Customer
GROUP BY customer_id HAVING
COUNT(DISTINCT(product_key))=(select count(*) from Product )