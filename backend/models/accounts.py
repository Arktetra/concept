from typing import Optional

from flask import Response, jsonify
from psycopg2.extras import DictCursor

from backend.db import get_db
from backend.models.users import Users
from backend.utils import database_error


class AccountManager:
    """
    A class for managing user accounts.
    """

    @staticmethod
    def register(user_name: str, email: str, password: str, mobile: Optional[str]) -> Response:
        try:
            conn = get_db()

            with conn.cursor() as cursor:
                if AccountManager.check_email_existence(email):
                    return jsonify({"error": "Email already exists"}), 409

                cursor.execute(
                    """
                    INSERT INTO Users (user_id, user_name, email, password, mobile)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    [Users.get_next_id(), user_name, email, password, mobile],
                )

                conn.commit()

                return "", 201

        except Exception as e:
            database_error(e)

    @staticmethod
    def login(email: str, password: str) -> Response:
        try:
            conn = get_db()

            with conn.cursor() as cursor:
                if not AccountManager.check_email_existence(email):
                    return jsonify({"error": "Invalid Email."}), 401

                cursor.execute(
                    """
                    SELECT password FROM Users
                    WHERE email = (%s)
                    """,
                    [email],
                )

                actual_password = cursor.fetchone()[0]

                if actual_password != password:
                    return jsonify({"error": "Invalid Password."}), 401
                else:
                    return "", 201

        except Exception as e:
            database_error(e)

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
