The API Service will have the following functions:

JOBS:
/loadhistoricaldatajob : Load historical job data 

/backupjob : Backup the job table in avro file 

/restorejob : Restore the job table in avro file 

/alljob : List all jobs in the job table 

/createjob : Create a new job

/deletejobid/{id} : Delete a specific job 

/jobid/{id} : Find a specific job 

/updatejobid/{id} : Update a specific job 

DEPARTMENT:
/loadhistoricaldatadepartment: Load historical department data 

/backupdepartment: Backup the department table in avro file 

/restoredepartment: Restore the department table in avro file 

/alldepartment: List all department in the job table 

/createdepartment: Create a new department

/deletedepartmentid/{id}: Delete a specific department 

/departmentid/{id}: Find a specific department 

/updatedepartmentid/{id}: Update a specific department 

EMPLOYEE:
/loadhistoricaldataemployee: Load historical employee data 

/backupemployee: Backup the employee table in avro file 

/restoreemployee: Restore the employee table in avro file 

/allemployee: List all employee in the job table 

/createemployee: Create a new employee

/deleteemployeeid/{id}: Delete a specific employee 

/employeeid/{id}: Find a specific employee 

/updateemployeeid/{id}: Update a specific employee 

SQL
exercise1.sql:number of employees hired for each job and department in 2021 divided by quarter. The table must be ordered alphabetically by department and job.

exercise2.sql:List of ids, name and number of employees hired of each department that hired more employees than the mean of employees hired in 2021 for all the departments, ordered by the number of employees hired (descending).

