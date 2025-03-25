import streamlit as st
import requests

st.title("Consulta de Previsão do Tempo")

cidade = st.text_input("Digite o nome da cidade:")

if st.button("Buscar Previsão"):
    if cidade:
        response = requests.post("http://localhost:8000/previsao/", json={"cidade": cidade})
        if response.status_code == 200:
            data = response.json()
            st.write("**Cidade:**", data["cidade"])
            st.write("**Temperatura:**", data["temperatura"], "°C")
            st.write("**Descrição:**", data["descricao"])
            st.write("**Data da consulta:**", data["data_consulta"])
        else:
            st.error("Erro ao buscar previsão. Verifique a cidade ou a API.")
    else:
        st.warning("Por favor, insira o nome de uma cidade.")
