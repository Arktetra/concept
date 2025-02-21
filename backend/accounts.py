from flask import Blueprint, Response, make_response, request

from backend.models.accounts import AccountManager
from backend.models.users import Users

bp = Blueprint("account", __name__, url_prefix="/accounts")


@bp.route("/login", methods=["POST"])
def login() -> Response:
    email = request.json["email"]
    user_id = Users.get_id_from_email(email)
    res = AccountManager.login(email=email, password=request.json["password"])
    res.set_cookie("email", email)
    res.set_cookie("name", Users.get_user_name(user_id)[0])
    return res


@bp.route("/logout", methods=["GET"])
def logout() -> Response:
    res = make_response("")
    res.set_cookie("email", "")
    res.set_cookie("name", "")
    return res


@bp.route("/register", methods=["POST"])
def register() -> Response:
    email = request.json["email"]
    user_name = request.json["user_name"]
    res = AccountManager.register(
        user_name=user_name,
        email=email,
        password=request.json["password"],
        mobile=request.json["mobile"],
    )
    res.set_cookie("email", email)
    res.set_cookie("name", user_name)
    return res
