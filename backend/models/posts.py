from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db


class Posts:
    """
    A class for handling interactions with the Posts table in the
    database.
    """

    @staticmethod
    def get(id: int) -> Response:
        try:
            conn = get_db()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Posts
                    WHERE post_id = (%s)
                    """,
                    (id,),
                )
                post = cursor.fetchone()

            data = {
                "title": post["title"],
                "abstract": post["abstract"],
                "content": post["content"],
                "created_at": post["created_at"],
                "updated_at": post["updated_at"],
            }
            return jsonify(data)

        except Exception as e:
            print("Error: ", str(e))
            return jsonify({"error": "Database error"}), 500
