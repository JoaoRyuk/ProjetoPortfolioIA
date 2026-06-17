# utils/estilos/componentes.py
import streamlit as st

def aplicar_componentes():
    """Aplica estilos para botões, inputs e componentes"""
    
    st.markdown("""
    <style>
        /* ===== BOTOES ===== */
        .stButton button {
            background: linear-gradient(90deg, #ff7b00, #ff5500) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.6rem 1.5rem !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(255, 123, 0, 0.3) !important;
            width: 100% !important;
        }
        
        .stButton button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 6px 25px rgba(255, 123, 0, 0.5) !important;
        }
        
        .stButton button:active {
            transform: scale(0.98) !important;
        }
        
        /* ===== INPUTS ===== */
        .stTextInput input {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 123, 0, 0.3) !important;
            border-radius: 8px !important;
            color: #e0e0e0 !important;
            padding: 0.6rem !important;
        }
        
        .stTextInput input:focus {
            border-color: #ff7b00 !important;
            box-shadow: 0 0 15px rgba(255, 123, 0, 0.2) !important;
        }
        
        /* ===== SELECTBOX ===== */
        .stSelectbox div[data-baseweb="select"] {
            background: rgba(255, 255, 255, 0.05) !important;
            border-radius: 8px !important;
            border: 1px solid rgba(255, 123, 0, 0.3) !important;
        }
        
        .stSelectbox div[data-baseweb="select"]:hover {
            border-color: #ff7b00 !important;
        }
        
        /* ===== SLIDERS ===== */
        .stSlider .stSliderTrack {
            background: rgba(255, 123, 0, 0.3) !important;
            height: 4px !important;
        }
        
        .stSlider .stSliderThumb {
            background: #ff7b00 !important;
            border: 2px solid #ff7b00 !important;
            width: 16px !important;
            height: 16px !important;
        }
        
        .stSlider .stSliderThumb:hover {
            transform: scale(1.2) !important;
        }
        
        /* ===== RADIO BUTTONS ===== */
        .stRadio label {
            color: #e0e0e0 !important;
            padding: 0.3rem 0 !important;
        }
        
        .stRadio label:hover {
            color: #ff7b00 !important;
        }
        
        .stRadio div[role="radiogroup"] {
            gap: 0.2rem !important;
        }
        
        /* ===== DOWNLOAD BUTTONS ===== */
        .stDownloadButton button {
            background: rgba(255, 123, 0, 0.2) !important;
            border: 1px solid #ff7b00 !important;
            color: #ff7b00 !important;
        }
        
        .stDownloadButton button:hover {
            background: rgba(255, 123, 0, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)