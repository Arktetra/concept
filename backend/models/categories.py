from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db


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

    # except Exception as e:
    #     print("Error: ", str(e))
    #     return jsonify({"error": "Database error"}), 500
