WITH PREVIOUS AS (
    SELECT 
        td.department,
        tj.job,
    	IF(QUARTER(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=1,1,0) AS Q1,
    	IF(QUARTER(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=2,1,0) AS Q2,
    	IF(QUARTER(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=3,1,0) AS Q3,
    	IF(QUARTER(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=4,1,0) AS Q4
    FROM employee te
    INNER JOIN testjob tj ON te.job_id=tj.id
    INNER JOIN testdepartment td ON te.department_id=td.id 
    WHERE YEAR(str_to_date(te.datetime, '%Y-%m-%dT%H:%i:%sZ'))=2021
)
SELECT 
	department,
    job,
    SUM(Q1) AS Q1,
    SUM(Q2) AS Q2,
    SUM(Q3) AS Q3,
    SUM(Q4) AS Q4
FROM PREVIOUS
GROUP BY department,job ASC
ORDER BY department,job;