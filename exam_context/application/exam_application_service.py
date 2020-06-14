from exam_context.application.exam_create_command import ExamCreateCommand
from exam_context.domain.model.exam import Exam
from exam_context.infrastructure.exam_repository import save, get_all


def create_exam(exam_create_command: ExamCreateCommand):
    exam = Exam(
        name=exam_create_command.name,
        quizzes=exam_create_command.quizzes
    )
    save(exam)


def list_exams():
    return get_all()
