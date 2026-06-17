# utils/estilos/tipografia.py
import streamlit as st

def aplicar_tipografia():
    """Aplica estilos de fontes e textos"""
    
    st.markdown("""
    <style>
        /* ===== TITULOS ===== */
        h1, h2, h3, h4, h5, h6 {
            color: #ff7b00 !important;
            font-family: 'Segoe UI', 'Arial', sans-serif !important;
            font-weight: 700 !important;
        }
        
        h1 {
            font-size: 3.5rem !important;
            text-shadow: 0 0 20px rgba(255, 123, 0, 0.3);
            margin-bottom: 0.5rem !important;
        }
        
        h2 {
            font-size: 2.2rem !important;
            border-bottom: 2px solid rgba(255, 123, 0, 0.2);
            padding-bottom: 0.5rem !important;
            margin-bottom: 1rem !important;
        }
        
        h3 {
            font-size: 1.5rem !important;
            color: #ff7b00 !important;
        }
        
        /* ===== CABECALHO PERSONALIZADO ===== */
        .titulo-principal {
            font-size: 3.5rem;
            margin: 0;
            background: linear-gradient(90deg, #ff7b00, #ff5500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            text-align: center;
        }
        
        .subtitulo {
            font-size: 1.2rem;
            color: #aaa;
            margin: 0;
            text-align: center;
        }
        
        /* ===== TEXTO ===== */
        p, li, span, div {
            color: #e0e0e0 !important;
            font-family: 'Segoe UI', 'Arial', sans-serif !important;
        }
        
        .stMarkdown p {
            color: #e0e0e0 !important;
            line-height: 1.6 !important;
        }
        
        /* ===== LABELS ===== */
        label {
            color: #e0e0e0 !important;
            font-weight: 500 !important;
        }
        
        /* ===== SIDEBAR TEXTO ===== */
        .sidebar-text {
            color: #aaa;
            font-size: 0.8rem;
        }
        
        .sidebar-title {
            color: #ff7b00;
            font-size: 1.2rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)