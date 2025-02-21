from flask import Blueprint, Response, request

from backend.models.comments import Comments
from backend.models.users import Users

bp = Blueprint("comment", __name__, url_prefix="/comments")


@bp.route("/add", methods=["POST"])
def add_comment() -> Response:
    post_id = request.json["post_id"]
    user_id = Users.get_id_from_email(request.json["email"])
    comment = request.json["comment"]

    return Comments.add(post_id, user_id, comment)
