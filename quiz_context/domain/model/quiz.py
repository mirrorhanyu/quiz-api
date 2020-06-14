from sqlalchemy import Column, Integer, String

from quiz_context.domain.shared.base import Base


class Quiz(Base):

    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True)
    stem = Column(String)
    reference = Column(String)

