# Automação do experimento Rayleight / Projeto de Ciência de Dados 🖥️

## Descrição 📄

Este projeto faz parte da disciplina de **Prática em Ciência de Dados** ministrada pelo professor Dr. Leandro Nascimento Lemos na **ILUM - Escola de Ciência**. Utilizamos como base um experimento realizado no laboratório de física com o professor Dr James Moraes de Almeida. O código realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh, a fim de montar um gráfico interativo com a relação entre a cor original e a dispersão. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

## Pré-requisitos 🔍

- **Hardware:** 🛠️
  - Arduino (qualquer modelo compatível com comunicação serial)
  - Sensor de cor
  - Cabos de conexão


- **Software:** 🖥️
  - Bibliotecas Python: Bibliotecas
    [![pyserial](https://img.shields.io/badge/pyserial-Latest-green)](https://pypi.org/project/pyserial/)
    [![matplotlib](https://img.shields.io/badge/matplotlib-Latest-blue)](https://matplotlib.org/)
    [![numpy](https://img.shields.io/badge/numpy-Latest-orange)](https://numpy.org/)
    [![pandas](https://img.shields.io/badge/pandas-Latest-yellow)](https://pandas.pydata.org/)
    [![plotly](https://img.shields.io/badge/plotly-Latest-purple)](https://plotly.com/python/)
    [![time](https://img.shields.io/badge/time-Latest-red)](https://docs.python.org/3/library/time.html)
## Instalação 🔧

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/Otimiza-o_do_Espalhamento_Rayleight_PCD.git
   cd Otimiza-o_do_Espalhamento_Rayleight_PCD
   

2. **Instale as dependências Python:**

    ```bash
    pip install pyserial numpy pandas plotly
    

3. **Carregue o código no Arduino:**
   - Abra o aplicativo Arduíno IDE no seu computador
   - Execute o código **Arduino_Sensor_Luz**
   - Verifique qual número da porta USB em que seu arduíno está conectado
   - Após transferir o código para seu arduíno, feche o aplicativo Arduíno IDE

## Utilização

1.  Execute o script de medição:
     ```bash
     jupyter notebook main.ipynb

  O arquivo main.ipynb irá chamar mais três outros arquivos que, em conjunto, realizam a medição, tratamento de dados e plotagem do gráfico. Abaixo tem-se uma breve descrição do que cada um dos arquivos fará:

2. O arquivo **medição.py**:
   - Solicita o número de amostras que o usuário deseja fazer.
   - Solicita o número da porta USB em que o Arduino está conectado.
   - Lê os dados de cor (RGB) da porta serial.
   
  
3. O arquivo **tratamento_de_dados.py**:
    - Salva os dados coletados em arquivos de texto na pasta dados.
    - Calcula a média e o desvio padrão para cara cor RGB
   

4. O arquivo **plotar_grafico.py**:
   - Cálculo da curva de melhor ajuste
   - Plotagem dos dados e das curvas de melhor ajuste

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
