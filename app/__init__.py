from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

#local imports
from settings import app_settings

# db variable initialization

db = SQLAlchemy()


def create_app(settings_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_settings[settings_name])
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'


    return app