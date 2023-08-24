from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException


if __name__ == "__main__":
    uvicorn.run('carsharing:app', reload=True)

app = FastAPI()


@app.get("/api/cars")
def get_cars(size: Optional[str] = None, doors: Optional[int] = None) -> List:
    result = data.db
    if size:
        result = [car for car in result if car['size'] == size]
    if doors:
        result = [car for car in result if car['doors'] >= doors]
    return result


@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in data.db if car['id'] == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
