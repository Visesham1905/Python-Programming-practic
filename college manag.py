# from pyclbr import Class
from sqlalchemy import  create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Student(Base):    
    __tablename__="student"
    Column('sid',Integer, primary_key=True)
    Column('sname',String)
    Column('lname',String)
    Column('course',String)
    Column('year',CHAR)
    Column('gender',CHAR)
    Column('age',Integer)
    
    def __init__(self,sid,sname,lname,course,year,gender,age):
        self.sid=sid
        self.sname=sname
        self.lname=lname
        self.course=course
        self.year=year
        self.gender=gender
        self.age=age
        
    def __repr__(self):
        return f"({self.sid}) {self.sname} {self.lname} {self.course} {self.year} {self.gender} {self.age}"
    
engine=create_engine("sqlite:///sham.db",echo=True)
Base.metadata.create_all(bind=engine)


Session=sessionmaker(bind=engine)
session=Session()
session.execute(Student.insert(), [
    {1,'sham','vise','BCA','2nd','M',23},
    {9,'narayan','kale','BCA','2nd','M',23},
    {2,'ram','vise','MCA','1nd','M',22},
    {3,'ravi','khairnar','MBA','2nd','M',32},
    {4,'rushi','kamte','BBA','3nd','M',34},
    {5,'manjusha','ukande','MBA','2nd','F',52},
    {6,'akshada','nahe','BCA','3nd','F',23},
    {7,'vaishnavi','vise','MCA','2nd','F',14},
    ])
session.add(Student)
session.commit()


    
    
    

    
