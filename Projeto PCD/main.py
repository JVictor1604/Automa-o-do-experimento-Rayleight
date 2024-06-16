from medicao import medicao
from tratamento_de_dados import tratar_dados
from plotar_grafico import plotar_grafico

def main() :

    numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))

    medicao(numero_de_amostras)

    tratar_dados("dados", ",", numero_de_amostras)

    plotar_grafico(gotas, dadosblue, dadosred, dadosgreen)


main()