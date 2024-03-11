import pytest
from app import create_app
from app.extensions import db
from app.models.Image import Image


@pytest.fixture()
def app():
    app = create_app("testing")

    with app.app_context():
        db.create_all()
        img = Image("test.png", "image/png")
        db.session.add(img)
        db.session.commit()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
