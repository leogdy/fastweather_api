# 🌦 API de Previsão do Tempo

Bem-vindo à API de Previsão do Tempo! Este projeto fornece uma API para consultar previsões do tempo de uma cidade, utilizando dados do OpenWeatherMap e armazenando-os em um banco de dados PostgreSQL.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL (simulado com mock para testes)
- **ORM:** SQLAlchemy
- **API Externa:** OpenWeatherMap
- **Versionamento de Código:** Git (GitHub)
- **Ambiente Virtual:** Python Virtualenv
- **Testes:** Pytest, com mock do banco de dados

## 📌 Configuração do Projeto

### 1️⃣ Clonar o Repositório
Para começar, clone o repositório e navegue até o diretório do projeto:

```bash
git clone https://github.com/seu-usuario/fastweather_api.git
cd fastweather_api
```

### 2️⃣ Criar e Ativar o Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

No Windows:
```bash
venv\Scripts\activate
```

No macOS/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Instalar as Dependências
Instale as dependências necessárias utilizando o pip:

```bash
pip install -r requirements.txt
```

### 4️⃣ Criar o Arquivo .env
Crie um arquivo `.env` na raiz do projeto e adicione suas variáveis de configuração, incluindo a chave da API do OpenWeatherMap:

```ini
OPENWEATHER_API_KEY=SuaChaveAPI
```

> **Nota:** Como o banco de dados foi mockado para testes, não é necessário configurar um banco de dados real.

### 5️⃣ Executar o Servidor FastAPI
Com o ambiente configurado, execute o servidor FastAPI com o comando abaixo:

```bash
uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

## 📡 Endpoints Disponíveis

### 1️⃣ Criar uma previsão do tempo
- **Endpoint:** `POST /previsao/`
- **Exemplo de Payload:**

```json
{
  "cidade": "São Paulo"
}
```

- **Resposta Esperada:**

```json
{
  "id": 1,
  "cidade": "São Paulo",
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

## 🧪 Testando com o Pytest
Os testes são realizados utilizando o `pytest`. O banco de dados foi **mockado**, então **não é necessário configurar um banco de dados real** para rodar os testes.

Para executar os testes unitários:

```bash
pytest tests/
```

Isso executará os testes sem a necessidade de um banco de dados real, garantindo um processo de teste mais rápido e prático.

## 🔒 Segurança: Por Que Não Disponibilizei Minha Chave da API?
A chave da API do OpenWeatherMap **não** foi incluída no repositório público por motivos de segurança e boas práticas. Aqui estão os principais motivos:

- **Proteção das Credenciais:** Evita que terceiros usem a chave de forma indevida.
- **Boas Práticas:** Manter credenciais sensíveis fora do código-fonte.
- **Evitar Abuso de Recursos:** Evita consumo indevido da API, reduzindo riscos de custos inesperados.

### Como Configurar Sua Própria Chave de API
1. **Crie uma Conta na OpenWeatherMap** e obtenha sua chave de API.
2. **Configure a Chave no `.env`**:

```ini
OPENWEATHER_API_KEY=SuaChaveAPI
```

Essa abordagem garante a segurança da chave de API e a integridade do seu projeto.

## 🎨 Interface Web com Streamlit
Se você deseja visualizar as previsões de forma interativa, pode usar o `Streamlit` para criar uma interface gráfica simples. Basta rodar o seguinte comando:

```bash
streamlit run streamlit_app.py
```

Isso abrirá uma interface web em http://localhost:8501/, onde você poderá interagir com as previsões de maneira visual.

---

**Feito por Leonardo Godoy** ([GitHub](https://github.com/leogdy)) 🚀
