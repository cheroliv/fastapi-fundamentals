import json
from datetime import datetime
from fastapi import FastAPI

from fastapi.testclient import TestClient


canary = FastAPI()

client = TestClient(canary)


@canary.get("/")
def welcome():
    """Return a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service!"}


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text


@canary.get("/date")
def date():
    """Return the current date/time."""
    return {'date': datetime.now()}


def test_date():
    response = client.get("/date")
    assert response.status_code == 200
    # without exception it asserts date is a valid format
    datetime.fromisoformat(json.loads(response.text)["date"])


# request parameter
# localhost:8000/greeting/?name=John
@canary.get("/greeting")
def welcome(name):
    """Return a friendly welcome message."""
    return {"message": f'Hi {name}. Welcome to the Car Sharing service!'}


def test_greeting_with_query_param():
    name = "John"
    expected = f"Hi {name}. Welcome to the Car Sharing service!"
    response = client.get(f"/greeting/?name={name}")
    result = json.loads(response.text)[
        "message"]
    assert response.status_code == 200
    assert expected in result
