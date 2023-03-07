import sqlalchemy as db
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd
from fastavro import writer, reader, parse_schema
from config.db import conn
import numpy as np


class RestoreData():
    def retorejobs():
        engine = db.create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
        avro_records = []
        with open('./OutputAvroData/jobs.avro', 'rb') as fo:
            avro_reader = reader(fo)
            for record in avro_reader:
                avro_records.append(record)
        
        df_avro = pd.DataFrame(avro_records)
        df_avro.to_sql(
            "jobs", 
            con = engine,
            if_exists = "replace",
            index=False,
            chunksize=1000 ,
            dtype={
                "id": Integer,
                "job": String(255)
            }
        )

    def retoredepartments():
        engine = db.create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
        avro_records = []
        with open('./OutputAvroData/departments.avro', 'rb') as fo:
            avro_reader = reader(fo)
            for record in avro_reader:
                avro_records.append(record)
        df_avro = pd.DataFrame(avro_records)
        df_avro.to_sql(
            "departments", 
            con = engine,
            if_exists = "replace",
            index=False,
            chunksize=1000 ,
            dtype={
            "id": Integer,
            "department": String(255)
            }
        )

    def retoreemployees():
        engine = db.create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
        avro_records = []
        with open('./OutputAvroData/employees.avro', 'rb') as fo:
            avro_reader = reader(fo)
            for record in avro_reader:
                avro_records.append(record)
        df_avro = pd.DataFrame(avro_records)
        df_avro['job_id'] = df_avro['job_id'].replace({-99:np.nan})
        df_avro['department_id'] = df_avro['department_id'].replace({-99:np.nan})
        df_avro['id'] = df_avro['id'].replace({-99:np.nan})
        df_avro.to_sql( 
            "employees", 
            con = engine,
            if_exists = "replace",
            index=False,
            chunksize=1000 ,
            dtype={
            "id": Integer,
            "name": String(255),
            "datetime": String(255),
            "department_id": Integer,
            "job_id": Integer,
            }
        )
