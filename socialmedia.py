# from sqlalchemy import create_engine,ForeignKey,String,Integer,Column
# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker,declarative_base
# import uuid



# Base=declarative_base()

# def generate_uuid():
#     return str(uuid.uuid())

# class users(Base):
#     __tablename__="users"
#     userid=Column("userid",String,primary_key=True,default=generate_uuid)
#     firstName=Column("firstName",String)
#     lastName=Column("lastName",String)
#     profileName=Column("profileName",String)
#     email=Column("email",String)
    
#     def __init__(self,firstName,lastName,profileName,email):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.profileName=profileName
#         self.email=email
        
# db="sqlite:///social.db"
# engine=create_engine(db)


        

    
    