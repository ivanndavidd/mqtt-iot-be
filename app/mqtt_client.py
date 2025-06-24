import paho.mqtt.client as mqtt
from app.config import MQTT_BROKER, MQTT_PORT, MQTT_TOPICS
from app.storage import save_data, broadcast_to_clients
import asyncio
import json

energy_levels = {}
_main_loop = None



def on_connect(client, userdata, flags, rc):
    print(" Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPICS)

def on_message(client, userdata, msg):
    global cluster_id, energy, total_energy
    payload = msg.payload.decode()
    try:
        topic_parts = msg.topic.split("/")
        cluster_id = topic_parts[1]
        energy = float(payload)
        energy_levels[cluster_id] = energy
        total_energy = sum(energy_levels.values())

        # Print per cluster and total
        # print(f"[Cluster {cluster_id}] Energy: {energy:.2f} | Total Energy: {total_energy:.2f}")
        save_data(msg.topic, payload)
        if _main_loop:
            data = {
                "cluster_id": cluster_id,
                "energy": energy,
                "total_energy": total_energy
            }
            json_payload = json.dumps(data)
            # print("Broadcasting to clients:", json_payload)
            asyncio.run_coroutine_threadsafe(broadcast_to_clients(json_payload), _main_loop)
    except Exception as e:
        print("Invalid message:", payload, "from topic:", MQTT_TOPICS, "| Error:", e)

def run_mqtt(loop):
    global _main_loop
    _main_loop = loop

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()