def projeto (caminho, N_de_gotas):
    import os
    import glob as gb
    import pandas as pd
    import numpy as np
    
    Padrão = caminho
    gb.glob(padrão)
    conjunto_de_dados = gb.glob(padrão)
    
    
    contador = 0 
    media_Vermelho = []
    media_Verde = []
    media_Azul = []
    desvio_Vermelho = []
    desvio_Verde = []
    desvio_Azul = []
    
    for arquivo in conjunto_de_dados:
        dataframe = pd.read_csv(arquivo, )