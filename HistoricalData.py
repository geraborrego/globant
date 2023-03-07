import sqlalchemy as db
from sqlalchemy.types import Integer, Text, String, DateTime
from config.db import conn
import pandas as pd



#engine = db.create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
#connection2 = engine.connect()

#Department
class HistoricalData():
    def loadhistoricaldepartment():
        dfd = pd.read_csv("./IncomeLegacyData/departments.csv",names=['id','department'] , header=None) 
        dfd.to_sql(
            "departments", 
            con = conn,
            if_exists = "replace",
            index=False,
            chunksize=1000 ,
            dtype={
            "id": Integer,
            "department": String(255)
            }
        )
        
    #Jobs
    def loadhistoricaljobs():
        dfj = pd.read_csv("./IncomeLegacyData/jobs.csv",names=['id','job'] , header=None) 
        dfj.to_sql(
            "jobs", 
            con = conn,
            if_exists = "replace",
            index=False,
            chunksize=1000 ,
            dtype={
            "id": Integer,
            "job": String(255)
            }
        )

    #Employee hired_employees
    def loadhistoricalemployee():
        engine = db.create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
        dfe = pd.read_csv("./IncomeLegacyData/hired_employees.csv",names=['id','name','datetime','department_id','job_id'] , header=None) 
        dfe.to_sql( 
            name="employees", 
            con = engine,
            if_exists = "replace",
            index=False,
            chunksize=1000,
            dtype={
                "id": Integer,
                "name": String(255),
                "datetime": String(255),
                "department_id": Integer,
                "job_id": Integer
            }
        )

