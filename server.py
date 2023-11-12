
# from mysqlx import Column
from sqlalchemy import  DateTime, Integer, MetaData, String, create_engine ,MetaData,Table,Column,Integer,String,DateTime
meta=MetaData()
datetime=DateTime

engine=create_engine('sqlite:///sham.db',echo=True)

user =Table(
        'user',meta,
            Column('user_id',Integer(),primary_key=True),
            Column('username',String(15),nullable=False,unique=True),
            Column('email',String(150),nullable=False),
            Column('password',String(12),nullable=False),
            Column('created_on',datetime(),default=DateTime,nullable=False),
            Column('updated_on',datetime(),default=DateTime,onupdate=DateTime,nullable=False)
        )
conn=engine.connect()
# try:
#         conn=engine.connect()
#         print('db.connected')
#         print('connection object is:{}'.format(conn))
# except:
#         print('db not connected')
        # meta.create_all(engine
conn.commit()
conn.close()