import os
import serial
import serial.tools.list_ports
import time

# Verifica se a pasta 'dados' existe e a cria se necessário
if not os.path.exists('dados'):
    os.makedirs('dados')

def medir_amostra(num_amostras, BAUD_RATE, PORTA_SERIAL):
    """Cria um arquivo txt para armazenar os dados e inicia a medição de cada amostra, que será registrada 50 vezes"""
    for numero_amostra in range(num_amostras):
        print(f"Iniciando medição da amostra {numero_amostra + 1}")
        time.sleep(0.5)  # Pequeno atraso para estabilizar a comunicação serial
        NOME_DO_ARQUIVO = f'dados/amostra-{numero_amostra + 1}.txt'
        # Lista para armazenar as medições da amostra atual
        dados_amostra = []
        
        # Inicia a comunicação serial uma vez por amostra
        with serial.Serial(PORTA_SERIAL, BAUD_RATE) as pserial:
            # Realiza as 50 medições para cada amostra
            for numero_medicao in range(50):
                # Lê a porta serial, decodifica e limpa a string
                line = pserial.readline().decode('utf-8').rstrip().replace("Blue:", "").replace("Red:", "").replace("Green:", "")
                # Exibe a leitura da porta serial no terminal Python
                print(line)
                # Adiciona a medição à lista de medições da amostra atual
                dados_amostra.append(line)
        
        # Retorna o nome do arquivo e os dados da amostra
        yield NOME_DO_ARQUIVO, dados_amostra

def criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras):
    # Escreve as medições da amostra atual em um arquivo
    with open(nome_do_arquivo, 'w') as arquivo:
        for medicao in dados_das_amostras:
            arquivo.write(medicao + '\n')

def medicao():
    # Definindo o número de amostras
    numero_de_amostras = int(input("Defina o Número de Amostras Desejadas: "))
    Numero_da_Porta_Serial = int(input("Digite a porta serial à qual o Arduino está conectado (ex: 11): "))
    Porta_Serial = f"COM{Numero_da_Porta_Serial}"

    # Executa a medição e cria os arquivos
    for nome_do_arquivo, dados_das_amostras in medir_amostra(numero_de_amostras, BAUD_RATE=9600, PORTA_SERIAL=Porta_Serial):
        criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras)

medicao()
