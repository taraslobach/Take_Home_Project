import pytest
import requests

from config import base_url


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(user_id):
    url = base_url + f"{user_id}"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


def test_create_and_delete_user():
    data = {
        "name": "Taras Lobach",
        "job": "QA Engineer"
    }
    response = requests.post(base_url, json=data)

    assert response.status_code == 201
    user_id = response.json()["id"]

    url = base_url + f"{user_id}"
    response = requests.delete(url)

    assert response.status_code == 204
    assert response.text == ""


def test_update_user():
    user_id = 1
    url = base_url + f"{user_id}"
    data = {
        "name": "Taras Lobach",
        "job": "Developer"
    }
    response = requests.put(url, json=data)

    assert response.status_code == 200
    assert response.json()["name"] == data["name"]
    assert response.json()["job"] == data["job"]
