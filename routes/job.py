from fastapi import APIRouter,Response
from config.db import conn
from models.job import jobs
from schemas.job import Job
from starlette.status import HTTP_204_NO_CONTENT
from HistoricalData import HistoricalData
from restoreavros import RestoreData
from backupavros import backupData

job = APIRouter()

@job.get("/loadhistoricaldatajob",tags=["jobs"])
def historicalload_jobs():
    HistoricalData.loadhistoricaljobs()
    return "Load job history data"

@job.get("/backupjob",tags=["jobs"])
def backupdata_jobs():
    backupData.backupjob()
    return "backup job table"

@job.get("/restorejob",tags=["jobs"])
def restore_jobs():
    RestoreData.retorejobs()
    return "Restore job table"

@job.get("/alljob",response_model=list[Job],tags=["jobs"])
def get_jobs():
    return conn.execute(jobs.select()).fetchall()

@job.post("/createjob",tags=["jobs"])
def create_job(job:Job):
    new_job={"id":job.id,"job":job.job}
    result=conn.execute(jobs.insert().values(new_job))
    conn.commit()
    return "New job created"

@job.delete("/deletejobid/{id}",status_code=HTTP_204_NO_CONTENT,tags=["jobs"])
def delete_jobid(id:str):
    conn.execute(jobs.delete().where(jobs.c.id==id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@job.get("/jobid/{id}",response_model=Job,tags=["jobs"])
def get_jobid(id:str):
    return conn.execute(jobs.select().where(jobs.c.id==id)).first()

@job.put("/updatejobid/{id}",response_model=Job,tags=["jobs"])
def update_jobid(id:str,job:Job):
    conn.execute(jobs.update().values(job=job.job
    ).where(jobs.c.id==id))
    conn.commit()
    return conn.execute(jobs.select().where(jobs.c.id==id)).first()


