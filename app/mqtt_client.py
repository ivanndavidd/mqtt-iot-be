import paho.mqtt.client as mqtt
from app.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from app.storage import save_data, broadcast_to_clients

def on_connect(client, userdata, flags, rc):
    print(" Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"MQTT RECEIVED: {msg.topic} -> {payload}")
    save_data(msg.topic, payload)

    import asyncio
    asyncio.create_task(broadcast_to_clients(payload))


def run_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
