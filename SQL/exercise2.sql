WITH PREVIOUS AS (	
    SELECT 
    	td.id ,
        td.department,
        COUNT('X') AS HIRED
    FROM testemployee te
    INNER JOIN testdepartment td ON te.department_id=td.id 
    WHERE YEAR(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=2021
    GROUP BY td.id , td.department
)
SELECT 
    id ,
    department,
    hired
FROM PREVIOUS
WHERE hired>(SELECT AVG(hired) FROM PREVIOUS)
ORDER BY hired desc;