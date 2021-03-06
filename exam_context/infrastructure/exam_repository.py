from common.infrastucture.repository import OpenSession
from exam_context.domain.model.exam import Exam


def save(exam: Exam):
    with OpenSession() as session:
        session.add(exam)


def get_all():
    with OpenSession() as session:
        return session.query(Exam).all()
