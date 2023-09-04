select * , 
(case
when
x+y>z and y+z>x and x+z>y
THEN 'Yes'
ELSE "No"
end) as triangle
from Triangle