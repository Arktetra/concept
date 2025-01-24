import psycopg2
from flask import Flask, current_app, g


def get_db_connection() -> psycopg2.extensions.connection:
    if "db_conn" not in g:
        g.db_conn = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            database=current_app.config["DB_NAME"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            port=current_app.config["DB_PORT"],
        )
    return g.db_conn


def close_db_connection(e: Exception | None = None) -> None:
    db_conn = g.pop("db_conn", None)
    if db_conn is not None:
        db_conn.close()


def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db_connection)
