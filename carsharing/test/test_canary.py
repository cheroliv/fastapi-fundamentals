from fastapi.testclient import TestClient

from carsharing import app

from datetime import datetime

import json

client = TestClient(app)


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text


def test_date():
    response = client.get("/date")
    assert response.status_code == 200
    # without exception it asserts date is a valid format
    datetime.fromisoformat(json.loads(response.text)["date"])


def test_greeting():
    name = "John"
    response = client.get(f"/greeting/?name={name}")
    assert response.status_code == 200
    assert f"Hi {name}. Welcome to the Car Sharing service!" in json.loads(response.text)[
        "message"]
