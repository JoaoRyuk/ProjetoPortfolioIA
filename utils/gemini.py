# utils/gemini.py
import os
import streamlit as st
from google.oauth2 import service_account
import google.generativeai as genai
import json

def configurar_gemini():
    """Configura a API do Google Gemini usando conta de serviço"""
    
    # Tentar carregar do st.secrets (Streamlit Cloud)
    try:
        chave_privada = st.secrets.get('GEMINI_PRIVATE_KEY')
        if chave_privada:
            # Construir o dicionário de credenciais
            credenciais_dict = {
                "type": "service_account",
                "project_id": "projetogemini-499821",
                "private_key_id": "35c65a5d27580888557e19357c550a16342cf678",
                "private_key": chave_privada,
                "client_email": "gemini-service@projetogemini-499821.iam.gserviceaccount.com",
                "client_id": "116849209168678683587",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gemini-service%40projetogemini-499821.iam.gserviceaccount.com",
                "universe_domain": "googleapis.com"
            }
        else:
            raise ValueError("GEMINI_PRIVATE_KEY não encontrado nos secrets")
    except Exception as e:
        # Fallback local
        try:
            with open('projetogemini-499821-35c65a5d2758.json', 'r') as f:
                credenciais_dict = json.load(f)
        except:
            raise ValueError(f"Arquivo de credenciais não encontrado: {e}")
    
    # Criar credenciais
    try:
        credentials = service_account.Credentials.from_service_account_info(
            credenciais_dict,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        genai.configure(credentials=credentials)
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        raise ValueError(f"Erro ao configurar Gemini: {str(e)}")

def responder_pergunta(pergunta, dados):
    """Responde uma pergunta usando Gemini"""
    
    try:
        modelo = configurar_gemini()
    except Exception as e:
        return f"❌ Erro de configuração: {str(e)}"
    
    # Converter estágios para string
    estagios = [str(estagio) for estagio in dados['Stage'].unique()]
    
    contexto = f"""
    Você é um assistente especialista em Digimon.
    Responda de forma clara e objetiva.
    
    Informações sobre os Digimons:
    - Total: {len(dados)}
    - Estágios: {', '.join(estagios)}
    - Ataque médio: {int(dados['ATK lvl 50'].mean())}
    - Defesa média: {int(dados['DEF lvl 50'].mean())}
    - Velocidade média: {int(dados['SPD lvl 50'].mean())}
    """
    
    prompt = f"{contexto}\n\nPergunta do usuário: {pergunta}\n\nResposta:"
    
    try:
        resposta = modelo.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"❌ Erro ao chamar o Gemini: {str(e)}"