select person_name from
(
select *,sum(weight) over(order by turn)as cum_sum
from queue 
)as a
where cum_sum<=1000
order by cum_sum desc limit 1