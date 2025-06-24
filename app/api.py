# app/api.py
from fastapi import APIRouter, WebSocket
from app.storage import websocket_clients

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.add(websocket)
    print(f"Client connected. Total: {len(websocket_clients)}")
    try:
        while True:
            await websocket.receive_text()  # keep-alive
    except:
        print("Client disconnected.")
        websocket_clients.remove(websocket)