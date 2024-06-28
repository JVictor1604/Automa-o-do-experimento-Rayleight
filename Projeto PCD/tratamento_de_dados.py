def tratar_dados(caminho, separador_de_coluna, numero_de_amostras):
    import os 
    import glob as gb
    import pandas as pd
    import numpy as np
    padrao = os.path.join(caminho, "*.txt")
    gb.glob(padrao)
    conjunto_de_dados = gb.glob(padrao)

    contador = 0 
    media_Vermelho = [0]
    media_Verde = [0]
    media_Azul = [0]
    desvio_Vermelho = []
    desvio_Verde = []
    desvio_Azul = []

    while True:
            try:
                intervalo_de_gotas = int(input("Digite o intervalo de gotas adicionado em cada amostra: "))
                if intervalo_de_gotas > 0:
                    break
                else:
                    print("Por favor, digite um número inteiro maior que zero.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
    
    for arquivo in conjunto_de_dados:
        df = pd.read_csv(arquivo, delimiter = separador_de_coluna, names = ['Blue', 'Red', 'Green'], skiprows= 1)
        if contador == 0:
            media_Vermelho_referencia = df['Red'].mean()
            desvio_Vermelho.append(df['Red'].sem())
            media_Verde_referencia = df['Green'].mean()
            desvio_Verde.append(df['Green'].sem())
            media_Azul_referencia = df['Blue'].mean()
            desvio_Azul.append(df['Blue'].sem())
            contador +=1
        else :
            media_Vermelho_Unica = df['Red'].mean()
            media_Vermelho.append(media_Vermelho_Unica - media_Vermelho_referencia)
            desvio_Vermelho.append(df['Red'].sem())
            media_Verde_Unica = df['Green'].mean()
            media_Verde.append(media_Verde_Unica - media_Verde_referencia)
            desvio_Verde.append(df['Green'].sem())
            media_Azul_Unica = df['Blue'].mean()
            media_Azul.append(media_Azul_Unica - media_Azul_referencia)
            desvio_Azul.append(df['Blue'].sem())
 
    n_de_gotas = [ (i * intervalo_de_gotas) for i in range(numero_de_amostras)]

    return(media_Azul, media_Verde, media_Vermelho, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas)

    