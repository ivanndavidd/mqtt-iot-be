import uvicorn
from fastapi import FastAPI
from app.api import router
from app.mqtt_client import run_mqtt

app = FastAPI()
app.include_router(router)

run_mqtt()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)