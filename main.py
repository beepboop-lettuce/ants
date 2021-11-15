from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World!'}