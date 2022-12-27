from time import sleep
from breakout_bme280 import BreakoutBME280
from pimoroni_i2c import PimoroniI2C
from umqttsimple import MQTTClient
import network
import secrets

PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
bme = BreakoutBME280(i2c)

CLIENT_NAME = b'pico'

BROKER_ADDR = b'<address>'
USER = secrets.MQTT_USER.encode()
PASSWORD = secrets.MQTT_PASSWORD.encode()
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, user=USER, password=PASSWORD, keepalive=60)
TEMP_TOPIC = b'temp'
HUMIDITY_TOPIC = b'humidity'


def connect_to_wifi():
    print('connecting')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    while not wlan.isconnected():
        sleep(1.0)
    print('connected')


def measure():
    temperature, pressure, humidity = bme.read()
    mqttc.publish(TEMP_TOPIC, str(temperature).encode())
    mqttc.publish(HUMIDITY_TOPIC, str(humidity).encode())
    print(f'Temp: {temperature} | Humidity: {humidity}')


connect_to_wifi()
mqttc.connect()

while True:
    measure()
    sleep(10.0)
