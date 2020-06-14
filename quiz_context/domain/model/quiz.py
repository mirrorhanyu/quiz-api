from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from common.infrastucture.shared.base import Base


class Quiz(Base):

    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    stem = Column(String)
    reference = Column(String)

    quiz_option = relationship('QuizOption', cascade="all, delete, delete-orphan")



