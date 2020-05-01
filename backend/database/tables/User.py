from sqlalchemy import Column, Integer, String, Sequence, Table, UniqueConstraint
import jwt
import datetime
from .Utils import *
from .Base import *
from .BlacklistToken import BlacklistToken
import logging
import pathlib, sys

'''currentPath = pathlib.Path(__file__).parent.absolute()
databasedir = currentPath.parent.absolute()
sys.path.insert(0,databasedir)
backenddir = databasedir.parent.absolute()
sys.path.insert(0,backenddir)

from api import bcrypt, app'''

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,  Sequence('user_id_seq'), primary_key=True)
    fullname = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(50))
    role = Column(String(50), nullable=False)

    def __init__(self, fullname=None, phone=None, email=None, role=None, password=None):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.role = role
        self.password = password


    def __repr__(self):
        return "<User(fullname='%s', password='%s', phone='%s', email='%s', role='%s')>" % (
                                  self.fullname, self.password,
                                  self.phone, self.email, self.role)

    def create(self, engine, meta):
        logging.debug("Creating Table Users")
        user = Table(self.__tablename__, meta,
        Column('id',Integer,  Sequence('user_id_seq'), primary_key=True),
        Column('fullname', String(50), nullable=False),
        Column('password', String(50), nullable=False),
        Column('phone', String(50)),
        Column('email', String(50), nullable=False),
        Column('role', String(50), nullable=False),
        UniqueConstraint('email'),
        extend_existing=True
        )
        try:
            user.create(engine)
            logging.info("Table Users Created")
        except:
            logging.error("Failed Create Table Users")
    
    '''def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
    '''
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table Users")
        logging.info("Migration for Table Users Done")