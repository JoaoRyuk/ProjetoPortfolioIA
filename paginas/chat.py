# paginas/chat.py
import streamlit as st
from utils.gemini import configurar_gemini, responder_pergunta

def mostrar(dados):
    st.header("Chat com o Mundo Digital (Google Gemini)")
    
    # ===== DIAGNÓSTICO COMPLETO =====
    with st.expander("🔧 Diagnóstico da Conexão (clique para ver)"):
        st.write("**Informações do ambiente:**")
        
        # Verificar st.secrets
        try:
            if hasattr(st, 'secrets'):
                st.write(f"🔹 st.secrets disponível: ✅ Sim")
                st.write(f"🔹 Keys disponíveis: {list(st.secrets.keys()) if st.secrets else 'Nenhuma'}")
                
                if 'GEMINI_API_KEY' in st.secrets:
                    chave = st.secrets['GEMINI_API_KEY']
                    st.success(f"✅ Chave encontrada no st.secrets: {chave[:10]}...")
                else:
                    st.warning("⚠️ Chave NÃO encontrada no st.secrets")
            else:
                st.warning("⚠️ st.secrets NÃO está disponível")
        except Exception as e:
            st.error(f"Erro ao acessar st.secrets: {e}")
        
        # Verificar variáveis de ambiente
        import os
        chave_env = os.getenv('GEMINI_API_KEY')
        if chave_env:
            st.success(f"✅ Chave encontrada no os.environ: {chave_env[:10]}...")
        else:
            st.warning("⚠️ Chave NÃO encontrada no os.environ")
    
    st.markdown("""
    **Assistente Digimon IA com Google Gemini**
    
    Faça perguntas sobre Digimons e a IA do Google vai responder.
    """)
    
    # Tentar configurar o Gemini
    try:
        modelo = configurar_gemini()
        ia_disponivel = True
        st.success("✅ IA Gemini configurada com sucesso!")
    except Exception as e:
        ia_disponivel = False
        st.error(f"❌ Erro ao configurar Gemini: {e}")
    
    pergunta = st.text_input("Faça sua pergunta:", placeholder="Ex: Qual o Digimon mais forte?")
    
    if st.button("Perguntar"):
        if pergunta and ia_disponivel:
            with st.spinner("Consultando a IA Gemini..."):
                resposta = responder_pergunta(pergunta, dados)
                st.success("Resposta:")
                st.write(resposta)
        elif not ia_disponivel:
            st.error("❌ IA não disponível. Verifique o diagnóstico acima.")
        else:
            st.warning("Digite uma pergunta.")