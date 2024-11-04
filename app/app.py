from flask import Flask
from dotenv import load_dotenv
from .services.slack_service.routes import slack_routes


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.register_blueprint(slack_routes)

    return app
