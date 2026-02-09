# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# import asyncio

# from app.websocket.manager import manager

# from backend.app.mqtt.mqtt_worker import start, set_loop

# from app.services.data_pipeline import consumer
# from app.database.db import insert_record
# from app.api.routes import router

# app = FastAPI()
# app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     loop = asyncio.get_running_loop()
#     set_loop(loop)
#     start()
#     asyncio.create_task(consumer(manager, insert_record))

# @app.websocket("/ws")
# async def websocket_endpoint(websocket, WebSocket):
#     await manager.connect(websocket)
#     try:
#         while True:
#             await asyncio.sleep(60)
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)


"""api gateway
"""

from fastapi import FastAPI,WebSocket,WebSocketDisconnect
import asyncio

from .mqtt.mqtt_worker import start as mqtt_start
from .processor.event_processor import run as processor_run
from .websocket_manager import manager
from .database import Base,engine

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    mqtt_start()
    asyncio.create_task(processor_run())

@app.websocket("/ws")
async def ws(ws:WebSocket):
    await manager.connect(ws)
    try:
        while True:
            await asyncio.sleep(60)
    except WebSocketDisconnect:
        manager.disconnect(ws)




#how to run >> "docker-compose up --build
"
