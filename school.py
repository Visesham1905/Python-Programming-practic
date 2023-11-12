from sqlalchemy import Result, create_engine,table,Column,Integer,String,CHAR,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,Relationship
Base=declarative_base()

class Student(Base):
    __tablename__='student'
    sid=Column(Integer,primary_key=True)
    sname=Column(String)
    age=Column(Integer)
    course=Column(String)
    gender=Column(CHAR)
    issuebook=Column(ForeignKey('book.bid'))
    
    def __init__(self,sid,sname,age,course,gender,issuebook):
        self.sid=sid
        self.sname=sname
        self.age=age
        self.course=course
        self.gender=gender
        self.issuebook=issuebook
        
    def __repr__(self):
        return f"({self.sid}) {self.sname} {self.age} {self.course} {self.gender} {self.issuebook}"

class Book(Base):
    __tablename__='book'
    bid=Column(Integer,primary_key=True)
    bname=Column(String)
    price=Column(Integer)
    authors_book=Column(ForeignKey("author.aid"))
    publishBook=Column(ForeignKey('publisher.pid'))
    
    
    def __init__(self,bid,bname,price,authors_book,publishBook):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.authors_book=authors_book
        self.publishBook=publishBook
        
    def __repr__(self):
        return f"({self.bid}) {self.bname} {self.price} {self.authors_book} {self.publishBook}"

class Author(Base):
    __tablename__='author'
    aid=Column(Integer,primary_key=True)
    aname=Column(String)
   
    
    def __init__(self,aid,aname):
        self.aid=aid
        self.aname=aname
        
    def __repr__(self):
        return f"({self.aid}) {self.aname}"

class Publisher(Base):
    __tablename__='publisher'
    pid=Column(Integer,primary_key=True)
    pname=Column(String )
    quantity=Column(Integer)
    
    def __init__(Publisher,pid,pname,quantity):
            Publisher.pid=pid
            Publisher.pname=pname
            Publisher.quantity=quantity

    def __repr__(Publisher):
            return f"({Publisher.pid}) {Publisher.pname} {Publisher.quantity}"

engine=create_engine("sqlite:///school.db",echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()


# student=Student(1,"shyam",23,"BCA","M",7)
# s1=Student(2,"ram",31,"mpharm","M",5)
# s2=Student(3,"rushi",22,"BCA","M",3)
# s3=Student(4,"ajay",24,"10th","M",2)
# s4=Student(51,"manjusha",23,"MCA","F",4)
# s5=Student(6,"akshada",22,"BSC","F",5)
# s6=Student(7,"sayli",22,"BSC","F",8)
# s7=Student(8,"shubhangi",23,"BCA","F",9)
# s8=Student(9,"vaishnavi",17,"12th","F",6)
# s9=Student(10,"yash",24,"BCOM","M",1)
# session.add(student)
# session.add(s1)
# session.add(s2)
# session.add(s3)
# session.add(s4)
# session.add(s5)
# session.add(s6)
# session.add(s7)
# session.add(s8)
# session.add(s9)
# session.commit()

# book=Book(1,"shyamchi_aai",560,5,3)
# b1=Book(2,"Agnipankha",890,6,5)
# b2=Book(3,"chava",890,6,5)
# b3=Book(4,"bhudbhushan",1000,3,8)
# b4=Book(5,"psychology of money",890,7,9)
# b5=Book(6,"rich dad poor dad",930,2,11)
# b6=Book(7,"Mrutunjay",760,1,14)
# b7=Book(8,"think and grow rich",540,8,13)
# b8=Book(9,"java",234,9,10)
# b9=Book(10,"paython",23000,4,12)
# session.add(book)
# session.add(b1)
# session.add(b2)
# session.add(b3)
# session.add(b4)
# session.add(b5)
# session.add(b6)
# session.add(b7)
# session.add(b8)
# session.add(b9)
# session.commit()







# book=Book(1,"Chava",600,author,publisher)
# session.add(book)
# session.commit()


# author=Author(1,"Shivaji Savant")
# session.add(author)
# session.commit()
# a1=Author(2,"Willeam Shekspare")
# a2=Author(3,"pu l deshpande")
# a3=Author(4,"sane guruji ")
# a4=Author(5,"ravindranath tagor ")
# a5=Author(6,"a.p.j.kalam")
# a6=Author(7,"swami vivekanand")
# a7=Author(8,"tukaram maharaj")
# a8=Author(9,"dnyeshwar maharaj")
# a9=Author(10,"sambhaji maharaj")
# a10=Author(11,"bahinabai chaudhari")
# a11=Author(12,"rushikesh khairnar")
# a12=Author(13,"pra.k.atre")
# a13=Author(14,"bharata")
# a14=Author(15,"vishnu sharma")
# session.add(a1)
# session.add(a2)
# session.add(a3)
# session.add(a4)
# session.add(a5)
# session.add(a6)
# session.add(a7)
# session.add(a8)
# session.add(a9)
# session.add(a10)
# session.add(a11)
# session.add(a12)
# session.add(a13)
# session.add(a14)
# session.commit()



# publisher=Publisher(1,"nirmal",200)
# p1=Publisher(2,"success",700)
# p2=Publisher(3,"harpel",400)
# p3=Publisher(4,"simon",200)
# p4=Publisher(5,"random house",500)
# p5=Publisher(6,"wilye",600)
# p6=Publisher(7,"oxferd",7700)
# p7=Publisher(8,"nirali",800)
# p8=Publisher(9,"sarvoday",100)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.add(p4)
# session.add(p5)
# session.add(p6)
# session.add(p7)
# session.add(p8)
# session.commit()

    
# result=session.query(Student).all()           #print all the record of Student
# print(result)
    
    
# result=session.query(Book).all()           #print all the record of Book
# print(result)
    
    
# result=session.query(Publisher).all()           #print all the record Publisher
# print(result)
    
    
# result=session.query(Author).all()           #print all the record of Author
# print(result)
    
# result=session.query(Student).filter(Student.age==23)    #search the record  by age 
# for r in result:
#     print(r)
    
# result=session.query(Publisher).filter(Publisher.quantity==200)    #search the record  by age 
# for r in result:
#     print(r)
    
    
# result=session.query(Book).filter(Book.price==560)    #search the record  by age 
# for r in result:
#     print(r)


# result=session.query(Author).filter(Author.aid==8)    #search the record  by age 
# for r in result:
#     print(r)

# result=session.query(Student).filter(Student.age>22)    #search the record  by age
# for r in result:
#     print(r)
    
# result=session.query(Book).filter(Book.price>560)    #search the record  by age
# for r in result:
#     print(r)

# result=session.query(Student).update().where(Student.sid==6).values(age=37)  
# print(result)

# result=session.query(Student,Book).filter(Student.issuebook==Book.bid).filter(Student.sname=="manjusha")
# for r in result:
#     print(r)          