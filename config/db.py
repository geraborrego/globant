from sqlalchemy import create_engine,MetaData

#engine=create_engine("mysql+mysqlconnector://root:root@localhost:3306/globant")
engine=create_engine("mysql+pymysql://root:root@localhost:3306/globant")

meta=MetaData()

conn=engine.connect()