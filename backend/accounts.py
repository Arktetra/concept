from flask import Blueprint, Response, request

from backend.models.accounts import AccountManager

bp = Blueprint("account", __name__, url_prefix="/accounts")


@bp.route("/login", methods=["POST"])
def login() -> Response:
    return AccountManager.login(email=request.json["email"], password=request.json["password"])


@bp.route("/register", methods=["POST"])
def register() -> Response:
    return AccountManager.register(
        user_name=request.json["user_name"],
        email=request.json["email"],
        password=request.json["password"],
        mobile=request.json["mobile"],
    )
