# utils/gemini.py
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar .env apenas se estiver rodando localmente
if os.path.exists('.env'):
    load_dotenv()

def configurar_gemini():
    """Configura a API do Google Gemini com a chave do ambiente ou secrets"""
    
    chave = None
    # 1. Tentar pegar do st.secrets (Streamlit Cloud)
    try:
        if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
            chave = st.secrets['GEMINI_API_KEY']
    except:
        pass
    
    # 2. Se não tiver no secrets, tentar do .env (local)
    if not chave:
        chave = os.getenv('GEMINI_API_KEY')
    
    if not chave:
        raise ValueError("Chave do Gemini nao encontrada. Configure o arquivo .env ou os secrets do Streamlit")
    
    # Configuração explícita para usar a chave de API
    genai.configure(api_key=chave)
    
    # Usando um modelo estável e amplamente disponível
    return genai.GenerativeModel('gemini-2.0-flash')

def responder_pergunta(pergunta, dados):
    """Responde uma pergunta usando Gemini com contexto dos dados"""
    
    try:
        modelo = configurar_gemini()
    except Exception as e:
        return f"Erro de configuracao: {str(e)}"
    
    # Converter estágios para string
    estagios = [str(estagio) for estagio in dados['Stage'].unique()]
    
    contexto = f"""
    Voce e um assistente especialista em Digimon.
    Responda de forma clara e objetiva.
    
    Informacoes sobre os Digimons:
    - Total: {len(dados)}
    - Estagios: {', '.join(estagios)}
    - Ataque medio: {int(dados['ATK lvl 50'].mean())}
    - Defesa media: {int(dados['DEF lvl 50'].mean())}
    - Velocidade media: {int(dados['SPD lvl 50'].mean())}
    """
    
    prompt_completo = f"{contexto}\n\nPergunta do usuario: {pergunta}\n\nResposta:"
    
    try:
        resposta = modelo.generate_content(prompt_completo)
        return resposta.text
    except Exception as e:
        return f"Erro ao chamar o Gemini: {str(e)}"