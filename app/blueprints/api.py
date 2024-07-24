from flask import Blueprint


api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@api_bp.route("/version")
def exampleDict():
    return {"name": "flask", "version": 3}


@api_bp.route("/test")
def test():
    return "Exito", 201


@api_bp.route("/headers")
def headers():
    return {"status": False}, 404, {"custom": "flask"}
