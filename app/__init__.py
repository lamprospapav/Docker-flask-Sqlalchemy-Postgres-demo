from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#local imports
from settings import app_settings

# db variable initialization

db = SQLAlchemy()
#login_Manager = Login_Manager()

def create_app(settings_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_settings[settings_name])
    app.config.from_pyfile('settings.py')
    db.init_app(app)

    #from app import models


    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    #login_Manager.init_app(app)
    #login_manager.login_message = "You must be logged in to access this page."
    #login_manager.login_view = "auth.login"


    return app