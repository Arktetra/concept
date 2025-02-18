from flask import Response, jsonify
from werkzeug.security import generate_password_hash


def hash_password(password: str) -> str:
    return generate_password_hash(password)


def database_error(error: str) -> Response:
    # print("Error: ", str(error))
    raise Exception(error)
    return jsonify({"error": "Database error"}), 500
