from sqlalchemy import Column, Integer, Sequence, Table, UniqueConstraint, ForeignKey, DateTime, Boolean
from .Utils import *
from .Base import *
import logging

class Trial(Base):
    __tablename__ = 'trials'
    
    id = Column(Integer,  Sequence('trial_id_seq'), primary_key=True)
    user = Column(Integer, ForeignKey("users.id"), nullable=False)
    numberofTrials = Column(Integer, nullable=False)
    correctanswers = Column(Integer, nullable=False)
    wronganswers = Column(Integer, nullable=False)
    dificulty = Column(Integer)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime)
    finished = Column(Boolean)

    def __repr__(self):
        return "<Trial(user='%d', numberofTrials='%d', correctanswers='%d', wronganswers='%d', dificulty='%d', start='%d', end='%d', finished='%b' )>" % (
                                  self.user, self.numberofTrials, self.correctanswers,
                                  self.wronganswers, self.dificulty, self.start,
                                  self.end, self.finished)

    def create(self, engine, meta):
        logging.debug("Creating Table Trials")
        trial = Table(self.__tablename__, meta,
        Column('id',Integer,  Sequence('trial_id_seq'), primary_key=True),
        Column('user', Integer, ForeignKey("users.id"), nullable=False),
        Column('numberofTrials', Integer, nullable=False),
        Column('correctanswers', Integer, nullable=False),
        Column('wronganswers', Integer, nullable=False),
        Column('dificulty', Integer),
        Column('start', DateTime, nullable=False),
        Column('end', DateTime),
        Column('finished', Boolean),
        extend_existing=True
        )
        try:
            trial.create(engine)
            logging.info("Table Trials Created")
        except:
            logging.error("Failed Create Trials Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table Trials")
        logging.info("Migration for Table Trials Done")