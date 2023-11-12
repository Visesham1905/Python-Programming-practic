from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker,declarative_base
# from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")

class GrandChild(Base):
    __tablename__ = 'grandchild'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child", back_populates="grandchildren")

class GreatGrandChild(Base):
    __tablename__ = 'great_grandchild'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grandchild_id = Column(Integer, ForeignKey('grandchild.id'))
    grandchild = relationship("GrandChild", back_populates="great_grandchildren")

engine = create_engine('sqlite:///orm.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parent1 = Parent(name='Parent 1')
parent2 = Parent(name='Parent 2')

child1_1 = Child(name='Child 1-1', parent=parent1)
child1_2 = Child(name='Child 1-2', parent=parent1)
child2_1 = Child(name='Child 2-1', parent=parent2)

grandchild1_1_1 = GrandChild(name='Grandchild 1-1-1', child=child1_1)
grandchild1_2_1 = GrandChild(name='Grandchild 1-2-1', child=child1_2)

great_grandchild1_1_1_1 = GreatGrandChild(name='Great Grandchild 1-1-1-1', grandchild=grandchild1_1_1)

session.add_all([parent1, parent2])
session.add_all([child1_1, child1_2, child2_1])
session.add_all([grandchild1_1_1, grandchild1_2_1])
session.add_all([great_grandchild1_1_1_1])

session.commit()