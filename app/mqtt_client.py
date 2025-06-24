import paho.mqtt.client as mqtt
from app.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPICS
from app.storage import save_data, broadcast_to_clients
import asyncio

_main_loop = None

def on_connect(client, userdata, flags, rc):
    print(" Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPICS)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"MQTT RECEIVED: {msg.topic} -> {payload}")
    save_data(msg.topic, payload)

    if _main_loop:
        asyncio.run_coroutine_threadsafe(broadcast_to_clients(payload), _main_loop)

def run_mqtt(loop):
    global _main_loop
    _main_loop = loop

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()