import datetime
from pydantic import BaseModel, ConfigDict

# Modelo de entrada (POST)
class PrevisaoCreate(BaseModel):
    cidade: str

# Modelo de saída
class PrevisaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    cidade: str
    temperatura: float
    descricao: str
    data_consulta: datetime.datetime
