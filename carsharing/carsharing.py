from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def welcome():
    """Return a friendly welcome message."""
    return {'message': "Welcome to the Car Sharing service!"}


@app.get("/date")
def date():
    """Return the current date/time."""
    return {'date': datetime.now()}
