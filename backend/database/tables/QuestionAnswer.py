from sqlalchemy import Column, Integer, String, Sequence, Table, UniqueConstraint, ForeignKey
from .Utils import *
from .Base import *
import logging

class QuestionAnswer(Base):
    __tablename__ = 'question_answers'
    
    question = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    answer = Column(Integer, ForeignKey("answers.id"), primary_key=True)

    def __repr__(self):
        return "<Question(question='%d', answer='%d')>" % (
                                  self.question, self.answer)

    def create(self, engine, meta):
        logging.debug("Creating Table QuestionAnswers")
        questionanswer = Table(self.__tablename__, meta,
        Column('question', Integer, ForeignKey("tests.id"), primary_key=True),
        Column('answer', Integer, ForeignKey("answers.id"), primary_key=True),
        extend_existing=True
        )
        try:
            questionanswer.create(engine)
            logging.info("Table QuestionAnswers Created")
        except:
            logging.error("Failed Create QuestionAnswers Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table QuestionAnswers")
        logging.info("Migration for Table QuestionAnswers Done")