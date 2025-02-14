from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db


class Concepts:
    @staticmethod
    def get() -> Response:
        """
        A function to get all the concepts from the database. Concepts here
        means all the posts which are not in a category, and all the categories.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT * FROM (
                        SELECT post_id, title, abstract, created_at, updated_at, 'posts' AS type
                            FROM Posts
                        WHERE category_id IS NULL
                        UNION
                        SELECT category_id, title, abstract, created_at, updated_at, 'categories'
                            AS type FROM Categories
                    )
                    ORDER BY created_at ASC;
                    """
                )
                concepts = cursor.fetchall()

            data = []

            for concept in concepts:
                data.append(
                    {
                        "id": concept[0],
                        "title": concept["title"],
                        "abstract": concept["abstract"],
                        "created_at": concept["created_at"],
                        "updated_at": concept["updated_at"],
                        "type": concept["type"],
                    }
                )

            return jsonify(data)

        except Exception as e:
            print("Error: ", str(e))
            return jsonify({"error": "Database error"}), 500
