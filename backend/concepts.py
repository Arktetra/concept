from flask import Blueprint, request

from backend.models.concepts import Concepts

bp = Blueprint("concept", __name__, url_prefix="/concepts")


@bp.route("/get", methods=["GET"])
def get_concepts() -> list[dict]:
    return Concepts.get()


@bp.route("/add", methods=["POST"])
def add_concepts() -> None:
    if request.method == "POST":
        title = request.json["title"]
        abstract = request.json["abstract"]
        content = request.json["content"]
        print(title)
        print(abstract)
        print(content)
