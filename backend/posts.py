from flask import Blueprint, request

from backend.models.posts import Posts

bp = Blueprint("concept", __name__, url_prefix="/blog/posts")


@bp.route("/get", methods=["POST"])
def get_concept() -> dict:
    if request.method == "POST":
        post_id = request.json["slug"]

        return Posts.get(post_id)
