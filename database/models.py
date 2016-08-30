import datetime
import logging
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine, exc
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
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
            return session.query(User).filter(User.rfid_c == rfid).first()
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
            raise Exception('User not deleted with error:{0}'.format(e))

    @classmethod
    @dbsession
    def user_get_by_rfid(self, rfid, session):
        ''' Get user by str(rfid) '''

        logger.info('Start getting user by rfid..')

        try:
            user = session.query(User).filter(User.rfid_c == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Can't get user by RFID:'%s'", rfid)
            raise Exception('Cant get user by RFID:{0}'.format(e))
        if user:
            return user
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
            return users
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
    @dbsession
    def key_get_by_rfid(self, rfid, session):
        ''' Get key by str(rfid) '''

        logger.info('Start getting key by RFID..')

        try:
            key = session.query(Key).filter(Key.rfid_s == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get key by rfid: %s , %s", rfid, e)
            raise Exception('Cant get key by RFID:{0}'.format(e))
        if key:
            return key
        else:
            raise IOError('WARNING!Key by RFID:{0} not found'.format(rfid))

    @classmethod
    @dbsession
    def key_get_all_keys(self, session):
        ''' Method for getting all keys '''

        logger.info('Getting all keys..')

        try:
            keys = session.query(Key).filter().all()
        except exc.SQLAlchemyError as e:
            logger.info("Cant get all keys. %s", e)
            raise Exception('Cant get all keys. {0}'.format(e))
        if keys:
            return keys
        else:
            raise IOError('WARNING!Keys not found')

    @classmethod
    @dbsession
    def key_new(self, room, rfid, session):
        ''' Create key, str(room), str(rfid)'''

        logger.info('Start creating new Key..')

        try:
            if rfid in [key.rfid_s for key in session.query(Key).filter().all()]:
                raise IOError('WARNING!Key with this RFID: {0} already exist!'.format(rfid))

            new_key = Key(room=room, rfid_s=rfid, status=True)

            session.add(new_key)
            session.commit()
            logger.info("Created key for room:{0}, with RFID:{1}".format(room, rfid))
            return session.query(Key).filter(Key.rfid_s == rfid).first()
        except exc.SQLAlchemyError as e:
            logger.info("Key not created with error:{0}".format(e))
            raise Exception('Key not created with error {0}'.format(e))

    @classmethod
    @dbsession
    def key_delete(self, key, session):
        ''' Delete key by object '''

        logger.info('Start deleting key..')

        try:
            session.delete(key)
            session.commit()
            logger.info("Key deleted.")
        except exc.SQLAlchemyError as e:
            logger.info("Key DO NOT deleted from room:%s with RFID:%s", key.room, key.rfid_s)
            raise Exception('Key not deleted with error:{0}'.format(e))

    def __repr__(self):
        return '< {0}:{1.room!r}:{1.rfid_s!r}:{1.status!r}:{1.users!r} >'.format(Key, self)


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
    @dbsession
    def userkeylink_get_key(self, user, key, session):
        ''' Get key by user and key object'''

        logger.info('Start getting Key..')

        if key.status is False:
            logger.info('Sorry, but key from room:%s already taken by user:%s', key.room, key.users[-1].lastname)
            raise IOError('WARNING!Key already taken !')

        try:
            new_get = UserKeyLink(user=user, key=key)
            session.add(new_get)
            key.status = False
            session.commit()
            logger.info('User: %s with RFID:%s get key from room:%s with RFID:%s',
                        user.lastname, user.rfid_c, key.room, key.rfid_s)
            return new_get
        except exc.SQLAlchemyError as e:
            logger.info("Some error happend when user %s take a key %s. \n --- %s", user.id, key.id, e)
            raise Exception('Some error happend when user take a key:{0}'.format(e))

    @classmethod
    @dbsession
    def userkeylink_return_key(self, key, session):
        ''' Returned key by object '''

        logger.info('Starting returned Key..')

        if key.status is True:
            logger.info('Key from room:%s already returned!', key.room)
            raise IOError('WARNING!Key already returned !')

        try:
            relation = session.query(UserKeyLink).filter(UserKeyLink.key == key).first()
            relation.date_returned = datetime.datetime.utcnow()
            key.status = True
            session.add(relation)
            session.commit()
            logger.info('Key from room:%s returned!', key.room)
            return relation
        except (exc.SQLAlchemyError, InvalidRequestError) as e:
            logger.info("Some error happend when key id:%s returned %s", key.id, e)
            raise Exception('Some error happend when key returned:{0}'.format(e))

    def __repr__(self):
        return '< {0}:{1.user!r}:{1.key!r}:{1.date_taked!r}:{1.date_returned!r} >'.format(UserKeyLink, self)
