"""
Prevents crashes when dashboard disconnetcs, mqtt floods data or slow frontend

"""

import asyncio

queue = asyncio.Queue()

async def producer(record):
    await queue.put(record)

async def consumer (manager, db_insert):
    while True:
        record = await queue.get()
        await manager.broadcast(record)
        db_insert(record)