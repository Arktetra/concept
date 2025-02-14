from flask import Blueprint

from backend.models.concepts import Concepts

bp = Blueprint("concept", __name__, url_prefix="/concepts")


@bp.route("/get", methods=["GET"])
def get_concepts() -> list[dict]:
    return Concepts.get()
