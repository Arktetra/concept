from database.connection import get_db_connection
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["POST"])
def login() -> dict:
    data = request.json
    email = data.get("email", "")
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT user_id, password FROM Users WHERE email = %s", (email,))
            User = cursor.fetchone()
    except Exception:
        return jsonify({"errror": "Database error"}), 500

    if not User:
        return jsonify({"error": "Invalid email or password"}), 401

    user_id, user_password = User
    if not check_password_hash(user_password, password):
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful", "user_id": user_id})
