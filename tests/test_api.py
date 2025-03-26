import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.config.database import SessionLocal, engine
from app.model.previsao_entity import Base
from app.main import app, get_db

load_dotenv()

DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST", "postgresql://postgres:852456@localhost:5432/test_previsao")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

engine_test = create_engine(DATABASE_URL_TEST)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

Base.metadata.create_all(bind=engine_test)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_criar_previsao():
    response = client.post("/previsao/", json={"cidade": "São Paulo"})
    assert response.status_code == 200
    data = response.json()
    assert data["cidade"] == "São Paulo"
    assert "temperatura" in data
    assert "descricao" in data
