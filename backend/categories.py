from flask import Blueprint, request

from backend.models.categories import Categories

bp = Blueprint("category", __name__, url_prefix="/categories")


@bp.route("/get", methods=["POST"])
def get_concepts_from_category() -> list[dict]:
    if request.method == "POST":
        category_id = request.json["id"]
        print(category_id)

        return Categories.get(category_id)
