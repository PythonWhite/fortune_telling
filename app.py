import os
from flask import Flask



def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()