# teste_gemini.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

print("=" * 50)
print("TESTE DE CONEXÃO COM GOOGLE GEMINI")
print("=" * 50)

chave = os.getenv('GEMINI_API_KEY')

if chave:
    print(f"Chave carregada: {chave[:15]}...")
    try:
        genai.configure(api_key=chave)
        
        # Usando gemini-2.5-flash (disponível na lista)
        print("\n🔄 Tentando gerar conteudo com gemini-2.5-flash...")
        modelo = genai.GenerativeModel('gemini-2.5-flash')
        resposta = modelo.generate_content("Diga 'Ola, estou funcionando!'")
        print("\n✅ SUCESSO!")
        print(resposta.text)
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
else:
    print("❌ Chave nao encontrada!")