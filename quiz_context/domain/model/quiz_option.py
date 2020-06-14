from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from common.infrastucture.shared.base import Base


class QuizOption(Base):

    __tablename__ = 'quiz_option'

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quiz.id'))
    text = Column(String)
    correct = Column(Boolean)

