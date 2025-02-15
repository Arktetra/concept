from pathlib import Path
from typing import Any, Mapping

from flask import Flask


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
        DB_HOST="dpg-cu5ngjt2ng1s73bh2erg-a.oregon-postgres.render.com",
        DB_NAME="concept_db",
        DB_USER="concept_db",
        DB_PASSWORD="eszJb8N8NOxcaeXn94WFmbViP5lEmX8S",
        DB_PORT=5432,
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

    from . import db

    db.init_app(app)

    from .auth.routes import auth_bp

    app.register_blueprint(auth_bp)

    from . import posts

    app.register_blueprint(posts.bp)

    from . import concepts

    app.register_blueprint(concepts.bp)

    from . import categories

    app.register_blueprint(categories.bp)

    return app
