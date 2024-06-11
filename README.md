# Projeto de PCD com Arduino e Python

## Descrição

Este projeto faz parte da disciplina de **Prática em Ciência de Dados** ministrada pelo professor Dr. Leandro Nascimento Lemos na **ILUM - Escola de Ciência**. Utilizamos como base um experimento realizado no laboratório de física com o professor Dr James Moraes de Almeida. O código realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh, a fim de montar um gráfico interativo com a relação entre a cor original e a dispersão. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

## Pré-requisitos

- **Hardware:**
  - Arduino (qualquer modelo compatível com comunicação serial)
  - Sensor de cor
  - Cabos de conexão

- **Software:**
  - ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
  - Bibliotecas Python: ![pyserial](https://img.shields.io/badge/pyserial-Latest-green) ![matplotlib](https://img.shields.io/badge/matplotlib-Latest-blue) ![numpy](https://img.shields.io/badge/numpy-Latest-orange)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/projeto-pcd.git
   cd projeto-pcd
   

2. **Instale as dependências Python:**

    ```bash
    pip install pyserial matplotlib numpy
    

3. **Carregue o código no Arduino:**
   [Instruções de como carregar o código no Arduino]

## Utilização

1. Conecte o Arduino ao computador.

2. Execute o script de medição:
   ```bash
   python medicao.py
  

  O script irá:
   - Solicitar o número de amostras que você deseja fazer.
   - Tentar identificar automaticamente a porta do Arduino.
   - Ler os dados de cor (RGB) da porta serial.
   - Salvar os dados coletados em arquivos de texto na pasta dados.

3. Processar os dados coletados:
   ```bash
   python tratamento_de_dados.py
   

4. Gerar gráficos:
   ```bash
   python plotar_grafico.py

  Para visualizar os dados, utiliza-se o script \`plotar_grafico.py\` para gerar gráficos a partir dos dados processados.

## Contribuição

Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie um branch para a sua feature (\`git checkout -b feature/nova-feature\`).
3. Commit suas alterações (\`git commit -am 'Adiciona nova feature'\`).
4. Push para o branch (\`git push origin feature/nova-feature\`).
5. Crie um novo Pull Request.

## Colaboradores
- Ana Luiza: Implementação da função de medição do sensor de cor RGB.
- Marco Tulio: Desenvolvimento do código Arduino para comunicação com o sensor e envio de dados pela porta serial.
- Yasmin: Desenvolvimento da interface e interação com o usuário.
- José Victor: Implementação da função de análise e visualização dos dados.

## Licença
Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
EOF
