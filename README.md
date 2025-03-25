# 🌦 API de Previsão do Tempo

Bem-vindo! Esta API permite buscar previsões do tempo de uma cidade usando dados da OpenWeatherMap e armazená-los em um banco de dados.

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Framework:** FastAPI  
- **Banco de Dados:** SQLite/PostgreSQL  
- **ORM:** SQLAlchemy  
- **API Externa:** OpenWeatherMap  
- **Versionamento:** Git  

---

## 📌 Configuração do Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/fastweather_api.git
cd dev_jr_test-main
```

### 2️⃣ Criar e Ativar Ambiente Virtual
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Criar o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione:
```ini
DATABASE_URL=postgresql://postgres:852456@localhost:5432/previsao
OPENWEATHER_API_KEY=SuaChaveAPI
```

### 5️⃣ Executar o Servidor FastAPI
```bash
uvicorn main:app --reload
```
A API estará rodando em: `http://127.0.0.1:8000`

---

## 📡 Endpoints Disponíveis

### 1️⃣ Criar uma previsão do tempo
- **Endpoint:** `POST /previsao/`
- **Exemplo de Payload:**
```json
{
  "cidade": "Sao Paulo"
}
```
- **Resposta esperada:**
```json
{
  "id": 1,
  "cidade": "Sao Paulo",
  "temperatura": 25.5,
  "descricao": "Céu limpo",
  "data_consulta": "2024-03-20T12:00:00"
}
```

### 2️⃣ Listar todas as previsões
- **Endpoint:** `GET /previsao/`

### 3️⃣ Buscar previsão por cidade e data
- **Endpoint:** `GET /previsao?cidade=Sao Paulo&data=2024-03-20`

### 4️⃣ Excluir uma previsão
- **Endpoint:** `DELETE /previsao/{id}`

---

## 🧪 Testando com o Postman

1. Abra o Postman e crie uma nova requisição.
2. Defina o **método HTTP** (POST, GET, DELETE).
3. Insira a **URL**: `http://127.0.0.1:8000/previsao/`
4. Para `POST`, adicione o **corpo da requisição** em formato JSON.
5. Clique em **Send** e veja a resposta.

---

## 🎨 Interface Web com Streamlit
Caso queira visualizar as previsões via interface web:
```bash
streamlit run streamlit_app.py
```
Acesse `http://localhost:8501/` para interagir.

---

Feito por Leonardo (https://github.com/leogdy) 🚀
