# paginas/chat.py
import streamlit as st
from utils.gemini import configurar_gemini, responder_pergunta

def mostrar(dados):
    st.header("Chat com o Mundo Digital (Google Gemini)")
    
    # ===== DIAGNÓSTICO =====
    with st.expander("🔧 Diagnóstico da Conexão"):
        try:
            chave = None
            if hasattr(st, 'secrets') and 'GEMINI_API_KEY' in st.secrets:
                chave = st.secrets['GEMINI_API_KEY']
                st.success(f"✅ Chave encontrada no st.secrets: {chave[:10]}...")
            else:
                st.warning("⚠️ Chave NÃO encontrada no st.secrets")
                import os
                chave = os.getenv('GEMINI_API_KEY')
                if chave:
                    st.info(f"ℹ️ Chave carregada do .env: {chave[:10]}...")
                else:
                    st.error("❌ Nenhuma chave encontrada!")
        except Exception as e:
            st.error(f"Erro no diagnóstico: {e}")
    
    st.markdown("""
    **Assistente Digimon IA com Google Gemini**
    
    Faça perguntas sobre Digimons e a IA do Google vai responder.
    """)
    
    # Verifica se a chave está disponível
    try:
        chave = configurar_gemini()
        ia_disponivel = True
        st.success("✅ Chave configurada com sucesso!")
    except Exception as e:
        ia_disponivel = False
        st.error(f"❌ Erro: {e}")
    
    pergunta = st.text_input("Faça sua pergunta:", placeholder="Ex: Qual o Digimon mais forte?")
    
    if st.button("Perguntar"):
        if pergunta and ia_disponivel:
            with st.spinner("Consultando..."):
                resposta = responder_pergunta(pergunta, dados)
                st.success("Resposta:")
                st.write(resposta)
        elif not ia_disponivel:
            st.error("❌ Chave não disponível. Verifique o diagnóstico.")
        else:
            st.warning("Digite uma pergunta.")