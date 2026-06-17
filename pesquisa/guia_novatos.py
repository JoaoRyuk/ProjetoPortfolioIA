# pesquisa/guia_novatos.py
import streamlit as st

def mostrar():
    """Mostra o guia rápido para novatos"""
    with st.expander("Dica para Novatos: Como usar esta pagina"):
        st.markdown("""
        **Bem-vindo ao Mundo Digital!**
        
        Se voce esta comecando agora, aqui estao algumas dicas:
        
        1. Nao conhece nenhum Digimon? Clique no botao "Ver todos os Digimons" abaixo.
        2. Quer saber qual e o mais forte? Escolha uma categoria em "Recomendacoes".
        3. Tem um Digimon em mente? Digite o nome na busca.
        4. Quer evoluir? Use a secao "Caminho de Evolucao".
        
        **Classificacao dos Estagios:**
        - Baby, In-Training = Iniciante
        - Rookie = Intermediario
        - Champion, Ultimate = Avancado
        - Mega, Ultra = Especialista
        - Armor = Especial (evolucao com digimental)
        """)