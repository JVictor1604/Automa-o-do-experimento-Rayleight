Projeto de PCD com Arduino e Python
Descrição
Este projeto realiza medições de cor utilizando um sensor conectado ao Arduino para verificar o efeito Rayleigh. Os dados de cor (RGB) são coletados pelo Arduino e enviados para um computador via porta serial. Um script Python é utilizado para ler os dados da porta serial, processá-los e salvá-los em arquivos de texto.

Pré-requisitos
Hardware:

Arduino (qualquer modelo compatível com comunicação serial)
Sensor de cor
Cabos de conexão
Software:

Python 3.x
Bibliotecas Python: pyserial, matplotlib, numpy
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seuusuario/projeto-pcd.git
cd projeto-pcd
Instale as dependências Python:

bash
Copiar código
pip install pyserial matplotlib numpy
Carregue o código no Arduino:

cpp
Copiar código
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "ID") {
      Serial.println("ARDUINO");
    }
  }
}
Utilização
Executar o script de medição
Conecte o Arduino ao computador.

Execute o script de medição:

bash
Copiar código
python medicao.py
O script irá:

Solicitar o número de amostras que você deseja fazer.
Tentar identificar automaticamente a porta do Arduino.
Ler os dados de cor (RGB) da porta serial.
Salvar os dados coletados em arquivos de texto na pasta dados.
Processar os dados coletados
Após a coleta de dados, você pode processar os dados utilizando o script tratamento_de_dados.py.

Gerar gráficos
Para visualizar os dados, utilize o script plotar_grafico.py para gerar gráficos a partir dos dados processados.

Contribuição
Se você deseja contribuir com este projeto, siga os passos abaixo:

Faça um fork do repositório.
Crie um branch para a sua feature (git checkout -b feature/nova-feature).
Commit suas alterações (git commit -am 'Adiciona nova feature').
Push para o branch (git push origin feature/nova-feature).
Crie um novo Pull Request.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

