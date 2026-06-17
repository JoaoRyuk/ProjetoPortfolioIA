# pesquisa/busca_nome.py
import streamlit as st

def mostrar(dados):
    """Mostra a busca de Digimon por nome com sugestões"""
    st.subheader("Buscar Digimon por Nome")
    
    todos_nomes = sorted(dados['Digimon'].tolist())
    
    nome_busca = st.text_input(
        "Digite o nome do Digimon:",
        placeholder="Ex: Agumon, Greymon, etc."
    )
    
    if nome_busca:
        sugestoes = [nome for nome in todos_nomes if nome_busca.lower() in nome.lower()]
        
        if sugestoes:
            st.write(f"Sugestoes encontradas: {len(sugestoes)}")
            with st.expander(f"Clique para ver {len(sugestoes)} sugestoes:"):
                for sug in sugestoes[:10]:
                    st.write(f"- {sug}")
                if len(sugestoes) > 10:
                    st.write(f"... e mais {len(sugestoes) - 10} Digimons")
    
    if st.button("Buscar Digimon"):
        if nome_busca:
            resultado = dados[dados['Digimon'].str.contains(nome_busca, case=False, na=False)]
            
            if not resultado.empty:
                st.success(f"Encontrado(s) {len(resultado)} Digimon(s):")
                for idx, row in resultado.iterrows():
                    with st.expander(f"{row['Digimon']} ({row['Stage']})"):
                        st.write(f"""
                        **Estatisticas (Nv. 50):**
                        - HP: {int(row['HP lvl 50'])}
                        - SP: {int(row['SP lvl 50'])}
                        - Ataque: {int(row['ATK lvl 50'])}
                        - Defesa: {int(row['DEF lvl 50'])}
                        - Inteligencia: {int(row['INT lvl 50'])}
                        - Velocidade: {int(row['SPD lvl 50'])}
                        - Tipo: {row['Type']}
                        - Atributo: {row['Attribute']}
                        """)
                        
                        from pesquisa.caminho_evolucao import ver_evolucoes
                        if st.button(f"Ver evolucoes de {row['Digimon']}", key=f"evol_{idx}"):
                            ver_evolucoes(dados, row['Digimon'])
            else:
                st.warning(f"Nenhum Digimon encontrado com o nome '{nome_busca}'")
                
                sugestoes_nomes = [nome for nome in todos_nomes if nome_busca[:2].lower() in nome.lower()]
                if sugestoes_nomes:
                    st.info(f"Voce quis dizer: {', '.join(sugestoes_nomes[:5])}?")
        else:
            st.warning("Digite um nome para buscar")