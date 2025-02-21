from flask import Response
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.utils import database_error


class Tags:
    """
    A class for handling interactions with the Tags relation in the
    database.
    """

    @staticmethod
    def get(id: int) -> Response:
        # this should be in posts?
        NotImplementedError

    @staticmethod
    def get_id(tag_name: str) -> int:
        """
        A function that returns the id of a tag given its tag name.

        Args:
            tag_name (str): name of a tag.

        Returns:
            int: id corresponding to the name of the tag.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT tag_id FROM Tags
                    WHERE tag_name = (%s)
                    """,
                    [tag_name],
                )

                tag_id = cursor.fetchone()[0]

            return tag_id
        except Exception as e:
            return database_error(e)

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the tag id for the new post.

        Returns:
            int: a tag id.
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT tag_id FROM Tags
                    ORDER BY tag_id DESC
                    LIMIT 1;
                    """
                )
                tag_id = cursor.fetchone()

                tag_id = tag_id[0] if tag_id else 0

            return tag_id + 1
        except Exception as e:
            return database_error(e)

    @staticmethod
    def add(tag_name: str) -> Response:
        try:
            conn = get_db()

            if Tags.check_tag_existence(tag_name):
                return "", 201

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    INSERT INTO Tags
                    VALUES
                        (%s, %s)
                    """,
                    [Tags.get_next_id(), tag_name],
                )

            conn.commit()

            return "", 201
        except Exception as e:
            return database_error(e)

    @staticmethod
    def check_tag_existence(tag_name: str) -> bool:
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT 1 FROM Tags
                    WHERE tag_name = (%s)
                    """,
                    [tag_name],
                )

                exists = cursor.fetchone()

            return True if exists else False
        except Exception as e:
            return database_error(e)
