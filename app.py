import streamlit as st

# Título personalizado
st.title("Cálculo de porcentagem de frequência do Prof. Gustavo Abreu (EJA)")

# Lista de disciplinas disponíveis
disciplinas = [
    "Português", "Matemática", "História", "Geografia",
    "Ciências", "Artes", "Inglês", "Ed. Física"
]

# Escolha da disciplina
disciplina = st.selectbox("Selecione a disciplina:", disciplinas)

# Entrada do total de aulas dadas
total = st.number_input(f"Digite o total de aulas dadas em {disciplina}:", min_value=1)

# Entrada do número de faltas
faltas = st.number_input("Digite o número de faltas do aluno:", min_value=0)

# Calcular frequência
if st.button("Calcular frequência"):
    presencas = total - faltas
    frequencia = (presencas / total) * 100
    frequencia_arredondada = round(frequencia)
    st.success(f"Frequência em {disciplina}: {frequencia_arredondada}%")
