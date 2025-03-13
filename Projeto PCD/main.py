from medicao import medicao
from tratamento_de_dados import tratar_dados
from plotar_grafico import plotar_grafico
from colorama import Fore, Back, Style, init
import os

 

def main() :

    while True:

        init(autoreset=True)
        
        print(Fore.GREEN + Style.BRIGHT + "="*40)  # Borda superior
        print(Fore.YELLOW + Style.BRIGHT + "   Digite 1 para realizar uma nova medição   ")
        print(Fore.YELLOW + Style.BRIGHT + "   Digite 2 para plotar gráfico com dados já existentes   ")
        print(Fore.GREEN + Style.BRIGHT + "="*40)  # Borda inferior

        numero_acao = int(input(Fore.CYAN + "Digite o número da ação desejada: "))


        if numero_acao == 1:

            while True:
                try:
                    numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))
                    if numero_de_amostras > 0:
                        break
                    else:
                        print("Por favor, digite um número inteiro maior que zero.")
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")
            
            nome_pasta = medicao(numero_de_amostras)
            
            media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas = tratar_dados(f"{nome_pasta}", ",", numero_de_amostras)

            plotar_grafico(media_Azul, media_Verde, media_Vermelho, desvio_Azul, desvio_Verde, desvio_Vermelho, n_de_gotas)
        
        elif numero_acao == 2:
            
            nome_pasta = input("Digite o nome da pasta onde estão os arquivos: ")  

            while os.path.exists(nome_pasta) == False:
                  nome_pasta = input("Digite um nome de pasta válido: ")
                  
            while True:
                    try:
                        numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))
                        if numero_de_amostras > 0:
                            break
                        else:
                            print("Por favor, digite um número inteiro maior que zero.")
                    except ValueError:
                        print("Por favor, digite um número inteiro válido.")

            media_Azul, media_Vermelho, media_Verde, desvio_Azul, desvio_Vermelho, desvio_Verde, n_de_gotas = tratar_dados(f"{nome_pasta}", ",", numero_de_amostras)
              
            plotar_grafico(media_Azul, media_Verde, media_Vermelho, desvio_Azul, desvio_Verde, desvio_Vermelho, n_de_gotas)

        else: break


main()