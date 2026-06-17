# utils/estilos/layout.py
import streamlit as st

def aplicar_layout():
    """Aplica estilos de layout e estrutura"""
    
    st.markdown("""
    <style>
        /* ===== LAYOUT GERAL ===== */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        
        /* ===== COLUNAS ===== */
        .stColumns {
            gap: 1rem;
        }
        
        /* ===== DIVISORIAS ===== */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, rgba(255, 123, 0, 0.3), rgba(255, 123, 0, 0.1));
            margin: 2rem 0;
        }
        
        /* ===== RODAPE ===== */
        .footer {
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
            border-top: 1px solid rgba(255, 123, 0, 0.2);
            color: #888;
            font-size: 0.9rem;
        }
        
        /* ===== CARDS ===== */
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid rgba(255, 123, 0, 0.2);
            backdrop-filter: blur(10px);
            margin-bottom: 1rem;
        }
        
        /* ===== GRID ===== */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }
        
        /* ===== TABELAS ===== */
        .stTable {
            background: rgba(255, 255, 255, 0.05) !important;
            border-radius: 12px !important;
        }
        
        /* ===== BALOES ===== */
        .stBalloons {
            position: fixed !important;
            z-index: 9999 !important;
        }
        
        /* ===== SIDEBAR ===== */
        .css-1v3fvcr {
            background: linear-gradient(180deg, #0d0d2b, #1a1a4e) !important;
        }
    </style>
    """, unsafe_allow_html=True)