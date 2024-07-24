import json


def test_get_images(client):
    response = client.get("/api/images")
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert isinstance(res, (list, dict))


def test_get_image_by_id(client):
    response = client.get("/api/image/101")
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 404
    assert isinstance(res, (list, dict))
    assert "error" in res
