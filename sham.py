from sqlalchemy import create_engine,ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base =declarative_base()

# class Person(Base):
#     __tablename__="people"

#     ssn=Column("ssn",Integer,primary_key=True)
#     firstname=Column("firstname",String)
#     lastname=Column("lastname",String)
#     gender=Column("gender",CHAR)
#     age=Column("age",Integer)

#     def __init__(self,ssn,firstname,lastname,gender,age):
#         self.ssn=ssn
#         self.first=firstname
#         self.last=lastname
#         self.gender=gender
#         self.age=age

#     def __repr__(self):
#         return f"({self.ssn}){self.firstname} {self.lastname} {self.gender} {self.age}"
    
# engine=create_engine("sqlite:///mydb.db",echo=True)
# Base.metadata.create_all(bind=engine)


# Session=sessionmaker(bind=engine)
# session=Session()

# person =Person(123, "sham", "vise", "M", 24)
# session.add(person)
# session.commit()

# p1 =Person(1263, "ramakant", "shrivastav", "f", 74)
# p3 =Person(14523, "manjusha", "mankarni", "f", 23)

# session.add(p1)
# # session.add(p2)
# session.add(p3)
# session.commit()

results=session.query(Person).filter
print(results)


         


    