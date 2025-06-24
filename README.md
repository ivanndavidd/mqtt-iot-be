# MQTT IoT Backend (FastAPI + WebSocket)

A lightweight backend service for real-time MQTT data streaming using FastAPI and WebSocket.

## 🚀 Features

- Connects to an MQTT broker (e.g., Mosquitto)
- Subscribes to topics and listens for sensor data
- Pushes data in real-time to frontend via WebSocket
- No database — pure live streaming

## 📡 Architecture

graph TD
  ESP32 -->|publish| Mosquitto
  Mosquitto -->|subscribe| FastAPI Backend
  FastAPI -->|WebSocket PUSH| Frontend

## Library Installation

Install all lib below using pip 
- fastapi
- uvicorn
- paho-mqtt

## config.py
make a file of /app/config.py, with below required
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPICS = "sensor/piezo"
