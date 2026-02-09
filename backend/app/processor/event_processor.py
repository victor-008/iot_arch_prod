import redis
import json
import asyncio
from app.config import REDIS_HOST
from app.database import SessionLocal
from app.models import Telemetry
from app.websocket_manager import manager

r=redis.Redis(host=REDIS_HOST)

async def run():
    db=SessionLocal()

    last_id="0-0"

    while True:
        streams=r.xread({"telemetry_stream":last_id},block=0)
        for stream,events in streams:
            for eid,data in events:
                last_id=eid
                payload=json.loads(data[b'data'])

                record=Telemetry(
                    device_id=payload["device_id"],
                    temperature=payload["temperature"],
                    humidity=payload["humidity"]
                )
                db.add(record)
                db.commit()

                await manager.broadcast(payload)
