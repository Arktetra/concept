from flask import Blueprint, Response, request

from backend.models.posts import Posts

bp = Blueprint("post", __name__, url_prefix="/posts")


@bp.route("/delete", methods=["POST"])
def delete_post() -> Response:
    return Posts.delete(request.json["post_id"])


@bp.route("/get", methods=["POST"])
def get_post() -> dict:
    if request.method == "POST":
        post_id = request.json["slug"]

        return Posts.get(post_id)


@bp.route("/comments", methods=["POST"])
def get_comments() -> Response:
    return Posts.get_comments(request.json["post_id"])
