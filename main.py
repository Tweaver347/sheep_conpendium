from fastapi import FastAPI, HTTPException, status
from typing import List
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def get_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def create_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code = 400, detail = "Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sheep not found")
    del db.data[id]
    return

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, updated_sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sheep not found")
    db.data[id] = updated_sheep
    return updated_sheep

@app.get("/sheep", response_model=List[Sheep])
def get_all_sheep():
    return list(db.data.values())