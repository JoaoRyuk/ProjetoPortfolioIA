# paginas/pesquisa.py - Arquivo principal (pequeno e organizado)
import streamlit as st
from pesquisa import guia_novatos, lista_completa, busca_nome, recomendacoes, caminho_evolucao

def mostrar(dados):
    """Mostra a página de pesquisa e recomendacoes"""
    st.header("Pesquise Digimons e Receba Recomendacoes")
    
    # 1. Guia para novatos
    guia_novatos.mostrar()
    
    # 2. Lista completa
    lista_completa.mostrar(dados)
    
    # 3. Divisória
    st.markdown("---")
    
    # 4. Busca e Recomendações (lado a lado)
    col1, col2 = st.columns(2)
    
    with col1:
        busca_nome.mostrar(dados)
    
    with col2:
        recomendacoes.mostrar(dados)
    
    # 5. Caminho de evolução
    caminho_evolucao.mostrar(dados)