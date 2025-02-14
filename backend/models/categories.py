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
        try:
            conn = get_db()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                SELECT * FROM Categories
                WHERE category_id = (%s)
                """,
                    (id,),
                )
                category = cursor.fetchone()

            data = {
                "title": category["title"],
                "abstract": category["abstract"],
                "created at": category["created at"],
                "updated at": category["updated at"],
            }

            return jsonify(data)

        except Exception as e:
            print("Error: ", str(e))
            return jsonify({"error": "Database error"}), 500
