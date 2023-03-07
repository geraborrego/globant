from fastapi import APIRouter,Response
from config.db import conn
from models.employee import employees
from schemas.employee import Employee
from starlette.status import HTTP_204_NO_CONTENT
from HistoricalData import HistoricalData
from restoreavros import RestoreData
from backupavros import backupData

employee = APIRouter()


@employee.get("/loadhistoricaldataemployee",tags=["employees"])
def loadhistorical_employees():
    HistoricalData.loadhistoricalemployee() 
    return "Load employee history data"

@employee.get("/backupemployee",tags=["jobs"])
def backupdata_employee():
    backupData.backupemployee()
    return "backup employee table"

@employee.get("/restoreemployee",tags=["jobs"])
def restore_employees():
    RestoreData.retoreemployees()
    return "Restore employee table"

@employee.get("/allemployee",response_model=list[Employee],tags=["employees"])
def get_employee():
    return conn.execute(employees.select()).fetchall()

@employee.post("/createemployee",tags=["employees"])
def create_employee(employee:Employee):
    new_employee={"id":employee.id,"name":employee.name,"datetime":employee.datetime,"department_id":employee.department_id,"job_id":employee.job_id}
    result=conn.execute(employees.insert().values(new_employee))
    conn.commit()
    return "New employee created"

@employee.delete("/deleteemployeeid/{id}",status_code=HTTP_204_NO_CONTENT,tags=["employees"])
def delete_employeeid(id:str):
    conn.execute(employees.delete().where(employees.c.id==id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@employee.get("/employeeid/{id}",response_model=Employee,tags=["employees"])
def get_employeeid(id:str):
    return conn.execute(employees.select().where(employees.c.id==id)).first()

@employee.put("/updateemployeeid/{id}",response_model=Employee,tags=["employees"])
def update_employeeid(id:str,employee:Employee):
    conn.execute(employees.update().values(
                    name=employee.name,
                    datetime=employee.datetime,
                    department_id=employee.department_id,
                    job_id=employee.job_id
    ).where(employees.c.id==id))
    conn.commit()
    return conn.execute(employees.select().where(employees.c.id==id)).first()

