# paginas/chat.py
import streamlit as st
from utils.gemini import configurar_gemini, responder_pergunta

def mostrar(dados):
    """Mostra o chat com respostas usando a IA do Google Gemini"""
    st.header("Chat com o Mundo Digital (Google Gemini)")
    
    # ===== DIAGNÓSTICO =====
    with st.expander("🔧 Diagnóstico da Conexão (clique para ver)"):
        try:
            chave = None
            if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
                chave = st.secrets['GEMINI_API_KEY']
                st.success(f"✅ Chave encontrada no st.secrets: {chave[:10]}...")
            else:
                st.warning("⚠️ Chave NÃO encontrada no st.secrets")
                # Tenta carregar do .env como fallback
                import os
                from dotenv import load_dotenv
                load_dotenv()
                chave = os.getenv('GEMINI_API_KEY')
                if chave:
                    st.info(f"ℹ️ Chave carregada do .env local: {chave[:10]}...")
                else:
                    st.error("❌ Nenhuma chave encontrada em lugar nenhum!")
        except Exception as e:
            st.error(f"Erro no diagnóstico: {e}")
    
    st.markdown("""
    **Assistente Digimon IA com Google Gemini**
    
    Faca perguntas sobre Digimons e a IA do Google vai responder usando inteligencia artificial gratuita.
    
    **Exemplos:**
    - "Qual e o melhor Digimon para iniciantes?"
    - "Como evoluir o Agumon para Greymon?"
    - "Monte um time balanceado com 3 Digimons"
    - "Qual a diferenca entre Vaccine e Virus?"
    """)
    
    # Tentar configurar o Gemini
    try:
        modelo = configurar_gemini()
        ia_disponivel = True
    except Exception as e:
        ia_disponivel = False
        st.warning(f"""
        **API Gemini nao configurada!** Detalhe: {e}
        
        Para usar a IA, voce precisa:
        1. Criar uma conta Google
        2. Acessar o Google AI Studio: https://aistudio.google.com/
        3. Gerar uma chave de API
        4. Adicionar a chave no arquivo `.env` (local) ou nos secrets do Streamlit (cloud)
        """)
    
    pergunta = st.text_input("Faca sua pergunta sobre Digimons:", placeholder="Ex: Qual o Digimon mais forte?")
    
    if st.button("Perguntar para IA (Gemini)"):
        if pergunta:
            if ia_disponivel:
                with st.spinner("Consultando a IA Gemini..."):
                    resposta = responder_pergunta(pergunta, dados)
                    st.success("Resposta da IA Gemini:")
                    st.write(resposta)
            else:
                st.error("A IA Gemini não está configurada. Verifique o diagnóstico acima.")
        else:
            st.warning("Digite uma pergunta primeiro.")