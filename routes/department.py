from fastapi import APIRouter,Response
from config.db import conn
from models.department import departments
from schemas.department import Department
from starlette.status import HTTP_204_NO_CONTENT
from HistoricalData import HistoricalData
from restoreavros import RestoreData
from backupavros import backupData

department = APIRouter()

@department.get("/loadhistoricaldatadepartment",tags=["departments"])
def load_department():
    HistoricalData.loadhistoricaldepartment()
    return "Load job history data"

@department.get("/backupdepartment",tags=["jobs"])
def backupdata_department():
    backupData.backupdepartment()
    return "backup department table"

@department.get("/restoredepartment",tags=["jobs"])
def restore_departments():
    RestoreData.retoredepartments()
    return "Restore department table"

@department.get("/alldepartment",response_model=list[Department],tags=["departments"])
def get_departments():
    return conn.execute(departments.select()).fetchall()

@department.post("/createdepartment",tags=["departments"])
def create_department(department:Department):
    new_department={"id":department.id,"department":department.department}
    result=conn.execute(departments.insert().values(new_department))
    conn.commit()
    return "New department created"

@department.delete("/deletedepartmentid/{id}",status_code=HTTP_204_NO_CONTENT,tags=["departments"])
def delete_departmentid(id:str):
    conn.execute(departments.delete().where(departments.c.id==id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@department.get("/departmentid/{id}",response_model=Department,tags=["departments"])
def get_departmentid(id:str):
    return conn.execute(departments.select().where(departments.c.id==id)).first()

@department.put("/updatedepartmentid/{id}",response_model=Department,tags=["departments"])
def update_departmentid(id:str,department:Department):
    conn.execute(departments.update().values(department=department.department
    ).where(departments.c.id==id))
    conn.commit()
    return conn.execute(departments.select().where(departments.c.id==id)).first()
