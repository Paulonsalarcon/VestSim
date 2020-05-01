from sqlalchemy import Column, Integer, String, Sequence, Table
from .Utils import *
from .Base import *
import logging

class Answer(Base):
    __tablename__ = 'answers'
    
    id = Column(Integer,  Sequence('answer_id_seq'), primary_key=True)
    description = Column(String(2000), nullable=False)
    image = Column(String(500))

    def __repr__(self):
        return "<Answer(description='%s', image='%s')>" % (
                                  self.description, self.image,)

    def create(self, engine, meta):
        logging.debug("Creating Table Answers")
        answer = Table(self.__tablename__, meta,
        Column('id',Integer,  Sequence('answer_id_seq'), primary_key=True),
        Column('description', String(2000), nullable=False),
        Column('image', String(500)),
        extend_existing=True
        )
        try:
            answer.create(engine)
            logging.info("Table Answers Created")
        except:
            logging.error("Failed Create Answers Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table Answers")
        logging.info("Migration for Table Answers Done")