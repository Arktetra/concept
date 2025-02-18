from flask import Blueprint, request

from backend.models.concepts import Concepts
from backend.models.users import Users

bp = Blueprint("concept", __name__, url_prefix="/concepts")


@bp.route("/get", methods=["GET"])
def get_concepts() -> list[dict]:
    return Concepts.get()


@bp.route("/add", methods=["POST"])
def add_concepts() -> None:
    if request.method == "POST":
        author_emails = request.json["author_emails"]

        author_ids = [Users.get_id_from_email(email) for email in author_emails]

        return Concepts.add(
            title=request.json["title"],
            abstract=request.json["abstract"],
            content=request.json["content"],
            author_ids=author_ids,
            concept_type=request.json["type"],
        )
