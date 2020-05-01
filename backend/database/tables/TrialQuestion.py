from sqlalchemy import Column, Integer, Table,ForeignKey, Boolean
from .Utils import *
from .Base import *
import logging

class TrialQuestion(Base):
    __tablename__ = 'trialquestions'
    
    trial = Column(Integer, ForeignKey("trials.id"), primary_key=True)
    question = Column(Integer, ForeignKey("questions.id"), primary_key=True)
    correctanswer = Column(Integer, ForeignKey("answers.id"), nullable=False)
    chosenanswer = Column(Integer, ForeignKey("answers.id"))
    correct = Column(Boolean)

    def __repr__(self):
        return "<Trial(trial='%d', question='%d', correctanswer='%d', chosenanswer='%d', correct='%s')>" % (
                                  self.trial, self.question, self.correctanswer,
                                  self.chosenanswer, self.correct)

    def create(self, engine, meta):
        logging.debug("Creating Table TrialQuestions")
        trialquestion = Table(self.__tablename__, meta,
        Column('trial', Integer, ForeignKey("trials.id"), primary_key=True),
        Column('question', Integer, ForeignKey("questions.id"), primary_key=True),
        Column('correctanswer', Integer, ForeignKey("answers.id"), nullable=False),
        Column('chosenanswer', Integer, ForeignKey("answers.id")),
        Column('correct', Boolean),
        extend_existing=True
        )
        try:
            trialquestion.create(engine)
            logging.info("Table TrialQuestions Created")
        except:
            logging.error("Failed Create TrialQuestions Table")
    
    #Migration
    def addColumn(self,engine,column):
        add_column(engine, self.__tablename__, column)

    def migrate(self, engine):
        logging.info("Starting Migration for Table TrialQuestions")
        logging.info("Migration for Table TrialQuestions Done")