select customer_number from orders 
group by customer_number
having count(customer_number)=(select count(customer_number)as cnt from orders group by customer_number order by cnt desc limit 1)