from flask import Blueprint, request, jsonify
from app.models.Image import Image, ImageSchema
from app.utils import file_handler

img_bp = Blueprint("images", __name__)


@img_bp.route("/images", methods=["GET", "POST"])
def hello_world():
    imageSchema = ImageSchema()
    if request.method == "GET":
        images = Image.query.all()
        return imageSchema.dump(images, many=True)
    elif request.method == "POST":
        try:
            # Check if the POST request has the file part
            if "file" not in request.files:
                return {"error": "No file part"}, 400

            _file = request.files["file"]
            result = file_handler.upload_file(_file)
            return result
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {e}"}), 500
