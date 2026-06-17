# utils/estilos.py - Design limpo e legível
import streamlit as st

def aplicar_estilos():
    """Aplica estilos CSS personalizados - versão limpa"""
    
    st.markdown("""
    <style>
        /* ===== FUNDO BRANCO/LIMPO ===== */
        .stApp {
            background-color: #f8f9fa;
        }
        
        /* ===== CORPO DA PÁGINA ===== */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }
        
        /* ===== TITULOS ===== */
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50 !important;
            font-family: 'Segoe UI', sans-serif !important;
        }
        
        h1 {
            font-size: 2.8rem !important;
            font-weight: 700 !important;
            color: #2c3e50 !important;
        }
        
        h2 {
            font-size: 2rem !important;
            font-weight: 600 !important;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }
        
        h3 {
            font-size: 1.3rem !important;
            font-weight: 600 !important;
            color: #34495e !important;
        }
        
        /* ===== TEXTO ===== */
        p, li, span, div, label {
            color: #2c3e50 !important;
            font-family: 'Segoe UI', sans-serif !important;
        }
        
        .stMarkdown p {
            color: #2c3e50 !important;
            line-height: 1.6 !important;
        }
        
        /* ===== SIDEBAR ===== */
        .css-1d391kg, .css-1lcbmhc {
            background-color: #ffffff !important;
            border-right: 1px solid #e0e0e0 !important;
        }
        
        .sidebar .sidebar-content {
            background-color: #ffffff !important;
        }
        
        /* ===== BOTOES ===== */
        .stButton button {
            background-color: #3498db !important;
            color: white !important;
            border: none !important;
            border-radius: 6px !important;
            padding: 0.5rem 1.5rem !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }
        
        .stButton button:hover {
            background-color: #2980b9 !important;
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3) !important;
        }
        
        /* ===== METRICAS ===== */
        .stMetric {
            background-color: #ffffff !important;
            border-radius: 8px !important;
            padding: 1rem !important;
            border: 1px solid #e0e0e0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        
        .stMetric label {
            color: #7f8c8d !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
        }
        
        .stMetric .stMetricValue {
            color: #2c3e50 !important;
            font-size: 2rem !important;
            font-weight: 700 !important;
        }
        
        /* ===== EXPANDERS ===== */
        .streamlit-expanderHeader {
            background-color: #f8f9fa !important;
            border-radius: 6px !important;
            border: 1px solid #e0e0e0 !important;
            color: #2c3e50 !important;
            font-weight: 500 !important;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #e9ecef !important;
        }
        
        /* ===== DATAFRAMES ===== */
        .stDataFrame {
            border: 1px solid #e0e0e0 !important;
            border-radius: 8px !important;
            background-color: #ffffff !important;
        }
        
        .stDataFrame th {
            background-color: #f8f9fa !important;
            color: #2c3e50 !important;
            font-weight: 600 !important;
            border-bottom: 2px solid #e0e0e0 !important;
        }
        
        .stDataFrame td {
            color: #2c3e50 !important;
            border-bottom: 1px solid #f0f0f0 !important;
        }
        
        /* ===== INPUTS ===== */
        .stTextInput input {
            background-color: #ffffff !important;
            border: 1px solid #ced4da !important;
            border-radius: 6px !important;
            color: #2c3e50 !important;
            padding: 0.5rem !important;
        }
        
        .stTextInput input:focus {
            border-color: #3498db !important;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2) !important;
        }
        
        /* ===== SELECTBOX ===== */
        .stSelectbox div[data-baseweb="select"] {
            background-color: #ffffff !important;
            border: 1px solid #ced4da !important;
            border-radius: 6px !important;
        }
        
        /* ===== SLIDERS ===== */
        .stSlider .stSliderTrack {
            background-color: #d1d8e0 !important;
        }
        
        .stSlider .stSliderThumb {
            background-color: #3498db !important;
            border: 2px solid #3498db !important;
        }
        
        /* ===== MENSAGENS ===== */
        .stAlert {
            border-radius: 8px !important;
            border-left: 4px solid #3498db !important;
        }
        
        .stSuccess {
            background-color: #d4edda !important;
            border-left: 4px solid #28a745 !important;
            color: #155724 !important;
        }
        
        .stSuccess p {
            color: #155724 !important;
        }
        
        .stInfo {
            background-color: #d1ecf1 !important;
            border-left: 4px solid #17a2b8 !important;
            color: #0c5460 !important;
        }
        
        .stInfo p {
            color: #0c5460 !important;
        }
        
        .stWarning {
            background-color: #fff3cd !important;
            border-left: 4px solid #ffc107 !important;
            color: #856404 !important;
        }
        
        .stWarning p {
            color: #856404 !important;
        }
        
        .stError {
            background-color: #f8d7da !important;
            border-left: 4px solid #dc3545 !important;
            color: #721c24 !important;
        }
        
        .stError p {
            color: #721c24 !important;
        }
        
        /* ===== RODAPE ===== */
        .footer {
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
            border-top: 1px solid #e0e0e0;
            color: #7f8c8d;
            font-size: 0.9rem;
        }
        
        /* ===== RADIO BUTTONS ===== */
        .stRadio label {
            color: #2c3e50 !important;
            padding: 0.3rem 0 !important;
        }
        
        .stRadio label:hover {
            color: #3498db !important;
        }
        
        /* ===== LINKS ===== */
        a {
            color: #3498db !important;
            text-decoration: none !important;
        }
        
        a:hover {
            text-decoration: underline !important;
        }
        
        /* ===== BALOES ===== */
        .stBalloons {
            position: fixed !important;
            z-index: 9999 !important;
        }
        
        /* ===== TABELAS ===== */
        .stTable {
            background-color: #ffffff !important;
            border-radius: 8px !important;
            border: 1px solid #e0e0e0 !important;
        }
        
        /* ===== CODE ===== */
        code {
            background-color: #f0f0f0 !important;
            color: #2c3e50 !important;
            border-radius: 4px !important;
            padding: 0.1rem 0.3rem !important;
        }
        
        /* ===== CABECALHO ===== */
        .titulo-principal {
            color: #2c3e50 !important;
            font-size: 3rem;
            font-weight: 700;
            text-align: center;
            margin: 0;
        }
        
        .subtitulo {
            color: #7f8c8d !important;
            font-size: 1.2rem;
            text-align: center;
            margin: 0;
        }
        
        .linha-divisoria {
            width: 100px;
            height: 3px;
            background: #3498db;
            margin: 0.5rem auto;
        }
    </style>
    """, unsafe_allow_html=True)