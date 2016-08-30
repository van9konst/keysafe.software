import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from sqlalchemy.exc import InvalidRequestError
import logging
from functools import wraps


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base = declarative_base()

# connect to db
engine = create_engine('postgresql://cad_root:root_pass@localhost:5432/cad_keysafe', client_encoding='utf8')

session = sessionmaker()
session.configure(bind=engine)

def dbsession(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        result = {'data': None, 'errors': None, 'warnings': None}
        sess = session()
        logger.info('Seesion started..')
        try:
            result['data'] = f(*args, session=sess, **kwargs)
        except Exception as e:
            sess.rollback()
            if 'WARNING' in e.message:
                result['warnings'] = e
                logger.info('{0}'.format(e))
            else:
                result['errors'] = e
                logger.info('{0}'.format(e))
        finally:
            sess.close()
            logger.info('Session closed!')
        return result
    return wrapped


class User(Base):

    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    rfid_c = Column(String(50), unique=True)
    
    def __init__(self, firstname, lastname, rfid_c):
        self.firstname = firstname
        self.lastname = lastname
        self.rfid_c = rfid_c

    
    @classmethod
    @dbsession
    def user_new(self, firstname, lastname, rfid, session):
        ''' Create user by str(firstname), str(lastname), str(rfid) '''

        logger.info('Start creating new user..')

        try:
            if rfid in [i.rfid_c for i in session.query(User).filter().all()]:
                raise IOError('WARNING!User with card: {0} already exist!'.format(rfid))

            new_user = User(firstname=firstname, lastname=lastname, rfid_c=rfid)

            session.add(new_user)
            session.commit()
            logger.info("Created user:%s %s, with RFID:%s", firstname, lastname, rfid)
            return {'firstname': firstname, 'lastname': lastname, 'rfid': rfid}
        except exc.SQLAlchemyError as e:
            logger.info("User not created with error: %s", e)
            raise Exception('User not created with error:{0}'.format(e))

    @classmethod
    @dbsession
    def user_delete(self, user, session):
        ''' Delete user by object user '''

        logger.info('Start deleting user..')

        try:
            session.delete(user)
            session.commit()
            logger.info("User deleted.")
        except exc.SQLAlchemyError as e:
            logger.info("User with id: '%s' DO NOT deleted user with RFID:'%s'", user.id, user.rfid_c)
            raise Exception('User not created with error:{0}'.format(e))

    @classmethod
    @dbsession
    def user_get_by_rfid(self, rfid, session):
        ''' Get user by str(rfid) '''

        logger.info('Start getting user by rfid..')

        try:
            user = session.query(User).filter(User.rfid_c==rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get user by RFID:'%s'", rfid)
            raise Exception('Cant get user by RFID:{0}'.format(e))
        if user:
            return {'id': user.id, 'firstname': user.firstname, 'lastname': user.lastname, 'rfid': user.rfid_c, 'user_object': user}
        else:
            raise IOError('WARNING!User with card: {0} not found!'.format(rfid))

    @classmethod
    @dbsession
    def user_get_all(self, session):
        ''' Get all users objects '''
        
        logger.info('Start getting all users..')
        try:
            users = session.query(User).filter().all()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get users. {0}".format(e))
            raise Exception("Can't get users {0}".format(e))
        if users:
            users_dict = {}
            for user in users:
                users_dict[user.id] = {'firstname': user.firstname, 'lastname': user.lastname, 'rfid': user.rfid_c, 'user_object': user}
            return users_dict
        else:
            raise IOError('WARNING!Users not found')
        

    def __repr__(self):
        return '<{0} {1.firstname!r}:{1.lastname!r}:{1.rfid_c!r}>'.format(User, self)
 
 
class Key(Base):

    __tablename__ = 'key'

    id = Column(Integer, primary_key=True)
    room = Column(String(50))
    rfid_s = Column(String(50), unique=True)
    status = Column(Boolean, default=True)
    users = relationship(
        User,
        secondary='user_key_link'
    )
    
    def __init__(self, room, rfid_s, status):
        self.room = room
        self.rfid_s = rfid_s
        self.status = status
    
    @classmethod
    def key_get_by_rfid(self, rfid):
        ''' Get key by str(rfid) '''

        logger.info('Start getting key by RFID..')

        try:
            key = sess.query(Key).filter(Key.rfid_s==rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get key by rfid: %s , %s", rfid, e)
            return False
        return key
        
    @classmethod
    def key_get_all_keys(self):
        ''' Method for getting all keys '''

        logger.info('Getting all keys..')

        try:
            keys = sess.query(Key).filter().all()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get all keys. %s", e)
            return False
        return keys

    @classmethod
    def key_new(self, room, rfid_s):
        ''' Create key, str(room), str(rfid)'''
        
        logger.info('Start creating new Key..')

        new_key = Key(room=room, rfid_s=rfid_s, status=True)
        try:
            sess.add(new_key)
            sess.commit()
            logger.info("SUCCESS! Created key for room:{0}, with RFID:{1}").format(room, rfid_s)
        except exc.SQLAlchemyError as e:
            logger.info("Key not created with error:{0}").format(e)

    @classmethod
    def key_delete(self, key):
        ''' Delete key by object '''
        
        try:
            sess.delete(key)
            sess.commit()
            logger.info("SUCCESS! Key deleted.")
        except exc.SQLAlchemyError as e:
            logger.info("ERROR!Key DO NOT deleted from room:%s with RFID:%s", key.room, key.rfid_s)
        
    def __repr__(self):
        return '( {0}:{1.room!r}:{1.rfid_s!r}:{1.status!r}:{1.users!r} )'.format(Key, self)
 
 
class UserKeyLink(Base):

    __tablename__ = 'user_key_link'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    key_id = Column(Integer, ForeignKey('key.id'))
    date_taked = Column(DateTime, default=datetime.datetime.utcnow)
    date_returned = Column(DateTime, nullable=True)
    user = relationship(User)
    key = relationship(Key)

    def __init__(self, user, key):
        self.user = user
        self.key = key

    @classmethod
    def userkeylink_get_key(self, user, key):
        ''' Get key by user and key object'''
        
        logger.info('Start getting Key..')
        
        if key.status == False:
            logger.info('Sorry, but key from room:%s already taken by user:%s',key.room, key.users[-1].lastname)
            return key

        new_get = UserKeyLink(user=user, key=key)
        try:
            sess.add(new_get)
            key.status=False
            sess.commit()
            logger.info('SUCCESS!User: %s with RFID:%s get key from room:%s with RFID:%s',user.lastname, user.rfid_c, key.room, key.rfid_s)
            return 
        except exc.SQLAlchemyError as e:
            logger.info("ERROR!Some error happend when user %s take a key %s. \n --- %s", user.id , key.id, e)
    
    @classmethod
    def userkeylink_return_key(self, key):
        ''' Returned key by object '''

        logger.info('Starting returned Key..')
        
        if key.status == True:
            logger.info('Key from room:%s already returned!', key.room)
            return key

        try:
            relation = sess.query(UserKeyLink).filter(UserKeyLink.key==key).first()
            relation.date_returned = datetime.datetime.utcnow()
            key.status = True
            sess.add(relation)
            sess.commit()
            logger.info('SUCCESS!Key from room:%s returned!',key.room)
        except (exc.SQLAlchemyError, InvalidRequestError) as e:
            sess.rollback()
            sess.commit()
            logger.info("ERROR!Some error happend when key id:%s returned \n --- %s", key.id, e)

    def __repr__(self):
        return '( {0}:{1.user!r}:{1.key!r}:{1.date_taked!r}:{1.date_returned!r} )'.format(UserKeyLink, self)
        

Base.metadata.create_all(engine)

# Added test data
# key1 = Key(room="123", rfid_s="111", status=True)
# key2 = Key(room="111", rfid_s="444", status=True)
# key3 = Key(room="222", rfid_s="888", status=True)
# user1 = User(firstname="John", lastname="Johnson", rfid_c="222")
# user2 = User(firstname="Harry", lastname="Potter", rfid_c="333")
# user3 = User(firstname="John", lastname="Cena", rfid_c="555")
# user4 = User(firstname="Piter", lastname="Piterson", rfid_c="666")

# sess.add_all([key1, key2, key3, user1, user2, user3, user4])

# sess.commit()
# #engine.dispose()

# ukl1 = UserKeyLink.user_get_key(user2, key2)
# ukl2 = UserKeyLink.user_get_key(user3, key3)

# ukl3 = UserKeyLink.user_return_key(key2)
# ukl3 = UserKeyLink.user_get_key(user2, key2)

import pdb;pdb.set_trace()

print "READY TO WORK"