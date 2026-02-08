from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

from app.websocket.manager import manager
from app.mqtt.mqtt_service import start, set_loop
from app.services.data_pipeline import consumer
from app.database.db import insert_record
from app.api.routes import router

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup():
    loop = asyncio.get_running_loop()
    set_loop(loop)
    start()
    asyncio.create_task(consumer(manager, insert_record))

@app.websocket("/ws")
async def websocket_endpoint(websocket, WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(60)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
