from flask import Blueprint, request, Response, jsonify

from quiz_context.application.quiz_application_service import create_quiz, get_quiz
from quiz_context.application.quiz_create_command import QuizCreateCommand

quiz_blueprint = Blueprint('quiz', __name__)


@quiz_blueprint.route('/quizzes', methods=['POST'])
def create():
    payload = request.json
    quiz_create_command = QuizCreateCommand(
        stem=payload.get('stem'),
        options=payload.get('options'),
        reference=payload.get('reference')
    )
    create_quiz(quiz_create_command)
    return Response(status=201)


@quiz_blueprint.route('/quizzes/<int:quiz_id>', methods=['GET'])
def get(quiz_id):
    quiz = get_quiz(quiz_id)
    return jsonify({
        'id': quiz.id,
        'stem': quiz.stem,
        'options': [option.text for option in quiz.quiz_option]
    }), 200
