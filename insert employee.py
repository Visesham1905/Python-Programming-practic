from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# from employee import Employee
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()
conn = engine.connect()

employee = Table(
   'employee', meta, 
   Column('eid', Integer, primary_key = True), 
   Column('name', String), 
   Column('lname', String), 
   Column('age', Integer),
   Column('salery',Integer)
)

conn.execute(employee.insert(), [
   {'eid':1, 'name':'sham ', 'lname':'vise','age':'26','salery':'35000'},
   {'eid':4, 'name':'ram ','lname':'navse','age':'24','salery':'55000'},
   {'eid':3, 'name':'manju ','lname':'ukande','age':'25','salery':'76000'},
   {'eid':5, 'name':'rushi ','lname':'khairnar','age':'30','salery':'76800'},
   {'eid':2, 'name':'vishal ','lname':'more','age':'32','salery':'36000'},
   {'eid':7, 'name':'ramakant ','lname':'godbole','age':'26','salery':'35000'},
   {'eid':8, 'name':'anthuni ','lname':'more','age':'24','salery':'55000'},
   {'eid':9, 'name':'amar ','lname':'godse','age':'25','salery':'76000'},
   {'eid':11, 'name':'akbae ','lname':'vaje','age':'30','salery':'76800'},
   {'eid':15, 'name':'nandini ','lname':'navle','age':'32','salery':'36000'},
])
conn.commit()
conn.close()
