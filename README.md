# Automação do experimento Rayleight / Projeto de Ciência de Dados 🖥️

## Descrição 📄

Este projeto faz parte da disciplina de **Prática em Ciência de Dados** ministrada pelo professor Dr. Leandro Nascimento Lemos na **ILUM - Escola de Ciência**. Utilizamos como base um experimento realizado no laboratório de física com o professor Dr James Moraes de Almeida. O código realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh, a fim de montar um gráfico interativo com a relação entre a cor original e a dispersão. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

O experimento investiga o efeito Rayleigh, que explica a dispersão da luz em meios transparentes com partículas muito menores que o comprimento de onda da luz visível. Um exemplo clássico desse fenômeno é a cor azul do céu, resultante da dispersão da luz solar pela atmosfera.

No nosso caso, utilizamos um sensor de cor acoplado a um Arduino para medir a intensidade das cores vermelho (R), verde (G) e azul (B) em uma solução inicial de água. A cada medição, adicionamos pequenas quantidades de leite à solução, tornando-a progressivamente mais turva. Isso aumenta a dispersão da luz e altera a intensidade das cores medidas.

O código coleta os dados do sensor e os transmite via porta serial para um computador, onde um script em Python processa e visualiza os resultados em um gráfico interativo.

## Pré-requisitos 🔍

- **Hardware:** 🛠️
  - Arduino (qualquer modelo compatível com comunicação serial)
  - Sensor de cor
  - Cabos de conexão

