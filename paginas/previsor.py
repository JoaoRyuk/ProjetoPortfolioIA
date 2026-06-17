# paginas/previsor.py
import streamlit as st
from utils.funcoes import prever_estagio

def mostrar(modelo, encoder):
    """Mostra o previsor de evolucao e o plano de evolucao"""
    st.header("Preveja a Evolucao do seu Digimon!")
    
    # ===== PREVISOR (JA EXISTENTE) =====
    st.subheader("1. Preveja o Estagio do seu Digimon")
    
    st.markdown("""
    Preencha as estatisticas do seu Digimon no nivel 50 e descubra 
    em qual estagio ele vai evoluir.
    """)
    
    with st.form("form_evolucao"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Atributos (Nv. 50)")
            hp = st.slider("HP", 0, 2000, 1000, 10)
            sp = st.slider("SP", 0, 2000, 900, 10)
            atk = st.slider("Ataque", 0, 1000, 500, 10)
        
        with col2:
            st.subheader("Mais Atributos")
            df = st.slider("Defesa", 0, 1000, 500, 10)
            intel = st.slider("Inteligencia", 0, 1000, 500, 10)
            spd = st.slider("Velocidade", 0, 1000, 500, 10)
        
        st.subheader("Dados do Treinador")
        nome_digimon = st.text_input("Nome do seu parceiro:", "Agumon")
        
        if st.form_submit_button("Prever Evolucao"):
            estagio_previsto = prever_estagio(modelo, encoder, hp, sp, atk, df, intel, spd)
            
            st.balloons()
            st.success(f"""
            O Digimon {nome_digimon} vai evoluir para:
            {estagio_previsto.upper()}!
            """)
            
            # Mostrar a classificação do estágio
            classificacao = classificar_estagio(estagio_previsto)
            st.info(f"""
            **Classificacao:** {classificacao}
            
            **Estatisticas do {nome_digimon} (Nv. 50):**
            - HP: {hp}
            - SP: {sp}
            - Ataque: {atk}
            - Defesa: {df}
            - Inteligencia: {intel}
            - Velocidade: {spd}
            """)
    
    # ===== PLANO DE EVOLUCAO (NOVO) =====
    st.markdown("---")
    st.subheader("2. Plano de Evolucao - Qual caminho seguir?")
    
    st.markdown("""
    Escolha um Digimon inicial e o estagio que voce deseja alcancar.
    O sistema vai te mostrar o caminho completo de evolucao.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        digimon_inicial = st.text_input(
            "Digimon inicial:",
            placeholder="Ex: Agumon, Gabumon, etc."
        )
    
    with col2:
        estagio_desejado = st.selectbox(
            "Estagio desejado:",
            ["Baby", "In-Training", "Rookie", "Champion", "Ultimate", "Mega", "Ultra"]
        )
    
    if st.button("Gerar Plano de Evolucao"):
        if digimon_inicial:
            mostrar_plano_evolucao(digimon_inicial, estagio_desejado)
        else:
            st.warning("Digite o nome do Digimon inicial.")


# ============================================================
# FUNCOES AUXILIARES
# ============================================================

def classificar_estagio(estagio):
    """Classifica o estagio do Digimon em niveis de experiencia"""
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


def mostrar_plano_evolucao(digimon_inicial, estagio_desejado):
    """Mostra o plano de evolucao completo"""
    
    # Ordem dos estagios
    estagios_ordem = ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate', 'Mega', 'Ultra']
    
    # Verificar se o estagio desejado existe
    if estagio_desejado not in estagios_ordem:
        st.error(f"Estagio '{estagio_desejado}' nao reconhecido.")
        return
    
    # Simular um plano de evolucao (exemplo)
    plano = {
        'Baby': ['Baby'],
        'In-Training': ['Baby', 'In-Training'],
        'Rookie': ['Baby', 'In-Training', 'Rookie'],
        'Champion': ['Baby', 'In-Training', 'Rookie', 'Champion'],
        'Ultimate': ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate'],
        'Mega': ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate', 'Mega'],
        'Ultra': ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate', 'Mega', 'Ultra']
    }
    
    caminho = plano.get(estagio_desejado, [])
    
    if not caminho:
        st.warning(f"Nao foi possivel gerar um plano para {estagio_desejado}.")
        return
    
    # ===== EXIBIR O PLANO =====
    st.success(f"""
    **Plano de Evolucao para {digimon_inicial}**
    
    Objetivo: Alcancar o estagio {estagio_desejado.upper()}
    """)
    
    # Exibir o caminho passo a passo
    st.subheader("Caminho de Evolucao:")
    
    for i, estagio in enumerate(caminho):
        classificacao = classificar_estagio(estagio)
        
        # Icone visual para cada estagio
        if i == 0:
            icone = "🌱"
        elif i == len(caminho) - 1:
            icone = "⭐"
        else:
            icone = "➡️"
        
        col1, col2, col3 = st.columns([1, 3, 2])
        
        with col1:
            st.write(icone)
        with col2:
            st.write(f"**{estagio}**")
        with col3:
            st.write(f"*{classificacao}*")
        
        # Adicionar uma seta entre os estagios
        if i < len(caminho) - 1:
            st.write("⬇️")
    
    # ===== DICAS PARA CADA ESTAGIO =====
    st.subheader("Dicas para cada estagio:")
    
    dicas = {
        'Baby': "Foque em aumentar HP e resistencia. Treine batalhas contra oponentes fracos.",
        'In-Training': "Comece a treinar ataques basicos. Explore diferentes areas.",
        'Rookie': "Especialize-se em um atributo principal (ataque ou defesa).",
        'Champion': "Participe de batalhas mais dificeis. Procure itens de evolucao.",
        'Ultimate': "Treine em equipe. Evolua suas habilidades especiais.",
        'Mega': "Domine todas as habilidades. Enfrente os maiores desafios.",
        'Ultra': "Treinamento extremo. Prepare-se para batalhas lendarias."
    }
    
    for estagio in caminho:
        dica = dicas.get(estagio, "Continue treinando e evoluindo!")
        st.write(f"- **{estagio}:** {dica}")
    
    # ===== RECOMENDACAO DE ATRIBUTOS =====
    st.subheader("Recomendacao de atributos para cada estagio:")
    
    atributos_recomendados = {
        'Baby': "HP: 500+, Ataque: 100+",
        'In-Training': "HP: 700+, Ataque: 150+, Defesa: 100+",
        'Rookie': "HP: 900+, Ataque: 200+, Defesa: 150+",
        'Champion': "HP: 1200+, Ataque: 300+, Defesa: 200+",
        'Ultimate': "HP: 1500+, Ataque: 400+, Defesa: 300+",
        'Mega': "HP: 1800+, Ataque: 500+, Defesa: 400+",
        'Ultra': "HP: 2000+, Ataque: 600+, Defesa: 500+"
    }
    
    for estagio in caminho:
        rec = atributos_recomendados.get(estagio, "Treine todos os atributos!")
        st.write(f"- **{estagio}:** {rec}")
    
    st.info("""
    **Dica:** Use o Previsor de Evolucao (secao 1) para verificar se seu Digimon
    esta com as estatisticas necessarias para evoluir!
    """)