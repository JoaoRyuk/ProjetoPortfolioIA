# utils/estilos/cores.py
import streamlit as st

def aplicar_cores():
    """Aplica as cores e temas principais"""
    
    st.markdown("""
    <style>
        /* ===== CORES PRINCIPAIS ===== */
        :root {
            --cor-primaria: #ff7b00;
            --cor-secundaria: #ff5500;
            --cor-fundo: #0a0a2e;
            --cor-fundo-secundario: #1a1a4e;
            --cor-texto: #e0e0e0;
            --cor-texto-claro: #ffffff;
            --cor-borda: rgba(255, 123, 0, 0.2);
        }
        
        /* ===== FUNDO ===== */
        .stApp {
            background: linear-gradient(135deg, var(--cor-fundo) 0%, var(--cor-fundo-secundario) 50%, var(--cor-fundo) 100%);
        }
        
        /* ===== SIDEBAR ===== */
        .css-1d391kg, .css-1lcbmhc {
            background: linear-gradient(180deg, #0d0d2b, var(--cor-fundo-secundario)) !important;
            border-right: 2px solid var(--cor-primaria) !important;
        }
        
        /* ===== METRICAS ===== */
        .stMetric {
            background: rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px !important;
            padding: 1rem !important;
            border: 1px solid var(--cor-borda) !important;
            backdrop-filter: blur(10px) !important;
        }
        
        .stMetric label {
            color: var(--cor-primaria) !important;
            font-weight: bold !important;
        }
        
        .stMetric .stMetricValue {
            color: var(--cor-texto-claro) !important;
            font-size: 2rem !important;
        }
        
        /* ===== EXPANDERS ===== */
        .streamlit-expanderHeader {
            background: rgba(255, 123, 0, 0.1) !important;
            border-radius: 8px !important;
            border: 1px solid var(--cor-borda) !important;
            color: var(--cor-primaria) !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: rgba(255, 123, 0, 0.2) !important;
        }
        
        /* ===== DATAFRAMES ===== */
        .stDataFrame {
            background: rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px !important;
            border: 1px solid var(--cor-borda) !important;
        }
        
        .stDataFrame table {
            color: var(--cor-texto) !important;
        }
        
        .stDataFrame th {
            background: rgba(255, 123, 0, 0.2) !important;
            color: var(--cor-primaria) !important;
        }
        
        /* ===== MENSAGENS ===== */
        .stAlert {
            border-radius: 12px !important;
            border-left: 4px solid var(--cor-primaria) !important;
        }
        
        .stSuccess {
            background: rgba(0, 200, 100, 0.1) !important;
            border-left: 4px solid #00c864 !important;
        }
        
        .stInfo {
            background: rgba(255, 123, 0, 0.1) !important;
            border-left: 4px solid var(--cor-primaria) !important;
        }
        
        .stWarning {
            background: rgba(255, 200, 0, 0.1) !important;
            border-left: 4px solid #ffc800 !important;
        }
        
        .stError {
            background: rgba(255, 0, 0, 0.1) !important;
            border-left: 4px solid #ff0000 !important;
        }
        
        /* ===== LINKS ===== */
        a {
            color: var(--cor-primaria) !important;
            text-decoration: none !important;
        }
        
        a:hover {
            text-decoration: underline !important;
        }
    </style>
    """, unsafe_allow_html=True)