# app.py - Versão SEM CSS personalizado (usando tema padrão do Streamlit)
import streamlit as st
import os
from utils.funcoes import carregar_modelos, carregar_dados
from paginas import dashboard, previsor, chat, pesquisa

# ===== CONFIGURACAO =====
st.set_page_config(
    page_title="Digimon Master - Portal de Evolucoes",
    page_icon="⚡",
    layout="wide"
)

# ===== CABECALHO =====
st.title("Digimon Master")
st.subheader("O Portal de Evolucoes com Inteligencia Artificial")
st.markdown("---")

# ===== VERIFICAR ARQUIVOS =====
arquivos_necessarios = ['modelo_digimon.pkl', 'label_encoder_digimon.pkl', 'nomes_digimons.pkl', 'Digimon.csv']
arquivos_faltando = [f for f in arquivos_necessarios if not os.path.exists(f)]

if arquivos_faltando:
    st.error(f"Arquivos necessarios nao encontrados: {arquivos_faltando}")
    st.info("Execute primeiro o arquivo 'treinar_digimon.py' para gerar os modelos.")
    st.stop()

# ===== CARREGAR MODELOS =====
try:
    modelo, encoder, nomes = carregar_modelos()
    dados = carregar_dados()
except Exception as e:
    st.error(f"Erro ao carregar os arquivos: {e}")
    st.stop()

# ===== MENU LATERAL =====
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Digimon_Adventure_logo.png/220px-Digimon_Adventure_logo.png", 
             use_container_width=True)
    st.title("Digimon Master")
    st.caption("v1.0")
    st.markdown("---")
    
    opcao = st.radio(
        "Escolha sua jornada:",
        ["Dashboard", "Previsor de Evolucao", "Chat IA", "Pesquisa e Recomendacoes"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("""
    **Sobre o Projeto**
    
    Portal com:
    - Random Forest (ML)
    - Dashboard interativo
    - IA Generativa
    - Pesquisa e Recomendacoes
    """)

# ===== NAVEGACAO =====
if opcao == "Dashboard":
    dashboard.mostrar(dados)
elif opcao == "Previsor de Evolucao":
    previsor.mostrar(modelo, encoder)
elif opcao == "Chat IA":
    chat.mostrar(dados)
elif opcao == "Pesquisa e Recomendacoes":
    pesquisa.mostrar(dados)

# ===== RODAPE =====
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    Desenvolvido para portfolio | Junho 2026
</div>
""", unsafe_allow_html=True)