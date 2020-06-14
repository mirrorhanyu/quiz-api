from flask import Flask

from exam_context.user_interface.exam_blueprint import exam_blueprint
from quiz_context.user_interface.quiz_blueprint import quiz_blueprint

app = Flask(__name__)

app.register_blueprint(quiz_blueprint)
app.register_blueprint(exam_blueprint)

app.run()
