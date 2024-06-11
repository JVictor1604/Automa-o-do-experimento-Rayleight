# Projeto de PCD com Arduino e Python

## Descrição

Este projeto realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh visto durante o experimento do professor James. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

## Pré-requisitos

- **Hardware:**
  - Arduino (qualquer modelo compatível com comunicação serial)
  - Sensor de cor
  - Cabos de conexão

- **Software:**
  - Python 3.x
  - Bibliotecas Python: `pyserial`, `matplotlib`, `numpy`

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/projeto-pcd.git
   cd projeto-pcd

2. **Instale as dependências Python:**

    ```bash
    pip install pyserial plotly numpy glob pandas os

3. **Carregue o código no Arduino:**


4. **Utilização**
   
    Executar o script de medição
    Conecte o Arduino ao computador.
   
    Execute o script de medição:
   ```bash
   python medicao.py

  O script irá:

  Solicitar o número de amostras que você deseja fazer.
  Tentar identificar automaticamente a porta do Arduino.
  Ler os dados de cor (RGB) da porta serial.
  Salvar os dados coletados em arquivos de texto na pasta dados.
  Processar os dados coletados
  Após a coleta de dados, os dados serão processados utilizando o script tratamento_de_dados.py.

  Gerar gráficos
  Para visualizar os dados, utilize o script plotar_grafico.py para gerar gráficos a partir dos dados processados.



  ## Contribuição
  Se você deseja contribuir com este projeto, siga os passos abaixo:

  1- Faça um fork do repositório.
  2- Crie um branch para a sua feature (git checkout -b feature/nova-feature).
  3- Commit suas alterações (git commit -am 'Adiciona nova feature').
  4- Push para o branch (git push origin feature/nova-feature).
  6- Crie um novo Pull Request.
   
