from sqlalchemy import Select, create_engine,ForeignKey,String,Integer,Column,CHAR
from sqlalchemy.orm import declarative_base,sessionmaker

Base=declarative_base()
class Person(Base):
    __tablename__="people"
    ssn=Column('ssn',Integer,primary_key=True)
    firstname=Column('firstname',String)
    lastname=Column('lastname',String)
    gender=Column('gender',CHAR)
    age=Column('age',Integer)
    
    def __init__(self,ssn,firstname,lastname,gender,age):
        self.ssn=ssn
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age
        
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} {self.gender} ,{self.age}"
    
    
class Thing(Base):
    __tablename__="things"
    tid=Column("tid",Integer,primary_key=True)
    description=Column("description",String)
    owner=Column(Integer,ForeignKey("people.ssn"))
    
    def __init__(self,tid,description,owner):
        self.tid=tid
        self.description=description
        self.owner=owner
        
    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"


    
engine=create_engine("sqlite:///new.db",echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()

person=Person(25,"ramakant","mudgul","M",76)
session.add(person)
session.commit()

# p5=Person(8,"ram","vise","M",29)
# p6=Person(6,"manjusha","ukande","F",23)
# p7=Person(9,"rushikesh","khairnar","M" ,22)
# p8=Person(5,"yash","lakkad","M",26)
# p9=Person(11,"nandini","vise","M",29)
# p10=Person(12,"nirmala","ukande","F",23)
# p11=Person(14,"aarti","khairnar","M" ,22)
# p12=Person(24,"aayush","lakkad","M",26)


# session.add(p5)
# session.add(p6)
# session.add(p7)
# session.add(p8)
# session.add(p9)
# session.add(p10)
# session.add(p11)
# session.add(p12)
# session.commit()
# t1=Thing(1,"car",p5.ssn)
# session.add(t1)
# session.commit()

# t11=Thing(11,"Bugati",p6.ssn)
# t22=Thing(22,"Farrari",p6.ssn)
# t23=Thing(33,"Rolls Roys",p7.ssn)
# t34=Thing(44,"Fortuner",p8.ssn)
# t21=Thing(55,"bike",p9.ssn)
# t11=Thing(11,"scooty",p10.ssn)
# t22=Thing(22,"bike",p11.ssn)
# t23=Thing(33," xuv300",p12.ssn)
# t34=Thing(44,"thar",p9.ssn)
# t21=Thing(55,"bolero",p11.ssn)
# session.add(t11)
# session.add(t22)
# session.add(t23)
# session.add(t34)
# session.add(t21)
# session.commit()




# result=session.query(Person).all()           #print all the record query
# print(result)

# result=session.query(Person).filter(Person.lastname=="vise")    #search the record  by last name

# for r in result:
#     print(r)
    
# result=session.query(Person).filter(Person.age>22)    #search the record  by age
# for r in result:
#     print(r)

# result=session.query(Thing).all()             #print all the record of thing table
# print(result)

# result=session.query(Person).filter(Person.ssn!=1).update({Person.firstname:"shyam"},synchronize_session=False)
# print(result)                             //update the record  
        

# result=session.query(Person).update().where(Person.ssn==5).values(firstname="Shyam")  
# print(result)

# result=session.query(Thing,Person).filter(Thing.owner==Person.ssn).filter(Person.firstname=="manjusha")
# for r in result:
#     print(r)                        #search by foregin key of things table and person table
    