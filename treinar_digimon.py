# treinar_digimon.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

print("="*50)
print("INICIANDO TREINAMENTO DO MODELO DIGIMON")
print("="*50)

if not os.path.exists('Digimon.csv'):
    print("ERRO: Arquivo 'Digimon.csv' nao encontrado!")
    exit()

print("Carregando dados dos Digimons...")
digimons = pd.read_csv('Digimon.csv', sep=';')

print(f"Total de Digimons no dataset: {len(digimons)}")

colunas_caracteristicas = ['HP lvl 50', 'SP lvl 50', 'ATK lvl 50', 'DEF lvl 50', 'INT lvl 50', 'SPD lvl 50']
coluna_alvo = 'Stage'

print("\nLimpando dados...")
digimons_limpos = digimons.dropna(subset=colunas_caracteristicas + [coluna_alvo])
print(f"Digimons apos limpeza: {len(digimons_limpos)}")

X = digimons_limpos[colunas_caracteristicas]
y = digimons_limpos[coluna_alvo]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

joblib.dump(label_encoder, 'label_encoder_digimon.pkl')
print("\nEstagios codificados:")
for i, stage in enumerate(label_encoder.classes_):
    print(f"   {stage} = {i}")

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

print("\nTreinando o modelo Random Forest...")
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_treino, y_treino)

acuracia = modelo.score(X_teste, y_teste)
print(f"Acurcia do modelo: {acuracia:.2%}")

joblib.dump(modelo, 'modelo_digimon.pkl')
print("Modelo salvo como 'modelo_digimon.pkl'")

nomes_digimons = digimons_limpos['Digimon'].tolist()
joblib.dump(nomes_digimons, 'nomes_digimons.pkl')
print("Lista de nomes salva em 'nomes_digimons.pkl'")

print("\n" + "="*50)
print("TREINAMENTO CONCLUIDO COM SUCESSO!")
print("="*50)