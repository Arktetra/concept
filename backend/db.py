import click
import psycopg2
from flask import Flask, current_app, g
from psycopg2.extensions import connection


def get_db() -> connection:
    if "db" not in g:
        g.db = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            database=current_app.config["DB_NAME"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"],
            port=current_app.config["DB_PORT"],
        )

    return g.db


def init_db() -> None:
    """
    Clear the existing data and create new tables.
    """
    db: connection = get_db()

    try:
        cur = db.cursor()
        with current_app.open_resource("schema.sql") as f:
            cur.execute(f.read().decode("utf8"))

        db.commit()
    except Exception as e:
        raise e


def close_db(e: Exception | None = None) -> None:
    db: connection = g.pop("db", None)
    if db is not None:
        db.close()


@click.command("init-db")
def init_db_command() -> None:
    """
    Command to clear the existing data and create new tables.
    """
    init_db()
    click.echo("Initialized the database.")


@click.command("fill-db")
def fill_db_command() -> None:
    """
    Command to fill the tables in the data with dummy values.
    """
    db: connection = get_db()

    try:
        cur = db.cursor()

        cur.execute(
            """
            INSERT INTO Users (user_id, user_name, email, password, mobile, role)
            VALUES (1, 'John Doe', 'john.doe@example.com', 'securepassword', '123456789', 'author');
            """
        )

        cur.execute(
            """
            INSERT INTO Categories (category_id, title, abstract)
            VALUES (1, 'Sample Category', 'Description of the sample category.');
            """
        )

        cur.execute(
            """
            INSERT INTO Posts (post_id, title, content, abstract, category_id)
            VALUES
            (1, 'Sample Post', 'This is a sample post content.', 'Sample abstract', NULL),
            (
                2,
                'Sample Post that is inside a Category',
                'This is a sample post content.',
                'Sample abstract',
                1
            );
            """
        )

        cur.execute(
            """
            INSERT INTO PostUser (post_id, user_id)
            VALUES
                (1, 1),
                (2, 1);
            """
        )

        cur.execute(
            """
            INSERT INTO Tags (tag_id, tag_name, post_id, content)
            VALUES (1, 'Sample Tag', 1, 'Tag content for the sample post.');
            """
        )

        cur.execute(
            """
            INSERT INTO Comments (comment_id, post_id, user_id, comment_text)
            VALUES (1, 1, 1, 'This is a sample comment.');
            """
        )

        db.commit()

    except Exception as e:
        raise e


@click.command("show-db")
@click.option("--name", default="Users", help="The table name.")
def show_db_command(name: str) -> None:
    """
    Command to select all data in tables.
    """
    cur = get_db().cursor()
    cur.execute(f"SELECT * FROM {name}")

    print(cur.fetchall())


def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)
    app.cli.add_command(show_db_command)
