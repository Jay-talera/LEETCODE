# Write your MySQL query statement below
select request_at as Day,round(sum(if(status!='completed',1,0))/count(*),2) 'Cancellation Rate' 
from trips
where (request_at between  '2013-10-01' and '2013-10-03') and client_id not in (select users_id from users where banned='Yes')
and driver_id not in (select users_id from users where banned='Yes')
group by request_at