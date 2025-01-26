from flask import Blueprint, Response, jsonify, redirect, request

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

        # return jsonify({"message": "Login successful", "user_id": user_id})
        return redirect("/"), 303


@auth_bp.route("/register", methods=["POST"])
def register() -> Response:
    if request.method == "POST":
        data = request.get_json()

        # Extract registration details
        user_name = data.get("user_name")
        email = data.get("email")
        password = data.get("password")
        mobile = data.get("mobile")
        role = data.get("role", "user")  # Default role is 'user'

        # Validate required fields
        if not user_name or not email or not password:
            return jsonify({"error": "Missing required fields"}), 400

        conn = get_db()
        try:
            with conn.cursor() as cursor:
                # Check if email already exists
                cursor.execute("SELECT email FROM Users WHERE email = (%s)", (email,))
                existing_user = cursor.fetchone()

                if existing_user:
                    return jsonify({"error": "Email already exists"}), 409

                # Insert new user into database
                cursor.execute(
                    """
                    INSERT INTO Users (user_name, email, password, mobile, role)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (user_name, email, password, mobile, role),
                )
                conn.commit()
        except Exception as e:
            print("Error: ", str(e))
            return jsonify({"error": "Database error"}), 500

        return jsonify({"message": "Registration successful"}), 201
