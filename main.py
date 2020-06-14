from flask import Flask

from quiz_context.user_interface.quiz_blueprint import quiz_blueprint

app = Flask(__name__)

app.register_blueprint(quiz_blueprint)

app.run()
