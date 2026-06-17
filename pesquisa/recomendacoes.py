# pesquisa/recomendacoes.py
import streamlit as st

def mostrar(dados):
    """Mostra as recomendações por categoria"""
    st.subheader("Recomendacoes por Categoria")
    
    categoria = st.selectbox(
        "Escolha o atributo para recomendar:",
        ["Ataque", "Defesa", "Velocidade", "Inteligencia", "HP", "SP", "Melhor Geral", "Mais Equilibrado"]
    )
    
    if st.button("Recomendar Digimons"):
        if categoria == "Ataque":
            top = dados.nlargest(5, 'ATK lvl 50')[['Digimon', 'Stage', 'ATK lvl 50', 'Type']]
            st.info("Os 5 Digimons com maior Ataque:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Ataque: {int(row['ATK lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "Defesa":
            top = dados.nlargest(5, 'DEF lvl 50')[['Digimon', 'Stage', 'DEF lvl 50', 'Type']]
            st.info("Os 5 Digimons com maior Defesa:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Defesa: {int(row['DEF lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "Velocidade":
            top = dados.nlargest(5, 'SPD lvl 50')[['Digimon', 'Stage', 'SPD lvl 50', 'Type']]
            st.info("Os 5 Digimons mais rapidos:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Velocidade: {int(row['SPD lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "Inteligencia":
            top = dados.nlargest(5, 'INT lvl 50')[['Digimon', 'Stage', 'INT lvl 50', 'Type']]
            st.info("Os 5 Digimons mais inteligentes:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Inteligencia: {int(row['INT lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "HP":
            top = dados.nlargest(5, 'HP lvl 50')[['Digimon', 'Stage', 'HP lvl 50', 'Type']]
            st.info("Os 5 Digimons com mais HP:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - HP: {int(row['HP lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "SP":
            top = dados.nlargest(5, 'SP lvl 50')[['Digimon', 'Stage', 'SP lvl 50', 'Type']]
            st.info("Os 5 Digimons com mais SP:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - SP: {int(row['SP lvl 50'])} - Tipo: {row['Type']}")
        
        elif categoria == "Melhor Geral":
            dados['Total'] = dados['HP lvl 50'] + dados['SP lvl 50'] + dados['ATK lvl 50'] + dados['DEF lvl 50'] + dados['INT lvl 50'] + dados['SPD lvl 50']
            top = dados.nlargest(5, 'Total')[['Digimon', 'Stage', 'Total', 'Type']]
            st.info("Os 5 Digimons com melhor soma de atributos:")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Total: {int(row['Total'])} - Tipo: {row['Type']}")
            dados.drop('Total', axis=1, inplace=True)
        
        elif categoria == "Mais Equilibrado":
            atributos = ['HP lvl 50', 'SP lvl 50', 'ATK lvl 50', 'DEF lvl 50', 'INT lvl 50', 'SPD lvl 50']
            dados['Desvio'] = dados[atributos].std(axis=1)
            dados_filtrados = dados[(dados['HP lvl 50'] > 100) & (dados['ATK lvl 50'] > 100)]
            top = dados_filtrados.nsmallest(5, 'Desvio')[['Digimon', 'Stage', 'Desvio', 'Type']]
            st.info("Os 5 Digimons mais equilibrados (todos os atributos balanceados):")
            for i, (_, row) in enumerate(top.iterrows(), 1):
                st.write(f"{i}. **{row['Digimon']}** ({row['Stage']}) - Desvio: {row['Desvio']:.1f} - Tipo: {row['Type']}")
            dados.drop('Desvio', axis=1, inplace=True)