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
            print(posts)

        data = []

        for post in posts:
            print(f"category id: {post['category_id']}")
            data.append(
                {
                    "id": post[0],
                    "title": post["title"],
                    "abstract": post["abstract"],
                    "created_at": post["created_at"],
                    "updated_at": post["updated_at"],
                    "type": post["type"],
                }
            )

        print(data)

        return jsonify(data)

    # except Exception as e:
    #     print("Error: ", str(e))
    #     return jsonify({"error": "Database error"}), 500
