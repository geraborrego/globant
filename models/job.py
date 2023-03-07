from sqlalchemy import Table,Column
from config.db import meta,engine
from sqlalchemy.sql.sqltypes import Integer, String

jobs= Table("jobs",meta,
                 Column("id", Integer,primary_key=True),
                 Column("job", String(255))
            )

meta.create_all(engine)