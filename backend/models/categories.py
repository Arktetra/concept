from flask import Response, jsonify, make_response
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.utils import database_error


class Categories:
    """
    A class for handling interactions with the Categories table in the
    database.
    """

    @staticmethod
    def get(id: int) -> Response:
        # try:
        conn = get_db()
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(
                """
                SELECT *, 'posts' AS type FROM Posts
                WHERE category_id = (%s)
                """,
                (id,),
            )
            posts = cursor.fetchall()

            cursor.execute(
                """
                SELECT user_name FROM Users
                JOIN PostUser
                ON Users.user_id = PostUser.user_id
                JOIN Posts
                ON Posts.post_id = PostUser.post_id
                WHERE Posts.category_id = (%s)
                """,
                (id,),
            )

            authors = cursor.fetchall()

        data = []

        for post in posts:
            data.append(
                {
                    "id": post[0],
                    "title": post["title"],
                    "abstract": post["abstract"],
                    "created_at": post["created_at"],
                    "updated_at": post["updated_at"],
                    "authors": authors,
                    "type": post["type"],
                }
            )

        return jsonify(data)

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the category id for the new category.

        Returns:
            int: a category id.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT category_id FROM Categories
                    ORDER BY category_id DESC
                    LIMIT 1;
                    """
                )
                category_id = cursor.fetchone()

                category_id = category_id[0] if category_id else 1

            return category_id + 1
        except Exception as e:
            return database_error(e)

    @staticmethod
    def add(title: str, abstract: str) -> Response:
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                category_id = Categories.get_next_id()

                cursor.execute(
                    """
                    INSERT INTO Categories (category_id, title, abstract)
                    VALUES (%s, %s, %s)
                    """,
                    [category_id, title, abstract],
                )

                conn.commit()

            return "", 201
        except Exception as e:
            return database_error(e)

    @staticmethod
    def delete(id: int) -> Response:
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    UPDATE Posts
                    SET category_id = NULL
                    WHERE category_id = (%s)
                    """,
                    [id],
                )

                cur.execute(
                    """
                    DELETE FROM Categories
                    WHERE category_id = (%s)
                    """,
                    [id],
                )

            conn.commit()

            return make_response("", 201)

        except Exception as e:
            return database_error(e)
