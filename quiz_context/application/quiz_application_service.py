from quiz_context.application.quiz_create_command import QuizCreateCommand
from quiz_context.domain.model.quiz import Quiz
from quiz_context.domain.model.quiz_option import QuizOption
from quiz_context.infrastructure.quiz_repository import save


def create_quiz(quiz_create_command: QuizCreateCommand):
    quiz = Quiz(
        stem=quiz_create_command.stem,
        reference=quiz_create_command.reference
    )
    quiz_options = [QuizOption(
        text=option.get('text'),
        correct=option.get('correct'),
    ) for option in quiz_create_command.options]
    save(quiz, quiz_options)
