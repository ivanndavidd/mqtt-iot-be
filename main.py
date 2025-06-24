from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.mqtt_client import run_mqtt
from app.storage import websocket_clients
import asyncio

app = FastAPI()

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.add(websocket)
    print(f"Client connected. Total: {len(websocket_clients)}")

    try:
        while True:
            await websocket.receive_text()  # keep connection alive
    except WebSocketDisconnect:
        websocket_clients.remove(websocket)
        print(f"Client disconnected. Total: {len(websocket_clients)}")

# MQTT start during FastAPI startup
@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_running_loop()
    run_mqtt(loop)
