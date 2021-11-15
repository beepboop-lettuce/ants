from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Ant(BaseModel):
    domain: str
    kingdom: str
    phylum: str
    classs: str
    order: str
    family: str
    genus: str
    species: str

    class Config:
        orm_mode = True

@app.post('/ants/')
async def create_ant_view(ant: Ant):
    return ant


@app.get('/')
async def root():
    return {'message': 'Hello World!'}