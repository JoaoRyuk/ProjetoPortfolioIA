# Digimon Master - Portal de Evoluções com IA

![Digimon Master](https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/Digimon_Adventure_logo.png/220px-Digimon_Adventure_logo.png)

---

## 📖 Sobre o Projeto

**Digimon Master** é um portal interativo que utiliza **Machine Learning** para prever a evolução de Digimons com base em suas estatísticas. O projeto foi desenvolvido como portfólio para demonstrar habilidades em Python, análise de dados, machine learning e desenvolvimento de interfaces web.

**🎯 Objetivo:** Ajudar treinadores de Digimon a entenderem qual será o estágio de evolução do seu Digimon (Baby, In-Training, Rookie, Champion, Ultimate, Mega, Ultra) com base em atributos como HP, Ataque, Defesa, Velocidade, entre outros.

**🧠 Machine Learning:**
- **Algoritmo:** Random Forest Classifier
- **Acurácia:** 80.88%
- **Características:** 6 atributos (HP, SP, ATK, DEF, INT, SPD)
- **Classes:** 8 estágios de evolução

---

## 🚀 Funcionalidades

### 📊 Dashboard
- Estatísticas gerais dos Digimons
- Gráfico de distribuição por estágio
- Gráficos de dispersão (Ataque vs Defesa, Velocidade vs Inteligência)
- Ranking dos 10 Digimons mais fortes

### ⚔️ Previsor de Evolução
- Ajuste de estatísticas com sliders (HP, SP, Ataque, Defesa, Inteligência, Velocidade)
- Previsão do estágio de evolução com classificação
- Exibição das estatísticas do Digimon

### 💬 Chat IA (Assistente Virtual)
- Perguntas sobre Digimons
- Respostas baseadas nos dados:
  - Quais são os Digimons mais fortes?
  - Informações sobre o Agumon
  - Médias de atributos
  - Total de Digimons

### 🔍 Pesquisa e Recomendações
- Busca por nome de Digimon com sugestões
- Lista completa de todos os Digimons
- Recomendações por categoria (Ataque, Defesa, Velocidade, etc.)
- Caminho de evolução para um Digimon específico

---

## 🛠️ Tecnologias Utilizadas

### Linguagem
- **Python 3.9+**

### Bibliotecas
| Biblioteca | Função |
|------------|--------|
| **Streamlit** | Criação da interface interativa |
| **Pandas** | Manipulação e análise de dados |
| **Scikit-learn** | Machine Learning (Random Forest) |
| **Joblib** | Persistência de modelos treinados |

### Infraestrutura
- **GitHub**: Versionamento do código
- **Streamlit Cloud**: Deploy da aplicação

---

### 2. Criar um Ambiente Virtual

- python -m venv venv

**Ativar o ambiente virtual:**

- Windows:

venv\Scripts\activate

- Linux/Mac:

source venv/bin/activate

### 3. Instalar Dependências

pip install -r requirements.txt

### 4. Treinar o Modelo

python treinar_digimon.py

- Saída esperada:

text
==================================================
INICIANDO TREINAMENTO DO MODELO DIGIMON
==================================================
Carregando dados dos Digimons...
Total de Digimons no dataset: 341
Digimons apos limpeza: 339
Acurcia do modelo: 80.88%
Modelo salvo como 'modelo_digimon.pkl'
==================================================
TREINAMENTO CONCLUIDO COM SUCESSO!
==================================================

### 5. Executar a Aplicação

streamlit run app.py

### 6. Acessar

Abra o navegador em: http://localhost:8501
---

### A aplicação está disponível publicamente em:

🔗 Streamlit Cloud: https://projeto-portfolio-ia.streamlit.app/
