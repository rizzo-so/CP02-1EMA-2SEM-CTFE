import network
import time
import json
import random

from umqtt.simple import MQTTClient

SSID = "Wokwi-GUEST"
PASSWORD = ""

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_fiap_01"
MQTT_TOPIC = "fiap/iot/grupo01/temperatura"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Conectando ao Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

print("Wi-Fi conectado!")

client = MQTTClient(
    MQTT_CLIENT_ID,
    MQTT_BROKER,
    port=MQTT_PORT
)

print("Conectando ao broker MQTT...")

client.connect()

print("MQTT conectado!")
print("Topico:", MQTT_TOPIC)

while True:
    temperatura = round(random.uniform(20, 30), 1)

    dados = {
        "temperatura": temperatura
    }

    mensagem = json.dumps(dados)

    client.publish(MQTT_TOPIC, mensagem)

    print("Publicado:", mensagem)

    time.sleep(5)
