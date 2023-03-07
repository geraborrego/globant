from fastapi import FastAPI
from routes.department import department
from routes.job import job
from routes.employee import employee

app=FastAPI()


app.include_router(job)
app.include_router(department)
app.include_router(employee)