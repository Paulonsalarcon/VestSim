from sqlalchemy import Column, Integer, String, Sequence, Table, UniqueConstraint, ForeignKey
from .Utils import *
from .Base import *
import logging

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer,  Sequence('question_id_seq'), primary_key=True)
    test = Column(Integer, ForeignKey("tests.id"), nullable=False)
    subject = Column(String(50), nullable=False)
    description = Column(String(2000), nullable=False)
    correctanswer = Column(Integer, ForeignKey("answers.id"), nullable=False)
    image = Column(String(500))
    dificulty = Column(Integer)

    def __repr__(self):
        return "<Question(test='%d', subject='%s', description='%s', correctanswer='%d', image='%s', dificulty='%d')>" % (
                                  self.test, self.subject, self.description,
                                  self.correctanswer, self.image, self.dificulty)

    def create(self, engine, meta):
        logging.debug("Creating Table Questions")
        question = Table(self.__tablename__, meta,
        Column('id',Integer,  Sequence('question_id_seq'), primary_key=True),
        Column('test', Integer, ForeignKey("tests.id"), nullable=False),
        Column('subject', String(50), nullable=False),
        Column('description', String(2000), nullable=False),
        Column('correctanswer', Integer, ForeignKey("answers.id"), nullable=False),
        Column('image', String(500)),
        Column('dificulty', Integer),
        extend_existing=True
        )
        try:
            question.create(engine)
            logging.info("Table Questions Created")
        except:
            logging.error("Failed Create Questions Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table Questions")
        logging.info("Migration for Table Questions Done")