# Write your MySQL query statement below
select distinct email as Email from person
group by email
having count(email)>1