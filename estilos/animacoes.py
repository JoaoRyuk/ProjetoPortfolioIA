# utils/estilos/animacoes.py
import streamlit as st

def aplicar_animacoes():
    """Aplica animações e transições"""
    
    st.markdown("""
    <style>
        /* ===== TRANSICOES GERAIS ===== */
        * {
            transition: all 0.3s ease !important;
        }
        
        /* ===== HOVER EFEITOS ===== */
        .stButton button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 6px 25px rgba(255, 123, 0, 0.5) !important;
        }
        
        .stButton button:active {
            transform: scale(0.98) !important;
        }
        
        /* ===== FADE IN ===== */
        .stApp {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* ===== SLIDE IN (SIDEBAR) ===== */
        .css-1d391kg {
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }
        
        /* ===== BALOES ===== */
        .stBalloons {
            position: fixed !important;
            z-index: 9999 !important;
            animation: balloonsFloat 2s ease-in-out;
        }
        
        @keyframes balloonsFloat {
            0% { transform: translateY(0); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: translateY(-100vh); opacity: 0; }
        }
        
        /* ===== CARDS ===== */
        .card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }
        
        /* ===== EXPANDERS ===== */
        .streamlit-expanderHeader {
            transition: background 0.3s ease !important;
        }
        
        /* ===== METRICAS ===== */
        .stMetric {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .stMetric:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(255, 123, 0, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)