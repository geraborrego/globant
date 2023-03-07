from sqlalchemy import Table,Column
from config.db import meta,engine
from sqlalchemy.sql.sqltypes import Integer, String

employees = Table("employees",meta,
                 Column("id", Integer,primary_key=True),
                 Column("name", String(255)),
                 Column("datetime", String(255)),
                 Column("department_id", Integer),
                 Column("job_id", Integer)
            )

meta.create_all(engine)