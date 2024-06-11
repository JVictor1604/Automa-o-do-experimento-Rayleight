# Projeto de PCD com Arduino e Python

## Descrição

Este projeto realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

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
