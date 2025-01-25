from pathlib import Path
from typing import Any, Mapping

from flask import Flask

from backend.auth.routes import auth_bp
from backend.database.connection import init_app


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    """
    An application factory for creating a Flask instance. Any configuration,
    registration and other setup the application needs will happen inside this
    function, then the application will be returned.

    Args:
        test_config (_type_, optional): test configuraiton. Defaults to None.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        # Load the instance config (if it exists), when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    except OSError:
        pass

    init_app(app)
    app.register_blueprint(auth_bp)
    return app


app = create_app()
