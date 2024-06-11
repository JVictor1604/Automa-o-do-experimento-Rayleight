import os
import serial
import serial.tools.list_ports
import time

# Verifica se a pasta 'dados' existe e a cria se necessário
if not os.path.exists('dados'):
    os.makedirs('dados')

# Definindo o número de amostras
numero_de_amostras = 2  # Defina o número de amostras desejado aqui

# Configurações da comunicação serial
BAUD_RATE = 9600
PORTA_SERIAL = input("Digite a porta serial à qual o Arduino está conectado (ex: COM3): ")

# Loop para fazer o número especificado de amostras
for numero_amostra in range(numero_de_amostras):
    print(f"Iniciando medição da amostra {numero_amostra + 1}")
    time.sleep(0.5)  # Pequeno atraso para estabilizar a comunicação serial
    NOME_DO_ARQUIVO = f'dados/amostra-{numero_amostra + 1}.txt'
    # Lista para armazenar as medições da amostra atual
    dados_amostra = []
    
    # Realiza as 50 medições para cada amostra
    for numero_medicao in range(50):
        # Inicia a comunicação serial
        with serial.Serial(PORTA_SERIAL, BAUD_RATE) as pserial:
            # Lê a porta serial, decodifica e limpa a string
            line = pserial.readline().decode('utf-8').rstrip().replace("Blue:","").replace("Red:","").replace("Green:","")
            # Exibe a leitura da porta serial no terminal Python
            print(line)
            # Adiciona a medição à lista de medições da amostra atual
            dados_amostra.append(line)
    
    # Escreve as medições da amostra atual em um arquivo
    with open(NOME_DO_ARQUIVO, 'w') as arquivo:
        for medição in dados_amostra:
            arquivo.write(medição + '\n')
