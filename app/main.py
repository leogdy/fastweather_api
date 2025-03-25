from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import engine, SessionLocal
from app.models import Base
from app.schemas import PrevisaoCreate, PrevisaoResponse
from app import crud

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Previsão do Tempo")

# Dependência para criar e fechar sessão de banco em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint POST: cria uma previsão
@app.post("/previsao/", response_model=PrevisaoResponse)
def criar_previsao(previsao_create: PrevisaoCreate, db: Session = Depends(get_db)):
    return crud.criar_previsao(db, previsao_create)

# Endpoint GET: lista previsões com filtros
@app.get("/previsao/", response_model=list[PrevisaoResponse])
def listar_previsoes(
    cidade: str = Query(None),
    data: str = Query(None),
    db: Session = Depends(get_db)
):
    return crud.listar_previsoes(db, cidade, data)

# Endpoint DELETE: exclui previsão por ID
@app.delete("/previsao/{id}", response_model=dict)
def excluir_previsao(id: int, db: Session = Depends(get_db)):
    return crud.excluir_previsao(db, id)
