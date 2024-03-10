from flask import Blueprint
from app.models.Image import Image, ImageSchema

img_bp = Blueprint("images", __name__)


@img_bp.route("/images")
def hello_world():
    imageSchema = ImageSchema()
    images = Image.query.all()
    return imageSchema.dump(images, many=True)
