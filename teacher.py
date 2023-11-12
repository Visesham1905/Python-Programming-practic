from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
engine= create_engine('sqlite:///system.db',echo=True)
meta=MetaData()
conn=engine.connect()
Base=declarative_base()


class Teacher(Base):
    __tablename__='teacher'
    Column('id',Integer,primary_key=True,),
    Column('name',String,unique=True),
    Column('subject',String),
    Column('degree',String),
    Column('experience',String),
    Column('salery',Integer),
    Column('st_id',Integer,ForeignKey('student.id'))
    Student=relationship('student',backref='course')

def __repr__(self):
    return f"<Teacher {self.id} {self.name} {self.subject} {self.degree} {self.experience} {self.salery} {self.st_id}"


conn.execute (Teacher.insert(), [
    {'id':1,'name':'sham_vise','subject':'python','degree':'BCA','experience':'3 year','salery':'650000'},
    {'id':2,'name':'rushi khairnar','subject':'java','degree':'bca','experience':'3 year','salery':'7600'},
    {'id':3,'name':'manjusha ukande','subject':'andriod','degree':'MCA','experience':'3 year','salery':'45333'},
    {'id':4,'name':'manjo khole','subject':'web','degree':'BCA','experience':'3 year','salery':'76754'},
    {'id':5,'name':'yash dhulekar','subject':'react','degree':'BCA','experience':'3 year','salery':'98798'},
    {'id':6,'name':'aayush jain','subject':'angular','degree':'BCA','experience':'3 year','salery':'650000'},
    {'id':7,'name':'kashinath','subject':'html','degree':'BCA','experience':'3 year','salery':'343645'},
    {'id':8,'name':'mukesh agale','subject':'css','degree':'BCA','experience':'3 year','salery':'345356'},
])

Student=Table(Base)
__tablename__='student'
Column('id',Integer,primary_key=true)
Column('name',String)
Column('lname',String)

def __rpre__(self):
    return f"<Student {self.st_id} {self.name} {self.lname}"


conn.commit()
conn.close()