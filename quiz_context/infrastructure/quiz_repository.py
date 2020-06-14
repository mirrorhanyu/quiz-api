from typing import List

from common.infrastucture.repository import OpenSession
from quiz_context.domain.model.quiz import Quiz
from quiz_context.domain.model.quiz_option import QuizOption


def save(quiz: Quiz, quiz_options: List[QuizOption]):
    with OpenSession() as session:
        session.add(quiz)
        session.flush()
        for quiz_option in quiz_options:
            quiz_option.quiz_id = quiz.id
            session.add(quiz_option)


def query(quiz_id: int):
    with OpenSession() as session:
        return session.query(Quiz) \
            .filter_by(id=quiz_id) \
            .join(QuizOption, QuizOption.quiz_id == Quiz.id)\
            .scalar()
