WITH main AS (
SELECT *, RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rnk
FROM products
WHERE change_date <= '2019-08-16'
)

, dprod AS (
SELECT DISTINCT 
 product_id
FROM products
)

SELECT 
 d.product_id
 , COALESCE(m.new_price, 10) AS price
FROM dprod AS d
LEFT JOIN main AS m
  ON d.product_id = m.product_id
  AND m.rnk = 1