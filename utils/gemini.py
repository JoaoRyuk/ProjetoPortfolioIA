# utils/gemini.py
import os
import streamlit as st
import requests
import json

def configurar_gemini():
    """Retorna a chave da API do Gemini"""
    
    chave = None
    
    # 1. Tentar st.secrets (Streamlit Cloud)
    try:
        if hasattr(st, 'secrets'):
            if 'GEMINI_API_KEY' in st.secrets:
                chave = st.secrets['GEMINI_API_KEY']
    except:
        pass
    
    # 2. Tentar .env (local)
    if not chave:
        chave = os.getenv('GEMINI_API_KEY')
    
    if not chave:
        raise ValueError("Chave do Gemini não encontrada!")
    
    return chave

def responder_pergunta(pergunta, dados):
    """Responde uma pergunta usando Gemini via API REST"""
    
    try:
        chave = configurar_gemini()
    except Exception as e:
        return f"❌ Erro de configuração: {str(e)}"
    
    # Preparar os dados de contexto
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
    
    # ===== CHAMADA DIRETA À API DO GEMINI =====
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={chave}"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        resposta = requests.post(url, json=payload, headers=headers)
        
        if resposta.status_code == 200:
            dados_resposta = resposta.json()
            texto = dados_resposta.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', 'Sem resposta')
            return texto
        else:
            return f"❌ Erro {resposta.status_code}: {resposta.text}"
            
    except Exception as e:
        return f"❌ Erro na requisição: {str(e)}"