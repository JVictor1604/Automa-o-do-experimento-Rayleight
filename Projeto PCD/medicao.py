import os
import serial
import serial.tools.list_ports
import time
import shutil

def criar_pasta(nome_pasta):
    """Cria uma pasta com o nome fornecido pelo usuário."""
    if os.path.exists(nome_pasta):
        shutil.rmtree(nome_pasta)
    os.makedirs(nome_pasta)

def medir_amostra(num_amostras, BAUD_RATE, PORTA_SERIAL, nome_pasta):
    """Realiza a medição das amostras e retorna os dados capturados."""
    for numero_amostra in range(1, num_amostras + 1):
        if numero_amostra == 1:
            input("Pressione Enter para iniciar as medições...")

        print(f"Iniciando medição da amostra {numero_amostra}.")
        time.sleep(0.5)

        NOME_DO_ARQUIVO = os.path.join(nome_pasta, f'amostra-{numero_amostra:02d}.txt')
        dados_amostra = []

        with serial.Serial(PORTA_SERIAL, BAUD_RATE) as pserial:
            for _ in range(51):
                line = pserial.readline().decode('utf-8').rstrip().replace("Blue:", "").replace("Red:", "").replace("Green:", "")
                print(line)
                dados_amostra.append(line)

        if numero_amostra != num_amostras:
            input("Pressione Enter para ir à próxima medição...")

        yield NOME_DO_ARQUIVO, dados_amostra

def criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras):
    """Cria um arquivo e salva as medições."""
    with open(nome_do_arquivo, 'w') as arquivo:
        for medicao in dados_das_amostras:
            arquivo.write(medicao + '\n')

def medicao(num_de_amostras):
    """Configura a porta serial e inicia a medição das amostras."""
    while True:
        try:
            Numero_da_Porta_Serial = int(input("Digite a porta serial à qual o Arduino está conectado (ex: 11): "))
            Porta_Serial = f"COM{Numero_da_Porta_Serial}"
            
            ser = serial.Serial(Porta_Serial)
            ser.close()

            print(f"Conectado com sucesso na porta {Porta_Serial}")
            break
        except ValueError:
            print("Por favor, digite um número de porta válido.")
        except serial.SerialException:
            print("Erro ao tentar conectar. Verifique se a porta está correta e tente novamente.")

    # Solicita o nome da pasta onde os dados serão armazenados
    while True:
        nome_pasta = input("Digite o nome da pasta para salvar os dados: ")
        if nome_pasta.strip():  # Verifica se o nome não está vazio
            # Verifica se o nome da pasta contém caracteres inválidos
            if any(char in nome_pasta for char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']):
                print("Nome de pasta contém caracteres inválidos. Tente novamente.")
            else:
                criar_pasta(nome_pasta)
                break
        else:
            print("Por favor, digite um nome válido para a pasta.")

    for nome_do_arquivo, dados_das_amostras in medir_amostra(num_de_amostras, BAUD_RATE=9600, PORTA_SERIAL=Porta_Serial, nome_pasta=nome_pasta):
        criar_arquivo_com_medicoes(nome_do_arquivo, dados_das_amostras)

    # Retorna o nome da pasta onde os dados foram armazenados
    return nome_pasta
