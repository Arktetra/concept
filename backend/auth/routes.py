from flask import Blueprint, jsonify, redirect, request

from backend.db import get_db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login() -> dict:
    if request.method == "POST":
        email = request.json["email"]
        password = request.json["password"]

        conn = get_db()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT user_id, password FROM Users WHERE email = (%s)", (email,))
                user = cursor.fetchone()
        except Exception as e:
            print("Error: ", str(e))
            return jsonify({"errror": "Database error"}), 500

        user_id, user_password = user

        if user is None:
            return jsonify({"error": "Invalid email"}), 401
        elif user_password != password:
            return jsonify({"error": "Invalid email or password"}), 401

        return redirect("/home"), 303
