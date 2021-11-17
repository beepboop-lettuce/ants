from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Boolean, Column, Float, String, Integer 

app = FastAPI()

#SqlAlchemy Setup
DATABASE_URL = 'sqlite+pysqlite:///./db.sqlite3:'
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Returning a Database Object
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DBAnt(Base):
    __tablename__ = 'ants'

    id = Column(Integer, primary_key=True, index=True)
    domain = Column(String(50), nullable=True)
    kingdom = Column(String(50), nullable=True)
    phylum = Column(String(50), nullable=True)
    classs = Column(String(50), nullable=True)
    order = Column(String(50), nullable=True)
    family = Column(String(50), nullable=True)
    genus = Column(String(50), nullable=True)
    species = Column(String(50), nullable=True)

Base.metadata.create_all(bind=engine)

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

def get_ant(db: Session, ant_id: int):
    return db.query(DBAnt).where(DBAnt.id == ant_id).first()

def get_ants(db: Session):
    return db.query(DBAnt).all()

def create_ant(db: Session, ant: Ant):
    db_ant = DBAnt(**ant.dict())
    db.add(db_ant)
    db.commit()
    db.refresh(db_ant)

    return db_ant

@app.post('/ants/')
async def create_ant(ant: Ant):
    return ant


@app.get('/')
async def root():
    return {'message': 'Hello World!'}