import os
import serial
import serial.tools.list_ports

def identificar_porta_arduino():
    """
    Retorna a porta COM fornecida pelo usuário.
    """
    porta = input("Digite a porta COM à qual o Arduino está conectado (ex: COM3): ")
    return porta

def ler_dado_serial(porta_serial):
    """
    Lê um dado da porta serial e retorna a linha formatada.
    """
    BAUD_RATE = 9600  # Definindo a taxa de baud como 9600
    with serial.Serial(porta_serial, BAUD_RATE, timeout=1) as pserial:
        # Certifique-se de que há um timeout para que não fique esperando indefinidamente por dados
        line = pserial.readline().decode('utf-8').rstrip()
        return line
with open(nome_do_arquivo, 'a') as arquivo:
        arquivo.write(dado + '\n')

def main():
    # Criar a pasta 'dados' se ela não existir
    if not os.path.exists('dados'):
        os.makedirs('dados')

    numero_arquivo = 1
    numero_de_amostras = int(input("Digite o número de amostras que você deseja fazer: "))

    # Solicitar ao usuário que insira a porta COM à qual o Arduino está conectado
    PORTA_SERIAL = identificar_porta_arduino()

    for i in range(numero_de_amostras):
        NOME_DO_ARQUIVO = f'dados/medida_espalhamento-{numero_arquivo}.txt'
        dado = ler_dado_serial(PORTA_SERIAL)
        print(dado)  # Imprimir o dado lido da porta serial
        salvar_dado_em_arquivo(NOME_DO_ARQUIVO, dado)
        numero_arquivo += 1

if __name__ == "__main__":
    main()
