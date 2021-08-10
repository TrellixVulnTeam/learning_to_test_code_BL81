"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, config
import flask_excel

# initializes extensions
db = SQLAlchemy()

# application factory
def create_app(config):
    
    # create application instance
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    flask_excel.init_excel(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models # miguel uses
