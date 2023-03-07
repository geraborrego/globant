from sqlalchemy import Table,Column
from config.db import meta,engine
from sqlalchemy.sql.sqltypes import Integer, String

departments= Table("departments",meta,
                 Column("id", Integer,primary_key=True),
                 Column("department", String(255))
            )

meta.create_all(engine)
