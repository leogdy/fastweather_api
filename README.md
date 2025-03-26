API de Previsão do Tempo
Bem-vindo à API de Previsão do Tempo! Este projeto fornece uma API para consultar previsões do tempo de uma cidade, utilizando dados do OpenWeatherMap e armazenando-os em um banco de dados PostgreSQL.

🚀 Tecnologias Utilizadas
Linguagem: Python 3.x

Framework: FastAPI

Banco de Dados: PostgreSQL (banco de dados de produção e de teste)

ORM: SQLAlchemy

API Externa: OpenWeatherMap

Versionamento de Código: Git (GitHub)

Ambiente Virtual: Python Virtualenv

Testes: Pytest, com mock do banco de dados para testes

📌 Configuração do Projeto
1️⃣ Clonar o Repositório
Para começar, clone o repositório e navegue até o diretório do projeto:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/fastweather_api.git
cd fastweather_api
2️⃣ Criar e Ativar o Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências do projeto:

bash
Copiar
Editar
python -m venv venv
# No Windows
venv\Scripts\activate
# No macOS/Linux
source venv/bin/activate
3️⃣ Instalar as Dependências
Instale as dependências necessárias utilizando o pip:

bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Criar o Arquivo .env
Crie um arquivo .env na raiz do projeto e adicione suas variáveis de configuração, incluindo a chave da API do OpenWeatherMap:

ini
Copiar
Editar
DATABASE_URL=postgresql://postgres:852456@localhost:5432/previsao
DATABASE_URL_TEST=postgresql://postgres:852456@localhost:5432/test_previsao
OPENWEATHER_API_KEY=SuaChaveAPI
Importante: A chave da API do OpenWeatherMap não foi disponibilizada no repositório por questões de segurança, como explicado mais adiante.

5️⃣ Executar o Servidor FastAPI
Com o ambiente configurado, execute o servidor FastAPI com o comando abaixo:

bash
Copiar
Editar
uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

📡 Endpoints Disponíveis
1️⃣ Criar uma previsão do tempo
Endpoint: POST /previsao/

Exemplo de Payload:

json
Copiar
Editar
{
  "cidade": "São Paulo"
}
Resposta Esperada:

json
Copiar
Editar
{
  "id": 1,
  "cidade": "São Paulo",
  "temperatura": 25.5,
  "descricao": "Céu limpo",
  "data_consulta": "2024-03-20T12:00:00"
}
2️⃣ Listar todas as previsões
Endpoint: GET /previsao/

3️⃣ Buscar previsão por cidade e data
Endpoint: GET /previsao?cidade=Sao Paulo&data=2024-03-20

4️⃣ Excluir uma previsão
Endpoint: DELETE /previsao/{id}

🧪 Testando com o Pytest
Os testes são realizados utilizando o pytest. O banco de dados foi mockado para evitar a necessidade de os usuários configurarem um banco de dados local, tornando o processo de teste mais rápido e fácil.

Testes
Para executar os testes unitários:

bash
Copiar
Editar
pytest tests/
Isso irá executar os testes sem a necessidade de um banco de dados real, já que o banco de dados foi mockado para os testes, permitindo que você se concentre na lógica da aplicação sem configurações adicionais.

🔒 Por Que Não Disponibilizei Minha Chave da API?
A chave da API do OpenWeatherMap não foi incluída no repositório público por motivos de segurança e boas práticas. Aqui estão os principais motivos:

Proteção das Credenciais: As chaves de API são informações privadas e devem ser mantidas seguras. Expor a chave publicamente pode permitir que outros usuários usem a chave de forma inadequada, o que pode gerar custos inesperados ou impactar a integridade do serviço.

Boas Práticas de Segurança: Em ambientes de desenvolvimento, é uma prática recomendada manter credenciais sensíveis, como chaves de API, fora do código-fonte. Utilizando variáveis de ambiente ou arquivos .env, conseguimos manter essas credenciais seguras e evitar que sejam expostas em repositórios públicos.

Evitar Abuso de Recursos: Se a chave da API for publicada, qualquer pessoa pode utilizá-la, o que pode gerar um uso excessivo da API e, consequentemente, custos inesperados para o proprietário da chave.

Como Configurar Sua Própria Chave de API
Crie uma Conta na OpenWeatherMap:
Acesse o OpenWeatherMap e crie uma conta. Após o cadastro, você poderá acessar sua chave de API.

Configure a Chave no .env:
Após obter a chave, crie o arquivo .env na raiz do projeto (se ainda não existir) e adicione a chave da API da seguinte forma:

ini
Copiar
Editar
OPENWEATHER_API_KEY=SuaChaveAPI
Essa abordagem garante a segurança da chave de API e a integridade do seu projeto.

🎨 Interface Web com Streamlit
Se você deseja visualizar as previsões de forma interativa, pode usar o Streamlit para criar uma interface gráfica simples. Basta rodar o seguinte comando:

bash
Copiar
Editar
streamlit run streamlit_app.py
Isso abrirá uma interface web em http://localhost:8501/, onde você poderá interagir com as previsões de maneira visual.

Feito por Leonardo Godoy (https://github.com/leogdy) 🚀
