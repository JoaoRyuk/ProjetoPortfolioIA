# paginas/dashboard.py
import streamlit as st

def mostrar(dados):
    """Mostra o dashboard com gráficos e estatísticas"""
    st.header("Estatisticas do Mundo Digital")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Digimons", len(dados))
    with col2:
        estagios = dados['Stage'].value_counts()
        st.metric("Estagios", len(estagios))
    with col3:
        st.metric("Ataque Medio", int(dados['ATK lvl 50'].mean()))
    with col4:
        st.metric("Velocidade Media", int(dados['SPD lvl 50'].mean()))
    
    st.subheader("Distribuicao por Estagio")
    st.bar_chart(estagios)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ataque vs Defesa")
        st.scatter_chart(dados[['ATK lvl 50', 'DEF lvl 50']].dropna().head(100))
    with col2:
        st.subheader("Velocidade vs Inteligencia")
        st.scatter_chart(dados[['SPD lvl 50', 'INT lvl 50']].dropna().head(100))
    
    st.subheader("Top 10 Digimons Mais Fortes (Ataque)")
    top_digimons = dados.nlargest(10, 'ATK lvl 50')[['Digimon', 'Stage', 'ATK lvl 50', 'DEF lvl 50']]
    st.dataframe(top_digimons)