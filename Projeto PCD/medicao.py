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
        if(numero_amostra == 0) :
            str(input("Pressione Enter para iniciar as medições"))
        print(f"Iniciando medição da amostra {numero_amostra + 1}")
        time.sleep(0.5)  # Pequeno atraso para estabilizar a comunicação serial
        NOME_DO_ARQUIVO = f'dados/amostra-{numero_amostra + 1:02d}.txt'
        # Lista para armazenar as medições da amostra atual
        dados_amostra = []
    
        with serial.Serial(PORTA_SERIAL, BAUD_RATE) as pserial:
            for numero_medicao in range(51):
                line = pserial.readline().decode('utf-8').rstrip().replace("Blue:", "").replace("Red:", "").replace("Green:", "")
                print(line)
                dados_amostra.append(line)
        if numero_amostra  != num_amostras - 1:
            input("Pressione Enter para ir a próxima medição...")      
        yield NOME_DO_ARQUIVO, dados_amostra

def criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras):
    # Escreve as medições da amostra atual em um arquivo
    with open(nome_do_arquivo, 'w') as arquivo:
        for medicao in dados_das_amostras:
            arquivo.write(medicao + '\n')

def medicao(num_de_amostras):
    while True:
        try:
            Numero_da_Porta_Serial = int(input("Digite a porta serial à qual o Arduino está conectado (ex: 11): "))
            Porta_Serial = f"COM{Numero_da_Porta_Serial}"
            
            # Tentar abrir a porta serial
            ser = serial.Serial(Porta_Serial)
            ser.close()
            
            print(f"Conectado com sucesso na porta {Porta_Serial}")
            break
        except ValueError:
            print("Por favor, digite um número de porta válido.")
        except serial.SerialException:
            print("Erro ao tentar conectar. Por favor, verifique se a porta está correta e tente novamente.")

    for nome_do_arquivo, dados_das_amostras in medir_amostra(num_de_amostras, BAUD_RATE=9600, PORTA_SERIAL=Porta_Serial):
        criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras)

