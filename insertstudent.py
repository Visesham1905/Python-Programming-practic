import select
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,ForeignKey
engine = create_engine('sqlite:///college.db', echo = True)

meta = MetaData()
conn=engine.connect()

students = Table(
   'students', meta, 
   Column('st_id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
   
   
)

conn.execute(students.update(), [
   {'id':15, 'name':'ram ', 'lastname':'bhalke'},
   {'id':16, 'name':'ramakant ', 'lastname':'nagarkar'},
   {'id':17, 'name':'vaishnavi  ', 'lastname':'patil'},
   {'id':18, 'name':'shreenivas  ', 'lastname':'funde'},
   {'id':21, 'name':'pritesh  ' , 'lastname':'sapa'},
])

conn.commit()
conn.close()
