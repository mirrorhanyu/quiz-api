from sqlalchemy import Column, Integer, JSON

from common.infrastucture.shared.base import Base


class Exam(Base):

    __tablename__ = 'exam'

    id = Column(Integer, primary_key=True)
    quizzes = Column(JSON)
