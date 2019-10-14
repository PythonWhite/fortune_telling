from flask import Flask
from db import db


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
