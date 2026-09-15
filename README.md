# CP02-1EMA-2SEM-CTFE
# ESP32 com MicroPython: Display LCD 20x4, API OpenWeather e Comunicação MQTT

Este repositório contém a implementação do projeto prático de Internet das Coisas (IoT) utilizando a placa ESP32 programada em MicroPython. O projeto aborda a integração de exibição em display LCD 20x4 I2C, requisição HTTP REST para a API da OpenWeather, e publicação de dados de telemetria via protocolo MQTT para consumo no Node-RED.

---

## Fluxo de Dados e Arquitetura

O sistema opera de acordo com o seguinte fluxo integrado:

OpenWeather API -> ESP32 (MicroPython) -> Display LCD 20x4 (I2C) + Broker MQTT (HiveMQ) -> Dashboard Node-RED

1. **Obtenção de Dados**: O ESP32 conecta-se à internet e realiza requisições HTTP GET para a API do OpenWeather.
2. **Processamento**: O microcontrolador processa a resposta em formato JSON, extraindo temperatura, umidade e condição do tempo.
3. **Exibição Local**: As informações selecionadas são formatadas e exibidas em tempo real no display LCD 20x4.
4. **Transmissão Remota**: O ESP32 formata a telemetria em formato JSON e envia via MQTT para o broker HiveMQ.
5. **Visualização**: O Node-RED assina o tópico MQTT e exibe os dados em um painel interativo.

---

## Estrutura do Repositório

```
.
├── main.py            # Código principal da aplicação integrada
├── lcd_api.py         # Biblioteca base para comunicação com displays LCD
├── i2c_lcd.py         # Driver I2C para acionamento do LCD 20x4
├── diagram.json       # Configuração das conexões do circuito no Wokwi
└── README.md          # Documentação do projeto
```

---

## Pré-requisitos e Dependências

### Hardware / Simulador
* Placa ESP32 (NodeMCU ESP32-WROOM-32)
* Display LCD 20x4 com módulo I2C (PCF8574)
* Conexão Wi-Fi (no ambiente Wokwi, utilize a rede `Wokwi-GUEST`)

### Software e Serviços
* Ambiente MicroPython instalado no ESP32 ou simulador **Wokwi**
* Chave de acesso (API Key) do serviço **OpenWeather**
* Broker MQTT Público: `broker.hivemq.com` (porta `1883`)
* **Node-RED** para recepção e exibição das mensagens MQTT

---

## Esquema de Ligação (Pinagem I2C)

A conexão entre o ESP32 e o módulo I2C do display LCD 20x4 segue a pinagem padrão:

| Componente | Pino LCD / Módulo I2C | Pino ESP32 | Descrição |
| :--- | :--- | :--- | :--- |
| Alimentação | VCC | 5V / VIN | Tensão de alimentação (5V) |
| Terra | GND | GND | Referência de terra |
| Dados | SDA | GPIO 21 | Linha de Dados I2C |
| Clock | SCL | GPIO 22 | Linha de Clock I2C |

---

## Etapas do Projeto

### 1. Display LCD 20x4 I2C
Utilização das bibliotecas `lcd_api.py` e `i2c_lcd.py` para comunicação com o display LCD 20x4 via barramento I2C (endereço padrão `0x27` ou `0x3F`). Permite inicialização, posicionamento de cursor e escrita de linhas de texto.

### 2. Consulta à API OpenWeather
Conexão à rede sem fio e realização de requisição HTTP utilizando a biblioteca `urequests`. O JSON de resposta é parsed no MicroPython para extrair os seguintes parâmetros:
* **Temperatura**: Valor em graus Celsius.
* **Umidade**: Percentual de umidade relativa do ar.
* **Condição do Tempo**: Descrição do estado meteorológico (ex: ensolarado, nublado, chuva).

### 3. Comunicação MQTT e Node-RED
Conexão ao broker público HiveMQ via protocolo MQTT (biblioteca `umqtt.simple`). Publicação periódica da mensagem em um tópico customizado do grupo em formato JSON.

#### Estrutura do Payload JSON
```json
{
  "temperatura": 25.4,
  "umidade": 68,
  "condicao": "Nublado",
  "dispositivo": "ESP32_Grupo_01"
}
```

---

## Como Executar

### 1. Configuração no Wokwi ou Hardware Real
1. Importe os arquivos `lcd_api.py`, `i2c_lcd.py` e `main.py` para o seu projeto no Wokwi ou no ESP32.
2. Certifique-se de que o circuito está devidamente montado com as conexões I2C (SDA -> GPIO 21, SCL -> GPIO 22).

### 2. Configuração de Credenciais
No arquivo `main.py`, insira suas credenciais da API OpenWeather e configure o tópico MQTT do seu grupo:

```python
# Configurações Wi-Fi
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# Configurações OpenWeather API
API_KEY = "SUA_CHAVE_OPENWEATHER_AQUI"
CITY = "Sao Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pt_br"

# Configurações MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "seu_grupo/iot/openweather"
```

### 3. Execução do Código
Execute o arquivo `main.py`. O ESP32 irá:
1. Inicializar o display LCD.
2. Conectar-se ao Wi-Fi.
3. Consultar os dados na API OpenWeather.
4. Exibir as informações atualizadas na tela do LCD 20x4.
5. Publicar o JSON com os dados meteorológicos no broker MQTT.

### 4. Configuração do Node-RED
1. Abra o Node-RED e crie um nó **mqtt in**.
2. Configure o servidor para `broker.hivemq.com:1883` e o tópico para `seu_grupo/iot/openweather`.
3. Conecte o nó MQTT a nós de visualização (**debug** ou **dashboard** em gauge/text) para monitorar as mensagens recebidas.

---

## Licença e Créditos

Trabalho desenvolvido como atividade prática de comunicação IoT com ESP32 e MicroPython.
