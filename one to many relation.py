from sqlalchemy import Select,create_engine,Integer,String,Column,CHAR,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker

Base=declarative_base()

class Student(Base):
    __tablename__="student"
    sid=Column('sid',Integer,primary_key=True)
    fname=Column('fname',String)
    lname=Column('lname',String)
    age=Column('age',Integer)
    gender=Column('gender',CHAR)
    
    
    def __init__(self,sid,fname,lname,age,gender):
        self.sid=sid
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
        
    def __repr__(self):
        return f"({self.sid}) {self.fname} {self.lname} {self.age} ,{self.gender}"


class Teacher(Base):
    __tablename__='teacher'
    T_id=Column(Integer,primary_key=True)
    name=Column(String)
    subject=Column(String)
    salery=Column(Integer)
    # sub_code=Column(ForeignKey('student.sid'))
    
    def __init__(self,T_id,name,subject,salery):
        self.T_id=T_id
        self.name=name
        self.subject=subject
        self.salery=salery
        # self.sub_code=sub_code
        
    def __repr__(self):
        return f"({self.T_id}) {self.name} {self.subject} {self.salery}"

engine=create_engine("sqlite:///instuite.db",echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()

student=Student(25,"vishal","more",28,"M")
session.add(student)
session.commit()

s1=Student(1,"sham","vise",23,'M')
s2=Student(2,"ram","vise",30,'M')
s3=Student(3,"ajay","vise",25,'M')
s4=Student(4,"vaishnavi","vise",19,'F')
s5=Student(5,"manjusha","ukande",23,'F')
s6=Student(6,"rushikesh","khairnar",22,'M')
s7=Student(7,"yash","lakkad",21,'M')
s8=Student(8,"aarti","navale",22,'F')
s9=Student(9,"shrutika","kadam",24,'F')
s10=Student(10,"aayush","jain",22,'M')
s11=Student(11,"kashinath","kanadi",25,'M')
s12=Student(12,"rajkumar","sharma",35,'M')
session.add(s1)
session.add(s2)
session.add(s3)
session.add(s4)
session.add(s5)
session.add(s6)
session.add(s7)
session.add(s8)
session.add(s9)
session.add(s10)
session.add(s11)
session.add(s12)
session.commit()



t1=Teacher(11,"atharva","android",34000)
t2=Teacher(12,"rajan","Python",54000)
t3=Teacher(13,"narayan","java",65557)
t4=Teacher(14,"kiran","android",84743)
t5=Teacher(15,"rutuja","nodejs",565543)
t6=Teacher(16,"samir","react",77672)
t7=Teacher(17,"navnath","Anaconda",65654)
t8=Teacher(18,"anand","Python",893839)
t9=Teacher(19,"harish","JQUERY",65465)
t10=Teacher(20,"pritesh","JS",32313)
t11=Teacher(21,"avdhut","CSS",23322)
t12=Teacher(22,"kisan","HTML",45532)
t13=Teacher(23,"sharma","Java",98562)
t14=Teacher(24,"varma","C++",78765)
t15=Teacher(25,"arjun","C",87476)
session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.add(t6)
session.add(t7)
session.add(t8)
session.add(t9)
session.add(t10)
session.add(t11)
session.add(t12)
session.add(t13)
session.add(t14)
session.add(t15)
session.commit()



