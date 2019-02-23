from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand





#local imports
from settings import app_settings

# db variable initialization

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(settings_name):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_settings[settings_name])
    Bootstrap(app)
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app import models
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .book import book as books_blueprint
    app.register_blueprint(books_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app