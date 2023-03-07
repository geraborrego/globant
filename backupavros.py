import pandas as pd
from fastavro import writer, reader, parse_schema
from config.db import conn
from models.job import jobs
from models.employee import employees
from models.department import departments


class backupData():
    def backupdepartment():
        df = pd.DataFrame(conn.execute(departments.select()).fetchall())
        schema = {
            'doc': 'department',
            'name': 'department',
            'namespace': 'department',
            'type': 'record',
            'fields': [
                {'name': 'id', 'type': 'int'},
                {'name': 'department', 'type': 'string'}
            ]
        }
        parsed_schema = parse_schema(schema)
        records = df.to_dict('records')

        with open('./OutputAvroData/departments.avro', 'wb') as out:
            writer(out, parsed_schema, records)

    def backupjob():
        df = pd.DataFrame(conn.execute(jobs.select()).fetchall())
        schema = {
            'doc': 'jobs',
            'name': 'jobs',
            'namespace': 'jobs',
            'type': 'record',
            'fields': [
                {'name': 'id', 'type': 'int'},
                {'name': 'job', 'type': 'string'}
            ]
        }
        parsed_schema = parse_schema(schema)
        records = df.to_dict('records')

        with open('./OutputAvroData/jobs.avro', 'wb') as out:
            writer(out, parsed_schema, records)

    def backupemployee():
        df = pd.DataFrame(conn.execute(employees.select()).fetchall())
        print(df.head())
        #df = df.fillna("")
        #df[['name','datetime']].fillna('')
        #df[['id','department_id','job_id']].fillna(0)
        #df2 = df[['id','department_id','job_id' ]] = df[['id','department_id','job_id']].fillna(0)

        df['job_id'].fillna(-99, inplace = True)
        df['department_id'].fillna(-99, inplace = True)
        df['id'].fillna(-99, inplace = True)
        df['name'].fillna('', inplace = True)
        df['datetime'].fillna('', inplace = True)
        print(df.head())

        schema = {
            'doc': 'employee',
            'name': 'employee',
            'namespace': 'employee',
            'type': 'record',
            'fields': [
                {'name': 'id', 'type': 'int'},
                {'name': 'name', 'type': 'string'},
                {'name': 'datetime', 'type': 'string'},
                {'name': 'department_id', 'type': 'int'},
                {'name': 'job_id', 'type': 'int'}
            ]
        }
        parsed_schema = parse_schema(schema)
        records = df.to_dict('records')
        with open('./OutputAvroData/employees.avro', 'wb') as out:
            writer(out, parsed_schema, records)
   

#sql_query = pd.read_sql_query("SELECT id,department FROM departments", conn)

#df = pd.read_sql_query('departments', conn)

#df = pd.DataFrame(sql_query,names=['id','department'])

#df =pd.read_sql('SELECT id,department FROM departments', conn)

#df = pd.DataFrame(conn.execute(jobs.select()).fetchall())

#ddf = pd.DataFrame(conn.execute(departments.select()).fetchall())

#dprint(df.head())

#df = pd.DataFrame(sql_query, columns = ['product_id', 'product_name', 'price'])
#print (df)

#df = pd.read_csv("./IncomeLegacyData/jobs.csv",names=['id','job'] , header=None)
#print(df.head())
"""

schema = {
    'doc': 'department',
    'name': 'department',
    'namespace': 'department',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'department', 'type': 'string'}
    ]
}
parsed_schema = parse_schema(schema)
records = df.to_dict('records')

with open('./OutputAvroData/department.avro', 'wb') as out:
    writer(out, parsed_schema, records)



# 1. List to store the records
avro_records = []

# 2. Read the Avro file
with open('./OutputAvroData/prices.avro', 'rb') as fo:
    avro_reader = reader(fo)
    for record in avro_reader:
        avro_records.append(record)
        
# 3. Convert to pd.DataFrame
df_avro = pd.DataFrame(avro_records)

# Print the first couple of rows
print('result')
print(df_avro.head())
"""