from flask import Blueprint, Response, request

from backend.models.categories import Categories

bp = Blueprint("category", __name__, url_prefix="/categories")


@bp.route("/get", methods=["POST"])
def get_concepts_from_category() -> list[dict]:
    if request.method == "POST":
        category_id = request.json["id"]

        return Categories.get(category_id)


@bp.route("/delete", methods=["POST"])
def delete_category() -> Response:
    return Categories.delete(request.json["category_id"])
