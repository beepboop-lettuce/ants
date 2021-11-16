from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer 

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
async def create_ant(ant: Ant):
    return ant


@app.get('/')
async def root():
    return {'message': 'Hello World!'}