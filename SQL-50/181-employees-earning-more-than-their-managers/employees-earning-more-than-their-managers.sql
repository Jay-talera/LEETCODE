# Write your MySQL query statement below
select e1.name as employee from employee e1 where e1.salary > (select salary from employee e2 where e2.id=e1.managerid)