from flask import Flask
from app.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database
    init_db(app)

    # Register routes
    from app.routes import crm_blueprint

    app.register_blueprint(crm_blueprint, url_prefix="/api/crm")

    return app
