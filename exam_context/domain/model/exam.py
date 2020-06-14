from sqlalchemy import Column, Integer, JSON, String

from common.infrastucture.shared.base import Base


class Exam(Base):

    __tablename__ = 'exam'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quizzes = Column(JSON)
