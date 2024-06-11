#!pip uninstall serial
#}!pip install pySerial
import serial
# Lembrar de alterar o nome do arquivo sempre que iniciar um experimento novo
NOME_DO_ARQUIVO = 'medida_espalhamento-31.txt'
# Usar aqui o mesmo valor da velocidade de comunicação usada para iniciar a
# comunicação serial no Arduino
BAUD_RATE = 9600
# Alterar o nome da porta serial para a porta onde o Arduino está conectado
PORTA_SERIAL = 'COM15' # usar esta notação caso esteja no windows
#PORTA_SERIAL = r'/dev/ttyACM0' # usar esta notação caso esteja no linux

# loop infinito
#while True:
for i in range(0,50):
    # iniciando comunicação serial
    with serial.Serial(PORTA_SERIAL, BAUD_RATE) as pserial:
        # lendo a porta serial, decodificando e limpando a string
        line = pserial.readline().decode('utf-8').rstrip().replace("Blue:","").replace("Red:","").replace("Green:","")
        # exibindo a leitura da porta serial no terminal Python
        print(line)
        # escrevendo resultado em um arquivo
        with open(NOME_DO_ARQUIVO, 'a') as arquivo:
            arquivo.write(line + '\n')


