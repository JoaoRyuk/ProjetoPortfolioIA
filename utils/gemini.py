# utils/gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def configurar_gemini():
    """Configura a API do Google Gemini com a chave do arquivo .env"""
    chave = os.getenv('GEMINI_API_KEY')
    if not chave:
        raise ValueError("Chave do Gemini nao encontrada. Configure o arquivo .env")
    genai.configure(api_key=chave)
    return genai.GenerativeModel('gemini-2.5-flash')

def responder_pergunta(pergunta, dados):
    """Responde uma pergunta usando Gemini com contexto dos dados"""
    
    try:
        modelo = configurar_gemini()
    except Exception as e:
        return f"Erro de configuracao: {str(e)}"
    
    # Converter todos os estágios para string antes de juntar
    estagios = [str(estagio) for estagio in dados['Stage'].unique()]
    
    # Preparar o contexto
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