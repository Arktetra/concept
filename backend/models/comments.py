from typing import Dict

from flask import Response
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.utils import database_error


class Comments:
    """
    A class for handling interactions with the Comments table in the
    database.
    """

    @staticmethod
    def get(comment_id: int) -> Dict[str, str]:
        """
        A function that returns the user id, comment text, and the time
        at which the comment was created at.

        Args:
            comment_id (int): id of tge comment.

        Returns:
            Dict[str, str]: A dictionary with "user_id", "comment_text",
            "created_at" keys and their corresponding values.
        """
        raise NotImplementedError

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the comment id for the new comment.

        Returns:
            int: comment id for the next comment.
        """

        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    SELECT comment_id FROM Comments
                    ORDER BY comment_id DESC
                    LIMIT 1;
                    """
                )
                comment_id = cur.fetchone()
                comment_id = comment_id[0] if comment_id else 0

            return comment_id + 1
        except Exception as e:
            return database_error(e)

    @staticmethod
    def add(post_id: int, user_id: int, comment_text: str) -> Response:
        """
        A function to add a comment to the Comments relation.

        Args:
            post_id (int): id of the post.
            user_id (int): id of the user.
            comment_text (str): comment.

        Returns:
            Response: success or failure.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    INSERT INTO Comments (comment_id, post_id, user_id, comment_text)
                    VALUES
                        (%s, %s, %s, %s)
                    """,
                    [Comments.get_next_id(), post_id, user_id, comment_text],
                )

            conn.commit()

            return "", 201

        except Exception as e:
            return database_error(e)
