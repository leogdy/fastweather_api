import datetime
import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.previsao_entity import Previsao
from app.dto.previsao_dto import PrevisaoCreate
from dotenv import load_dotenv
import os

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "a0d572785334d53b9353094b337283e3")

def buscar_previsao(cidade: str):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={cidade}"
        f"&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt_br"
    )
    resposta = requests.get(url)
    if resposta.status_code != 200:
        raise HTTPException(status_code=404, detail="Cidade não encontrada ou erro na API externa")

    dados = resposta.json()
    try:
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        data_consulta = datetime.datetime.fromtimestamp(dados["dt"], datetime.timezone.utc)
    except KeyError:
        raise HTTPException(status_code=500, detail="Erro ao processar dados da API externa")

    return {
        "cidade": cidade,
        "temperatura": dados["main"]["temp"],
        "descricao": dados["weather"][0]["description"],
        "data_consulta": datetime.datetime.fromtimestamp(dados["dt"], datetime.timezone.utc)
    }

def criar_previsao(db: Session, previsao_data: PrevisaoCreate):
    dados = buscar_previsao(previsao_data.cidade)
    nova_previsao = Previsao(**dados)
    db.add(nova_previsao)
    db.commit()
    db.refresh(nova_previsao)
    return nova_previsao

def listar_previsoes(db: Session, cidade: str = None, data: str = None):
    query = db.query(Previsao)
    if cidade:
        query = query.filter(Previsao.cidade.ilike(f"%{cidade}%"))
    if data:
        try:
            data_obj = datetime.datetime.strptime(data, "%Y-%m-%d")
            proximo_dia = data_obj + datetime.timedelta(days=1)
            query = query.filter(Previsao.data_consulta >= data_obj, Previsao.data_consulta < proximo_dia)
        except ValueError:
            raise HTTPException(status_code=400, detail="Formato de data inválido. Utilize YYYY-MM-DD")
    return query.all()

def excluir_previsao(db: Session, previsao_id: int):
    previsao = db.query(Previsao).filter(Previsao.id == previsao_id).first()
    if not previsao:
        raise HTTPException(status_code=404, detail="Previsão não encontrada")
    db.delete(previsao)
    db.commit()
    return {"detail": "Previsão excluída com sucesso"}
