import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

Base = declarative_base()

class Previsao(Base):
    __tablename__ = "previsoes"
    id = Column(Integer, primary_key=True, index=True)
    cidade = Column(String, index=True)
    temperatura = Column(Float)
    descricao = Column(String)
    data_consulta = Column(DateTime, default=datetime.datetime.utcnow)
