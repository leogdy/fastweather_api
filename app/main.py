from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.config.database import engine, SessionLocal
from app.model.previsao_entity import Base
from app.dto.previsao_dto import PrevisaoCreate, PrevisaoResponse
from app.repository import previsao_repository

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Previsão do Tempo")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/previsao/", response_model=PrevisaoResponse)
def criar_previsao(previsao_create: PrevisaoCreate, db: Session = Depends(get_db)):
    return previsao_repository.criar_previsao(db, previsao_create)

@app.get("/previsao/", response_model=list[PrevisaoResponse])
def listar_previsoes(
    cidade: str = Query(None),
    data: str = Query(None),
    db: Session = Depends(get_db)
):
    return previsao_repository.listar_previsoes(db, cidade, data)

@app.delete("/previsao/{id}", response_model=dict)
def excluir_previsao(id: int, db: Session = Depends(get_db)):
    return previsao_repository.excluir_previsao(db, id)
