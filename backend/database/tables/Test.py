from sqlalchemy import Column, Integer, String, Sequence, Table, UniqueConstraint
from .Utils import *
from .Base import *
import logging

class Test(Base):
    __tablename__ = 'tests'
    
    id = Column(Integer,  Sequence('test_id_seq'), primary_key=True)
    code = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    institution = Column(String(50), nullable=False)
    

    def __repr__(self):
        return "<Test(code='%s', name='%s', year='%d', institution='%s')>" % (
                                  self.code, self.name, self.year,
                                  self.institution)

    def create(self, engine, meta):
        logging.debug("Creating Table Tests")
        test = Table(self.__tablename__, meta,
        Column('id',Integer,  Sequence('test_id_seq'), primary_key=True),
        Column('code', String(50), nullable=False),
        Column('name', String(50), nullable=False),
        Column('year', Integer, nullable=False),
        Column('institution', String(50), nullable=False),
        UniqueConstraint('code'),
        extend_existing=True
        )
        try:
            test.create(engine)
            logging.info("Table Tests Created")
        except:
            logging.error("Failed Create Tests Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table Tests")
        logging.info("Migration for Table Tests Done")