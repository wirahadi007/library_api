from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import get_config
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py based on environment
    app.config.from_object(get_config())

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    #swager UI
    swagger = Swagger(app)

    # Register Blueprints
    from app.authors import authors_bp
    from app.books import books_bp
    app.register_blueprint(authors_bp, url_prefix='/authors')
    app.register_blueprint(books_bp, url_prefix='/books')

    return app
