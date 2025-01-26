from datetime import datetime

from app.extensions import db
from app.extensions import ma


class Image(db.Model):
    """Image entity"""

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(60), nullable=False)
    _hash = db.Column(db.String(60), nullable=False)
    content_type = db.Column(db.String(60), nullable=False)
    create_date = db.Column(
        db.DateTime(timezone=True),
    )
    edit_date = db.Column(db.DateTime(timezone=True), nullable=True)
    deleted = db.Column(db.Boolean, default=True)

    def __init__(self, path, content_type) -> None:
        super().__init__()
        self.path = path
        self.content_type = content_type
        self._hash = ""
        self.create_date = datetime.now()
        self.edit_date = None
        self.deleted = False


class ImageSchema(ma.SQLAlchemySchema):
    """Image Schema"""

    class Meta:
        """Meta class"""

        model = Image

    id = ma.auto_field()
    path = ma.auto_field()
    _hash = ma.auto_field()
    content_type = ma.auto_field()
    create_date = ma.auto_field()
    edit_date = ma.auto_field()
    deleted = ma.auto_field()
