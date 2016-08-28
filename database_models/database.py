import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()



class Keys(Base):
    __tablename__ = 'keys'
    
    id = Column(Integer, primary_key=True)
    room = Column(String(250), nullable=False)
    rfid = Column(String(250), nullable=False)
    status = Column(Boolean)
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    rfid_card = Column(String(250)), nullable=False)
    taked_keys = relationship('Keys', secondary='history')

    
class History(Base):
    __tablename__ = 'history'
    
    key = Column.ForeignKey('Keys', )
    user = Column.ForeignKey('')


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe', echo=True)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

#Close the connection
engine.dispose()
'''
Session example:

Session = sessionmaker(bind=engine)
session = Session()
 
#Insert multiple data in this session, similarly you can delete
customer = Customer(name='Linux', email='linux@example.com')
customer2 = Customer(name='Python', email='python@example.com')
 
session.add(customer)
session.add(customer2)
 
try:
    session.commit()
#You can catch exceptions with SQLAlchemyError base class
except SQLAlchemyError as e:
    session.rollback()
    print (str(e)) 


'''
