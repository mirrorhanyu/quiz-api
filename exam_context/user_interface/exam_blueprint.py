from flask import Blueprint, request, Response, jsonify

from exam_context.application.exam_application_service import create_exam, list_exams
from exam_context.application.exam_create_command import ExamCreateCommand

exam_blueprint = Blueprint('exam', __name__)


@exam_blueprint.route('/exams', methods=['POST'])
def create():
    payload = request.json
    exam_create_command = ExamCreateCommand(
        name=payload.get('name'),
        quizzes=payload.get('quizzes'),
    )
    create_exam(exam_create_command)
    return Response(status=201)


@exam_blueprint.route('/exams', methods=['GET'])
def get_all():
    exams = list_exams()
    return jsonify([{
        'id': exam.id,
        'name': exam.name
    } for exam in exams]), 200
