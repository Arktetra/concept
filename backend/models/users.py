from typing import Optional

from flask import jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.utils import database_error


class Users:
    """
    A class for handling interactions with the Users table in the
    database.
    """

    @staticmethod
    def get_id_from_email(email: str) -> int:
        """
        A function to get the user id from email.

        Returns:
            int: a user id.
        """

        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                if not Users.check_email_existence(email):
                    return jsonify({"error": "Invalid email"}), 401

                cursor.execute(
                    """
                    SELECT user_id FROM Users
                    WHERE email LIKE (%s)
                    """,
                    [email],
                )

                user_id = cursor.fetchone()[0]

            return user_id

        except Exception as e:
            return database_error(e)

    @staticmethod
    def get_email_from_id(id: int) -> Optional[str]:
        """
        A function to get the user email from user id.

        Returns:
            Optional[str]: user email
        """
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    SELECT email FROM Users
                    WHERE user_id = (%s)
                    """,
                    [id],
                )
                result = cur.fetchone()

            return result if result else None
        except Exception as e:
            return database_error(e)

    @staticmethod
    def check_email_existence(email: str) -> bool:
        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT 1 FROM Users
                    WHERE email = (%s)
                    """,
                    [email],
                )

                exists = cursor.fetchone()

                exists = True if exists else False

            return exists
        except Exception as e:
            return database_error(e)

    @staticmethod
    def get_next_id() -> int:
        """
        A function to get the user id for the new user.

        Returns:
            int: a user id.
        """

        try:
            conn = get_db()

            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                        SELECT MAX(user_id) FROM Users;
                        """
                )

                user_id = cursor.fetchone()
                user_id = user_id[0] + 1 if user_id[0] else 0

            return user_id
        except Exception as e:
            return database_error(e)

    @staticmethod
    def exists(ids: list[int]) -> bool:
        try:
            conn = get_db()
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(
                    """
                    SELECT user_id FROM Users
                    """
                )

                user_ids = cursor.fetchall()

            id_exists = True

            for user_id in ids:
                if user_id not in user_ids:
                    id_exists = False

            return id_exists

        except Exception as e:
            return database_error(e)
