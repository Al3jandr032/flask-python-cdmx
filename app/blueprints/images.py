"""
Images Blueprint definition
process images and apply filters
"""

import io
from flask import Blueprint, request, jsonify, send_file

from app.models.image import Image, ImageSchema
from app.utils import file_handler
from app.extensions import db
from app.utils.image_processor_factory import ImageProcessorFactory

PROCESSOR_TYPE = "PIL"
img_bp = Blueprint("images", __name__)
imageSchema = ImageSchema()
processor = ImageProcessorFactory.create_processor(PROCESSOR_TYPE)


@img_bp.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        _images = Image.query.all()
        return imageSchema.dump(_images, many=True)
    # POST handle logic
    try:
        # Check if the POST request has the file part
        if "file" not in request.files:
            return {"error": "No file part"}, 400

        _file = request.files["file"]
        result = file_handler.upload_file(_file)
        if result.success:
            img = Image(result.data["name"], _file.content_type)
            db.session.add(img)
            db.session.commit()
            return {"message": result.status, "image": imageSchema.dump(img)}, 201
        return {"error": result.status}, 501
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


@img_bp.route("/image/<int:_id>", methods=["GET"])
def get_image(_id):
    print(_id)
    img = Image.query.get(_id)
    if img is None:
        return jsonify({"error": "image not found"}), 404

    img_data = file_handler.download_file(img.path)

    return send_file(
        io.BytesIO(img_data.data.read()),
        download_name=img.path,
        mimetype=img.content_type,
    )


@img_bp.route("/image/<int:_id>/filter/<_filter>", methods=["GET"])
def filter_image(_id, _filter):
    allow_filters = ImageProcessorFactory.get_filters()
    if _filter not in allow_filters:
        return (
            jsonify(
                {"error": f"invalid filter {_filter} allow values {allow_filters}"}
            ),
            400,
        )
    img = Image.query.get(_id)
    if img is None:
        return jsonify({"error": "image not found"}), 404
    print(f"Apply filter {_filter} to image {_id}")
    img_data = file_handler.download_file(img.path)
    processor.load_image(img_data.data)
    processor.apply_filter(_filter)
    img_bytes = processor.save_image()

    return send_file(
        io.BytesIO(img_bytes),
        download_name=img.path,
        mimetype=img.content_type,
    )
