# utils/gemini.py
import os
import streamlit as st
import google.generativeai as genai

def configurar_gemini():
    """Configura a API do Google Gemini"""
    
    chave = None
    
    # ===== TENTAR DIFERENTES FONTES =====
    
    # 1. Tentar st.secrets (Streamlit Cloud)
    try:
        # Verificar se st.secrets existe e tem a chave
        if hasattr(st, 'secrets'):
            if 'GEMINI_API_KEY' in st.secrets:
                chave = st.secrets['GEMINI_API_KEY']
                print("🔑 Chave encontrada no st.secrets")  # Log para debug
    except Exception as e:
        print(f"Erro ao acessar st.secrets: {e}")
    
    # 2. Se não encontrou, tentar variável de ambiente
    if not chave:
        chave = os.getenv('GEMINI_API_KEY')
        if chave:
            print("🔑 Chave encontrada no os.environ")
    
    # 3. Se ainda não encontrou, tentar ler arquivo .env manualmente
    if not chave:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            chave = os.getenv('GEMINI_API_KEY')
            if chave:
                print("🔑 Chave encontrada no .env")
        except:
            pass
    
    # ===== VERIFICAR SE ENCONTROU =====
    if not chave:
        raise ValueError("""
        Chave do Gemini não encontrada!
        
        Verifique:
        1. No Streamlit Cloud: Settings > Secrets
        2. Localmente: arquivo .env com GEMINI_API_KEY
        """)
    
    # ===== CONFIGURAR E RETORNAR =====
    genai.configure(api_key=chave)
    return genai.GenerativeModel('gemini-1.5-flash')

def responder_pergunta(pergunta, dados):
    """Responde uma pergunta usando Gemini"""
    
    try:
        modelo = configurar_gemini()
    except Exception as e:
        return f"❌ Erro de configuracao: {str(e)}"
    
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