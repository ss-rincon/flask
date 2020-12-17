from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "mintic2022"
    app.config["SQLALCHEMY_DATABAS_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app