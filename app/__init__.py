"""App module for flask app."""

import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# from app.blueprints.api import api_bp
from app.blueprints.images import img_bp
from app.extensions import db, migrate, ma
from app.settings import config


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


def create_app(enviroment="development"):
    """
    Create a flask app and configure it
    """
    app = Flask("restApi")
    app.config.from_object(config[enviroment])

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    """
    Register extensions on the app instance
    """
    CORS(
        app,
        origins="*",
        allow_headers=[
            "Content-Type",
            "Authorization",
            "Access-Control-Allow-Credentials",
        ],
        supports_credentials=True,
    )
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


def register_blueprints(app):
    """
    Register blueprints on the app instance
    """
    # app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(img_bp, url_prefix="/api")
