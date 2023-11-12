from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR,'emp.db')


Base=declarative_base()

engine=create_engine(connection_string,echo=True)

Session=sessionmaker()

""""
class User
    id int
    username str
    email str
    date_created datetime
"""

class Employee(Base):
    __tablename__='employee'
    id=Column(Integer(),primary_key=True)
    fname=Column(String(25),nullable=False,unique=True)
    lname=Column(String(80),unique=True,nullable=False)
    date_created=Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return f"<Employee fname={self.fname} lname={self.lname}>"


new_user=Employee(id=1,fname="ram",lname="Kute")
print(new_user)