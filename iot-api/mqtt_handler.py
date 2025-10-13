import threading
import json
import paho.mqtt.client as mqtt
from sqlalchemy.orm import Session
from db import SessionLocal
from models import SensorData
import os

broker = os.getenv("MQTT_BROKER", "mosquitto")
port = int(os.getenv("MQTT_PORT", "1883"))
username = os.getenv("MQTT_USER", "iotuser")
password = os.getenv("MQTT_PASS", "iotpass")
topic = "sensors/ph"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao broker MQTT com código {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    print("Recebido MQTT:", payload)
    db: Session = SessionLocal()
    try:
        data = SensorData(device=payload["device"], ph=payload["ph"])
        db.add(data)
        db.commit()
    except Exception as e:
        print("Erro ao salvar no banco:", e)
    finally:
        db.close()

def start_mqtt():
    def run():
        client = mqtt.Client(client_id="fastapi_listener")
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker, port, 60)
        client.loop_forever()

    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
