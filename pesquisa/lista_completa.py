# pesquisa/lista_completa.py
import streamlit as st

def mostrar(dados):
    """Mostra a lista completa de Digimons"""
    st.subheader("Digidex - Lista Completa de Digimons")
    
    if st.button("Ver todos os Digimons"):
        st.info(f"Total de Digimons disponiveis: {len(dados)}")
        
        # Criar tabela com as colunas importantes
        tabela_digimons = dados[['Number', 'Digimon', 'Stage', 'Type', 'ATK lvl 50', 'SPD lvl 50']].copy()
        
        # ORDENAR POR NUMBER (ID) DO MENOR PARA O MAIOR
        tabela_digimons = tabela_digimons.sort_values('Number')
        
        st.dataframe(
            tabela_digimons,
            column_config={
                "Number": "ID",
                "Digimon": "Nome",
                "Stage": "Estagio",
                "Type": "Tipo",
                "ATK lvl 50": "Ataque",
                "SPD lvl 50": "Velocidade"
            },
            hide_index=True,
            use_container_width=True
        )
        
        # Opcao para baixar a lista
        csv = tabela_digimons.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Baixar lista completa (CSV)",
            data=csv,
            file_name='todos_digimons.csv',
            mime='text/csv'
        )