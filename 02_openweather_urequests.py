import network
import urequests
import time

SSID = "Wokwi-GUEST"
PASSWORD = ""

API_KEY = "SUA_API_KEY"
CIDADE = "Sao%20Paulo"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Conectando ao Wi-Fi...")

while not wifi.isconnected():
    time.sleep(0.5)

print("Wi-Fi conectado!")

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    "?q=" + CIDADE +
    "&appid=" + API_KEY +
    "&units=metric"
)

print("URL:")
print(url)

response = urequests.get(url)

print("Status:", response.status_code)
print("Resposta:")
print(response.text)

if response.status_code == 200:
    dados = response.json()

    print()
    print("Cidade:", dados["name"])
    print("Temperatura:", dados["main"]["temp"], "C")
    print("Umidade:", dados["main"]["humidity"], "%")
    print("Condicao:", dados["weather"][0]["description"])

response.close()
