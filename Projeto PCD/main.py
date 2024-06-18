from medicao import medicao
from tratamento_de_dados import tratar_dados
<<<<<<< HEAD
from plotar_grafico import plotar_grafico

def main() :

    numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))

    medicao(numero_de_amostras)

    tratar_dados("dados", ",", numero_de_amostras)

    plotar_grafico(gotas, dadosblue, dadosred, dadosgreen)

=======

def main() :

    tratar_dados("dados", ",", medicao())
>>>>>>> 7dc0e77d82991478e1d03c1fc0a94045bf0754fe

main()