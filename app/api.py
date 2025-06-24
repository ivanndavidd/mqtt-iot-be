# app/api.py
from fastapi import APIRouter, WebSocket
from app.storage import websocket_clients

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()  # Untuk jaga koneksi tetap hidup
    except:
        websocket_clients.remove(websocket)