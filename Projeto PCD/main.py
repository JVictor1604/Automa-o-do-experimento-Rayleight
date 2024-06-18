from medicao import medicao
from tratamento_de_dados import tratar_dados
from plotar_grafico import plotar_grafico


def main() :
    while True:
        try:
            numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))
            if numero_de_amostras > 0:
                break
            else:
                print("Por favor, digite um número inteiro maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    medicao(numero_de_amostras)

    media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas = tratar_dados("dados", ",", numero_de_amostras)

    plotar_grafico(media_Azul, media_Verde, media_Vermelho, desvio_Azul, desvio_Verde, desvio_Vermelho, n_de_gotas)


main()