import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from app.database import SessionLocal, engine
from app.models import Base
from app.main import app, get_db

load_dotenv()

# Banco de testes
DATABASE_URL_TEST = os.getenv("DATABASE_URL_TEST", "postgresql://postgres:852456@localhost:5432/test_previsao")

# Cria um engine para o banco de testes
engine_test = create_engine(DATABASE_URL_TEST)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Cria as tabelas no banco de testes
Base.metadata.create_all(bind=engine_test)

# Override da dependência get_db para usar o banco de teste
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
