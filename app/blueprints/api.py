"""
Api Blueprint definition
Simple endpoints that show different
return types
"""

from flask import Blueprint

api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def hello_world():
    """hello world get example"""
    return "<p>Hello, World!</p>"


@api_bp.route("/version")
def example_dict():
    """path get example"""
    return {"name": "flask", "version": 3}


@api_bp.route("/test")
def test():
    """Tuple as return value"""
    return "Exito", 201


@api_bp.route("/headers")
def headers():
    """Endpoint that return headers custom"""
    return {"status": False}, 404, {"custom": "flask"}