- **Software:** 🖥️
  - Bibliotecas Python:
    [![pyserial](https://img.shields.io/badge/pyserial-Latest-green)](https://pypi.org/project/pyserial/)
    [![matplotlib](https://img.shields.io/badge/matplotlib-Latest-blue)](https://matplotlib.org/)
    [![numpy](https://img.shields.io/badge/numpy-Latest-orange)](https://numpy.org/)
    [![pandas](https://img.shields.io/badge/pandas-Latest-yellow)](https://pandas.pydata.org/)
    [![plotly](https://img.shields.io/badge/plotly-Latest-purple)](https://plotly.com/python/)
    [![time](https://img.shields.io/badge/time-Latest-red)](https://docs.python.org/3/library/time.html)

## Instalação 🔧

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/JVictor1604/Otimiza-o_do_Espalhamento_Rayleight_PCD.git
   
   # Entre na pasta
   cd Otimiza-o_do_Espalhamento_Rayleight_PCD


2. **Instale as dependências Python:**

    ```bash
    pip install pyserial numpy pandas plotly
    

3. **Carregue o código no Arduino:**
   - Abra o aplicativo Arduíno IDE no seu computador
   - Execute o código **Arduino_Sensor_Luz**
   - Verifique qual número da porta USB em que seu arduíno está conectado
   - Após transferir o código para seu arduíno, feche o aplicativo Arduíno IDE

     *!!Atenção, caso o aplicativo do Arduino esteja aberto enquanto o script estiver rodando, ele não conseguirá se conectar com a porta serial*
  
  
  4. **Código do Arduino 🎛️**
  O sensor de cor utilizado no experimento funciona com base no TCS3200, que converte a intensidade de luz de diferentes cores em sinais de frequência. O código abaixo configura os pinos do Arduino e lê os valores das cores vermelho, verde e azul, enviando-os via porta serial para o computador:

   **Funcionamento do código do Arduino**
    o código configura os pinos do sensor e define a comunicação serial com o computador.
    Para cada canal de cor (R, G, B), o Arduino seleciona os fotodiodos correspondentes, mede a intensidade da cor através do sinal pulseIn(out, LOW).



Este código pode ser executado de duas maneiras: utilizando Python puro ou Jupyter Notebook. Ambas as abordagens realizarão as mesmas tarefas, mas você pode escolher a que for mais conveniente para você.


## 1. Executando no VS Code com Extensão Jupyter 🖥️
Se você preferir usar o Visual Studio Code (VS Code), pode instalar a extensão Jupyter, que oferece uma experiência similar ao Jupyter Notebook diretamente dentro do editor de código.

- Passo 1: Instalar a Extensão Jupyter para VS Code:
  
Abra o Visual Studio Code.
Vá até a aba de extensões (ícone de quadrado no menu lateral esquerdo).
Procure por "Jupyter" e instale a extensão oficial de Jupyter (desenvolvida pela Microsoft).

- Passo 2: Abrir o Notebook no VS Code:
  
Após instalar a extensão, você pode abrir o arquivo main.ipynb diretamente no VS Code. A extensão Jupyter permitirá que você execute as células do notebook de maneira interativa, da mesma forma que faria no Jupyter tradicional.

## 2.  executando em Python Puro 🖥️
     ```bash
     python main.py
     


# Funcionamento 🔧

O arquivo main irá chamar três outros arquivos que, em conjunto, realizam a medição, o tratamento de dados e a plotagem do gráfico. O usuário pode escolher entre iniciar uma nova medição ou plotar gráficos utilizando dados que já estão salvos em uma pasta existente.

A interface do usuário permite que o usuário escolha entre duas opções:

1- Realizar uma nova medição:
Se o usuário optar por essa opção, o código irá medir os dados, tratá-los e gerar o gráfico automaticamente.

2- Plotar gráfico com dados já existentes:
Se houver dados salvos anteriormente, o código irá carregar esses dados, tratá-los e gerar o gráfico.

Abaixo, uma breve descrição do que cada um dos arquivos fará:

1. O arquivo **medição.py**:
   - Solicita o número de amostras que o usuário deseja fazer.
   - Solicita o número da porta USB em que o Arduino está conectado.
   - Lê os dados de cor (RGB) da porta serial.
   
2. O arquivo **tratamento_de_dados.py**:
    - Salva os dados coletados em arquivos de texto na pasta dados.
    - Calcula a média e o desvio padrão para cada cor RGB

3. O arquivo **plotar_grafico.py**:
   - Cálculo da curva de melhor ajuste
   - Plotagem dos dados e das curvas de melhor ajuste

Todo esse código está integrado no arquivo `main` que será executado.

## Contribuição

Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para a sua feature (\`git checkout -b feature/nova-feature\`).
3. Commit suas alterações (\`git commit -am 'Adiciona nova feature'\`).
4. Push para o branch (\`git push origin feature/nova-feature\`).
5. Crie um novo Pull Request.

## Colaboradores

<div align="center">
  <table>
    <tr>
      <td align="center" style="border: 2px solid purple; padding: 10px;">
        <img src="Projeto PCD/imagens/ana.jpeg" alt="Ana Luiza" width="100" height="100" style="border-radius: 50%;"><br>
        <sub><span style="font-size: 16px; color: purple; font-weight: bold;">Ana Luiza</span></sub>
      </td>
      <td align="center" style="border: 2px solid purple; padding: 10px;">
        <img src="Projeto PCD/imagens/marco.jpeg" alt="Marco Tulio" width="100" height="100" style="border-radius: 50%;"><br>
        <sub><span style="font-size: 16px; color: purple; font-weight: bold;">Marco Tulio</span></sub>
      </td>
      <td align="center" style="border: 2px solid purple; padding: 10px;">
        <img src="Projeto PCD/imagens/yasmin.jpeg" alt="Yasmin" width="100" height="100" style="border-radius: 50%;"><br>
        <sub><span style="font-size: 16px; color: green; font-weight: bold;">Yasmin</span></sub>
      </td>
      <td align="center" style="border: 2px solid purple; padding: 10px;">
        <img src="Projeto PCD/imagens/jose.jpeg" alt="José Victor" width="100" height="100" style="border-radius: 50%;"><br>
        <sub><span style="font-size: 16px; color: purple; font-weight: bold;">José Victor</span></sub>
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center" style="margin-top: 20px;">
  <sub><span style="font-size: 14px; color: gray;">README.md criado com a ajuda de <a href="https://openai.com/chatgpt" target="_blank">ChatGPT</a>.</span></sub>
  <br>

## Papel dos colaboradores
</div>

- Ana Luiza: Desenvolvimento do código de plotagem do gráfico e da apresentação.
- Marco Tulio: Desenvolvimento do Código de tratamento de Dados e da função Main.
- Yasmin: Desenvolvimento do código de plotagem do gráfico e da apresentação.
- José Victor: Desenvolvimento do código de medição associado ao arduino, da função Main e criação do github.


<br>

  

<p align="center">
  <img src="https://github.com/JVictor1604/Otimiza-o_do_Espalhamento_Rayleight_PCD/assets/171518829/fe1b443f-1c9e-42f2-88e8-85e1b4400fd0" alt="Descrição da imagem">
</p>

## Licença
Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
EOF
