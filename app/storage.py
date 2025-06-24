from datetime import datetime

data_log = []
websocket_clients = set()

def save_data(topic, payload):
    data_log.append({
        "timestamp": datetime.utcnow().isoformat(),
        "topic": topic,
        "value": payload
    })
    if len(data_log) > 100:
        data_log.pop(0)

async def broadcast_to_clients(payload):
    for ws in list(websocket_clients):
        try:
            await ws.send_text(payload)
        except:
            websocket_clients.remove(ws)