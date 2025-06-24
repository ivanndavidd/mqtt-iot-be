
# MQTT IoT Backend (FastAPI + WebSocket)

A lightweight backend service for real-time MQTT data streaming using FastAPI and WebSocket — **without using a database**. Ideal for IoT sensor dashboards, like piezoelectric or energy monitoring.

---

## 🚀 Features

- 📡 Connects to MQTT broker (e.g., Mosquitto)
- 🔄 Subscribes to specific sensor topics
- ⚡ Streams real-time data to frontend via WebSocket
- 🧾 No database, pure in-memory data flow

---

## 📡 Architecture
| ESP32  | > | Mosquitto | > | FastAPI BE  | > | Frontend  |
---

## 🛠️ Setup

### 1. 📦 Library Installation

Install the required Python packages:

```bash
pip install fastapi uvicorn paho-mqtt
```

### 2. 🧠 Project Structure

```
mqtt-membumi-be/
├── app/
│   ├── config.py      # MQTT broker settings
│   ├── mqtt_client.py # MQTT listener logic
│   └── storage.py     # In-memory data store & WebSocket broadcasting
├── main.py            # FastAPI app entry point
```

### 3. ⚙️ `config.py` Configuration

Create a file at `app/config.py`:

```python
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPICS = ("sensor/piezo", 0)
```

---

## 🧪 Run Backend Server

Use the following command to start the server:

```bash
uvicorn main:app --reload
```

This runs FastAPI on [http://localhost:8000](http://localhost:8000) and initializes the MQTT listener.

> ✅ Make sure `main.py` contains `app = FastAPI()` and follows ASGI pattern.

---

## 🌐 WebSocket Endpoint

- URL: `ws://localhost:8000/ws`
- Accepts multiple clients.
- Pushes live payload from MQTT.

---

## 💡 How to Simulate MQTT Sensor

Use `mosquitto_pub` to send test data to the topic:

```bash
mosquitto_pub -h localhost -t sensor/piezo -m "123.45"
```

The backend will receive this via MQTT and push it to all connected WebSocket clients.

---

## 🧰 Install Mosquitto MQTT Broker

### 🖥️ On Windows (via Chocolatey):

```bash
choco install mosquitto
```

> Or download from: https://mosquitto.org/download/

### 🐧 On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

Test the broker:

```bash
mosquitto_sub -h localhost -t sensor/piezo
```

---

## 📬 Example Frontend WebSocket Client (JavaScript)

```js
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = (event) => {
  console.log("Received from backend:", event.data);
};
```

---

## 🧼 Notes

- This backend **does not store data permanently**.
- Suitable for real-time dashboards or volatile sensor streams.

---

## 📜 License

MIT License — Feel free to use and modify.
