import os
import glob as gb
import pandas as pd
import numpy as np

def tratar_dados(caminho, separador_de_coluna, numero_de_amostras):
    """
    Processa os arquivos de medição e retorna as médias e desvios para cada canal de cor,
    considerando o número fixo de gotas informado pelo usuário.
    """
    padrao = os.path.join(caminho, "*.txt")
    conjunto_de_dados = sorted(gb.glob(padrao))

    if not conjunto_de_dados:
        print("Nenhum arquivo de medição encontrado no diretório especificado.")
        return [], [], [], [], [], [], []  # Retorna listas vazias
    
    while True:
        try:
            intervalo_de_gotas = int(input("Digite o intervalo de gotas adicionado em cada amostra: "))
            if intervalo_de_gotas > 0:
                break
            else:
                print("Por favor, digite um número inteiro maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    media_Vermelho = [0]
    media_Verde = [0]
    media_Azul = [0]
    desvio_Vermelho = []
    desvio_Verde = []
    desvio_Azul = []
    
    contador = 0
    for arquivo in conjunto_de_dados:
        try:
            df = pd.read_csv(arquivo, delimiter=separador_de_coluna, names=['Blue', 'Red', 'Green'], skiprows=1)
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")
            continue
        
        if df.empty or any(col not in df.columns for col in ['Blue', 'Red', 'Green']):
            print(f"Dados inválidos no arquivo {arquivo}. Pulando para o próximo.")
            continue
        
        if contador == 0:
            media_Vermelho_referencia = df['Red'].mean()
            desvio_Vermelho.append(df['Red'].sem())
            media_Verde_referencia = df['Green'].mean()
            desvio_Verde.append(df['Green'].sem())
            media_Azul_referencia = df['Blue'].mean()
            desvio_Azul.append(df['Blue'].sem())
            contador += 1
        else:
            media_Vermelho_Unica = df['Red'].mean()
            media_Vermelho.append(media_Vermelho_Unica - media_Vermelho_referencia)
            desvio_Vermelho.append(df['Red'].sem())
            
            media_Verde_Unica = df['Green'].mean()
            media_Verde.append(media_Verde_Unica - media_Verde_referencia)
            desvio_Verde.append(df['Green'].sem())
            
            media_Azul_Unica = df['Blue'].mean()
            media_Azul.append(media_Azul_Unica - media_Azul_referencia)
            desvio_Azul.append(df['Blue'].sem())
    
    n_de_gotas = [i * intervalo_de_gotas for i in range(numero_de_amostras)]

    return media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas
