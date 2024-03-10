import io
from flask import Blueprint, request, jsonify, send_file
from app.models.Image import Image, ImageSchema
from app.utils import file_handler
from app.extensions import db

img_bp = Blueprint("images", __name__)
imageSchema = ImageSchema()


@img_bp.route("/images", methods=["GET", "POST"])
def images():
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
            if result.success:
                img = Image(result.data["name"], _file.content_type)
                db.session.add(img)
                db.session.commit()
                return {"message": result.status, "image": imageSchema.dump(img)}, 201
            else:
                return {"error": result.status}, 501
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {e}"}), 500


@img_bp.route("/image/<int:id>", methods=["GET"])
def getImage(id):
    print(id)
    img = Image.query.get(id)
    if img is None:
        return jsonify({"error": "image not found"}), 404

    img_data = file_handler.download_file(img.path)

    return send_file(
        io.BytesIO(img_data.data.read()),
        download_name=img.path,
        mimetype=img.content_type,
    )
