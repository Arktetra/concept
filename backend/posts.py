from flask import Blueprint, request

from backend.models.posts import Posts

bp = Blueprint("post", __name__, url_prefix="/posts")


@bp.route("/get", methods=["POST"])
def get_post() -> dict:
    if request.method == "POST":
        post_id = request.json["slug"]

        return Posts.get(post_id)
