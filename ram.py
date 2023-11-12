

# from user_table import post
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
# ,from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker,declarative_base

from socialmedia import users

#create a Connection to the database
engine=create_engine('sqlite:///ram.db',echo=True)
Session=sessionmaker()
session=Session(bind=engine)
# conn=engine.connect()


#Create a base class for our models
Base=declarative_base()

#define our models as classes that inherit from the base calss
class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    
    #define a relationship to the post table
    posts=relationship('Post',back_populates='author')
    
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
    Base.metadata.create_all(bind=engine)
        
    id=1
    name="sham_vise"
    email="shyamvise@gmail.com"
    
    Users=users(id,name,email)
    session.add(Users)
    session.commit()
    print("db is created")
    # def __repr__(self):
    #     return"<User(%r,%r,%r)>"%(self.id, self.name, self.email)
    
    # conn.ecexute(users.insert(), [
    #     {'id':1, 'name':"sham", 'email':"sham@gmail.com"},
    #     {'id':2, 'name':"ram", 'email':"ram@gmail.com"},
    #     {'id':3, 'name':"rushi", 'email':"rushi@gmail.com"},
    #     {'id':4, 'name':"manju", 'email':"manju@gmail.com"},
    #     {'id':5, 'name':"manish", 'email':"manish@gmail.com"},
    #     {'id':6, 'name':"harish", 'email':"harish@gmail.com"},
    #     {'id':7, 'name':"ganesh", 'email':"ganesh@gmail.com"},
    #     {'id':8, 'name':"tushar", 'email':"tushar@gmail.com"},
        
    # ])
    # conn.commit()
    
class Post(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String)
    content=Column(String)
    author_id=Column(Integer,ForeignKey('users.id'))
    
    # define a relationship to the users table
    author=relationship('User',back_populates='posts')
    
    
    # def __repr__(self):
    #     return"<Post(%r,%r,%r,%r)>"%(self.id, self.title, self.content, self.author_id)
    
    # session.add_all([
    #     Post(id=1, title="amrutvwl", content="jssu",author_id=11),
    #     Post(id=2, title="nakhshikant", content="usns", author_id=12),
    #     Post(id=3, title="chava", content="ksi", author_id=11),
    #     Post(id=5, title="the grear shivaji", content="yhd", author_id=11),
    #     Post(id=6, title="naykabhed", content="mnc", author_id=11),
    #     Post(id=7, title="dasbodh", content="xyx", author_id=11),
    #     Post(id=8, title="bhudbhushan", content="abc", author_id=11),
        
    # ])
class Comment(Base):
    __tablename__='comments'
    id=Column(Integer,primary_key=True)
    content=Column(String)
    post_id=Column(Integer,ForeignKey('posts.id'))
    
    #define the relationship to the posts table
    post=relationship('Post',back_populates='comments')
    
#create all the table in the database
Base.metadata.create_all(engine)




    
    
    
