import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
import datetime
 
Base = declarative_base()

# connect to db
engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe')
 


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    rfid_c = Column(String(50), unique=True)
    keys = relationship(
        'Key',
        secondary='user_key_link'
    )
    
    def __init__(self, firstname, lastname, rfid_c):
        self.firstname = firstname
        self.lastname = lastname
        self.rfid_c = rfid_c

    def __repr__(self):
        return '( {0}:{1.firstname!r}:{1.lastname!r}:{1.rfid_c!r}:{1.keys!r} )'.format(User, self)
 
 
class Key(Base):
    __tablename__ = 'key'
    id = Column(Integer, primary_key=True)
    room = Column(String(50))
    rfid_s = Column(String(50), unique=True)
    status = Column(Boolean, default=True)
    
    def __init__(self, room, rfid_s, status):
        self.room = room
        self.rfid_s = rfid_s
        self.status = status

    def __repr__(self):
        return '( {0}:{1.room!r}:{1.rfid_s!r}:{1.status!r}:{1.users!r} )'.format(Key, self)
 
 
class UserKeyLink(Base):
    __tablename__ = 'user_key_link'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    key_id = Column(Integer, ForeignKey('key.id'), primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship(User, backref=backref("user_assoc"))
    key = relationship(Key, backref=backref("key_assoc"))
    
    def __repr__(self):
        return '( {0}:{1.user!r}:{1.key!r}:{1.date!r} )'.format(UserKeyLink, self)
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
sess = session()

key1 = Key(room="123", rfid_s="111", status=True)
key2 = Key(room="111", rfid_s="444", status=True)
key3 = Key(room="222", rfid_s="888", status=True)
user1 = User(firstname="John", lastname="Johnson", rfid_c="222")
user2 = User(firstname="Harry", lastname="Potter", rfid_c="333")
user3 = User(firstname="John", lastname="Cena", rfid_c="555")
user4 = User(firstname="Piter", lastname="Piterson", rfid_c="666")

keylink = UserKeyLink(user=user2, key=key1)

sess.add_all([key1, key2, key3, user1, user2, user3, user4, keylink])
sess.commit()

all_links = sess.query(UserKeyLink).filter().all()
# add one item
# sess.add(key1)

# add all items
# sess.add_all([key1, user1, user2])

# filter items from table
# sess.query(User).filter(User.firstname == 'Harry').one()

print "READY TO WORK"
import pdb;pdb.set_trace()
#Close the connection
engine.dispose()
