import time
import json
import random
import paho.mqtt.client as mqtt
import os

# Configurações via variáveis de ambiente
broker = os.getenv("MQTT_BROKER", "mosquitto")
port = int(os.getenv("MQTT_PORT", "1883"))
username = os.getenv("MQTT_USER", "iotuser")
password = os.getenv("MQTT_PASS", "iotpass")

time.sleep(60)  # aguarda o broker subir

client = mqtt.Client(client_id="ph_sensor_simulator")
client.username_pw_set(username, password)

print(f"Conectando ao broker {broker}:{port} ...")
client.connect(broker, port, 5)
print("Conectado!")

while True:
    ph_value = round(random.uniform(6.0, 8.0), 2)
    payload = json.dumps({"device": "sensor-01", "ph": ph_value})
    client.publish("sensors/ph", payload)
    print("Enviado:", payload)
    time.sleep(5)
