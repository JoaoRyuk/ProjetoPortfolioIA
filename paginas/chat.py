# paginas/chat.py
import streamlit as st

def mostrar(dados):
    """Mostra o chat com respostas inteligentes"""
    st.header("Chat com o Mundo Digital")
    
    st.markdown("""
    Assistente Digimon IA
    Faca perguntas sobre os Digimons e a IA vai responder.
    
    Exemplos:
    - "Quais sao os Digimons mais fortes?"
    - "Me fale sobre o Agumon"
    - "Qual a media de ataque?"
    """)
    
    pergunta = st.text_input("Faca sua pergunta:")
    
    if st.button("Perguntar a IA"):
        if pergunta:
            with st.spinner("Analisando os dados do Digimundo..."):
                pergunta_lower = pergunta.lower()
                
                if "forte" in pergunta_lower or "ataque" in pergunta_lower:
                    top = dados.nlargest(5, 'ATK lvl 50')[['Digimon', 'Stage', 'ATK lvl 50']]
                    resposta = "Os Digimons com maior ataque sao:\n\n"
                    for i, (_, row) in enumerate(top.iterrows(), 1):
                        resposta += f"{i}. {row['Digimon']} ({row['Stage']}) - {int(row['ATK lvl 50'])} de ataque\n"
                    st.info(resposta)
                
                elif "rapido" in pergunta_lower or "velocidade" in pergunta_lower:
                    top = dados.nlargest(5, 'SPD lvl 50')[['Digimon', 'Stage', 'SPD lvl 50']]
                    resposta = "Os Digimons mais rapidos sao:\n\n"
                    for i, (_, row) in enumerate(top.iterrows(), 1):
                        resposta += f"{i}. {row['Digimon']} ({row['Stage']}) - {int(row['SPD lvl 50'])} de velocidade\n"
                    st.info(resposta)
                
                elif "defesa" in pergunta_lower:
                    top = dados.nlargest(5, 'DEF lvl 50')[['Digimon', 'Stage', 'DEF lvl 50']]
                    resposta = "Os Digimons com maior defesa sao:\n\n"
                    for i, (_, row) in enumerate(top.iterrows(), 1):
                        resposta += f"{i}. {row['Digimon']} ({row['Stage']}) - {int(row['DEF lvl 50'])} de defesa\n"
                    st.info(resposta)
                
                elif "agumon" in pergunta_lower:
                    agumon = dados[dados['Digimon'].str.contains('Agumon', case=False)]
                    if not agumon.empty:
                        row = agumon.iloc[0]
                        st.info(f"""
                        Sobre o Agumon:
                        - Estagio: {row['Stage']}
                        - Ataque: {int(row['ATK lvl 50'])}
                        - Defesa: {int(row['DEF lvl 50'])}
                        - Inteligencia: {int(row['INT lvl 50'])}
                        - Velocidade: {int(row['SPD lvl 50'])}
                        
                        O Agumon e um Digimon reptil do tipo Vacina. 
                        Ele e conhecido por sua lealdade e coragem.
                        """)
                    else:
                        st.info("Agumon nao encontrado no dataset.")
                
                elif "media" in pergunta_lower:
                    st.info(f"""
                    Medias de todos os Digimons:
                    - Ataque: {int(dados['ATK lvl 50'].mean())}
                    - Defesa: {int(dados['DEF lvl 50'].mean())}
                    - Inteligencia: {int(dados['INT lvl 50'].mean())}
                    - Velocidade: {int(dados['SPD lvl 50'].mean())}
                    """)
                
                elif "quantos" in pergunta_lower or "total" in pergunta_lower:
                    st.info(f"No total, existem {len(dados)} Digimons no dataset.")
                
                else:
                    st.info("""
                    Nao entendi sua pergunta.
                    
                    Tente perguntar sobre:
                    - Digimons mais fortes
                    - Digimons mais rapidos
                    - Digimons com maior defesa
                    - O Agumon
                    - Medias de estatisticas
                    - Total de Digimons
                    """)
        else:
            st.warning("Digite uma pergunta primeiro.")