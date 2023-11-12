from sqlalchemy import MetaData, Table, Column,Integer,String, create_engine
engine=create_engine('sqlite:///college.db',echo=True)
meta=MetaData()

students=Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('lastname',String),
)
meta.create_all(engine)

