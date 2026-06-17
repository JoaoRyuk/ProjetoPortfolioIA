# utils/funcoes.py
import pandas as pd
import joblib

def carregar_modelos():
    """Carrega o modelo, encoder e lista de nomes"""
    modelo = joblib.load('modelo_digimon.pkl')
    encoder = joblib.load('label_encoder_digimon.pkl')
    nomes = joblib.load('nomes_digimons.pkl')
    return modelo, encoder, nomes

def carregar_dados():
    """Carrega os dados do CSV"""
    return pd.read_csv('Digimon.csv', sep=';')

def prever_estagio(modelo, encoder, hp, sp, atk, df, intel, spd):
    """Preve o estágio do Digimon baseado nas estatísticas"""
    entrada = pd.DataFrame([[hp, sp, atk, df, intel, spd]], 
                          columns=['HP lvl 50', 'SP lvl 50', 'ATK lvl 50', 'DEF lvl 50', 'INT lvl 50', 'SPD lvl 50'])
    previsao_num = modelo.predict(entrada)[0]
    estagio = encoder.inverse_transform([previsao_num])[0]
    return estagio