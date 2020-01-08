from monarch import config
from flask import Blueprint
from flask_restplus import Api


def register_api(app):
    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api = Api(
        blueprint,
        title="New API",
        version="1.0",
        description="New API",
        doc=config.ENABLE_DOC,
    )

    app.register_blueprint(blueprint)
