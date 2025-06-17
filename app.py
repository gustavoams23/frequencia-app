import streamlit as st

disciplinas = {
    "Português": 120,
    "Matemática": 120,
    "História": 60,
    "Geografia": 60,
    "Ciências": 60,
    "Artes": 40,
    "Inglês": 40,
    "Ed. Física": 40
}

st.title("📊 Calculadora de Frequência Escolar")

disciplina = st.selectbox("Selecione a disciplina:", list(disciplinas.keys()))
faltas = st.number_input(f"Digite o número de faltas em {disciplina}:", min_value=0, step=1)

if st.button("Calcular Frequência"):
    total = disciplinas[disciplina]
    frequencia = (1 - faltas / total) * 100
    frequencia = max(0, frequencia)
    st.success(f"Frequência em {disciplina}: {frequencia:.2f}%")