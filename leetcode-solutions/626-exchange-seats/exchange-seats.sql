SELECT ROW_NUMBER() OVER(ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)) as id, student
FROM seat