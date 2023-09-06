select visited_on,
(select sum(amount) from customer
where visited_on Between DATE_SUB(c.visited_on,INTERVAL 6 DAY) and c.visited_on 
) as amount,
(
  round((select sum(amount)/7 from customer
where visited_on Between DATE_SUB(c.visited_on,INTERVAL 6 DAY) and c.visited_on 
),2)
)as average_amount
from customer c where c.visited_on>=(select DATE_ADD(min(visited_on),INTERVAL 6 DAY) from customer)
group by visited_on
order by visited_on