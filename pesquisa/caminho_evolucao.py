# pesquisa/caminho_evolucao.py
import streamlit as st
import random

def mostrar(dados):
    """Mostra o caminho de evolução com sugestões"""
    st.markdown("---")
    st.subheader("Qual caminho de evolucao seguir?")
    
    st.markdown("""
    Escolha um Digimon inicial e veja para quais estagios ele pode evoluir.
    """)
    
    todos_nomes = sorted(dados['Digimon'].tolist())
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        nome_evolucao = st.text_input(
            "Digite o nome do Digimon para ver suas opcoes de evolucao:",
            placeholder="Ex: Agumon, Gabumon, etc."
        )
    
    with col2:
        if st.button("Surpreenda-me"):
            digimon_aleatorio = random.choice(todos_nomes)
            nome_evolucao = digimon_aleatorio
            st.info(f"Que tal evoluir o {digimon_aleatorio}?")
    
    if st.button("Ver Opcoes de Evolucao"):
        if nome_evolucao:
            ver_evolucoes(dados, nome_evolucao)
        else:
            st.warning("Digite um nome para buscar")


def ver_evolucoes(dados, nome_digimon):
    """Mostra as opções de evolução para um Digimon"""
    
    digimon_atual = dados[dados['Digimon'].str.contains(nome_digimon, case=False, na=False)]
    
    if not digimon_atual.empty:
        row = digimon_atual.iloc[0]
        estagio_atual = row['Stage']
        
        # Classificação do estágio
        classificacao = classificar_estagio(estagio_atual)
        
        st.success(f"**{row['Digimon']}** - Estagio atual: {estagio_atual} ({classificacao})")
        
        estagios_ordem = ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate', 'Mega', 'Ultra']
        
        if estagio_atual in estagios_ordem:
            idx_atual = estagios_ordem.index(estagio_atual)
            proximos_estagios = estagios_ordem[idx_atual+1:]
            
            if proximos_estagios:
                st.info(f"Possiveis caminhos de evolucao para {row['Digimon']}:")
                
                for prox in proximos_estagios:
                    classificacao_prox = classificar_estagio(prox)
                    candidatos = dados[dados['Stage'] == prox].nlargest(3, 'ATK lvl 50')
                    
                    if not candidatos.empty:
                        with st.expander(f"Para {prox} ({classificacao_prox}) - 3 melhores em ataque:"):
                            for _, cand in candidatos.iterrows():
                                st.write(f"  - **{cand['Digimon']}** (Ataque: {int(cand['ATK lvl 50'])})")
            else:
                st.info(f"{row['Digimon']} ja esta no estagio maximo.")
        else:
            st.info(f"Estagio '{estagio_atual}' nao reconhecido para recomendacao de evolucao.")
        
        with st.expander("Ver estatisticas completas"):
            st.write(f"""
            **{row['Digimon']} - Estatisticas completas:**
            
            | Atributo | Valor (Nv. 50) |
            |----------|----------------|
            | HP       | {int(row['HP lvl 50'])} |
            | SP       | {int(row['SP lvl 50'])} |
            | Ataque   | {int(row['ATK lvl 50'])} |
            | Defesa   | {int(row['DEF lvl 50'])} |
            | Inteligencia | {int(row['INT lvl 50'])} |
            | Velocidade | {int(row['SPD lvl 50'])} |
            | Tipo     | {row['Type']} |
            | Atributo | {row['Attribute']} |
            """)
    else:
        st.warning(f"Nenhum Digimon encontrado com o nome '{nome_digimon}'")


def classificar_estagio(estagio):
    """Classifica o estágio do Digimon em níveis de experiência"""
    classificacoes = {
        'Baby': 'Iniciante',
        'In-Training': 'Iniciante',
        'Rookie': 'Intermediario',
        'Champion': 'Avancado',
        'Ultimate': 'Avancado',
        'Mega': 'Especialista',
        'Ultra': 'Especialista',
        'Armor': 'Especial'
    }
    return classificacoes.get(estagio, 'Desconhecido')