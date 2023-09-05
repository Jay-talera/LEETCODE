SELECT
    Products.product_name,
    SUM(Orders.unit) AS unit
FROM
    Products
INNER JOIN
    Orders
ON
    Products.product_id = Orders.product_id
WHERE
    left(order_date,7)='2020-02'
GROUP BY
    Products.product_id
HAVING
    unit >= 100