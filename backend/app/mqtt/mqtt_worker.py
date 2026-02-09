# import json
# import asyncio
# import paho.mqtt.client as mqtt
# from datetime import datetime

# from app.config import MQTT_BROKER, MQTT_TOPIC
# from app.services.data_pipeline import producer

# loop = None

# def set_loop(event_loop)
#     global loop
#     loop = event_loop

# def on_message(client,userdata,msg):
#     global loop
    
#     data = json.loads(msg.payload.decode())
#     record = {
#         "timestamp" : datetime.now().isoformat(),
#         "temperature" : data["temperature"],
#         "humidity" : data["humidity"]
#     }
#     print ("MQTT:", record)

#     if loop:
#         asyncio.run_coroutine_threadsafe(
#             producer(record),
#             loop
#         )

# def start():
#     client = mqtt.Client()
#     client.on_message = on_message
#     client.connect(MQTT_BROKER,1883)
#     client.subscribe(MQTT_TOPIC)
#     client.loop_start()


"""
Streaming into redis
"""

import json
import paho.mqtt.client as mqtt
import redis
from app.config import MQTT_BROKER,REDIS_HOST

r=redis.Redis(host=REDIS_HOST)

def on_message(client,userdata,msg):
    r.xadd("telemetry_stream",{
        "data":msg.payload.decode()
    })

def start():
    c=mqtt.Client()
    c.on_message=on_message
    c.connect(MQTT_BROKER,1883)
    c.subscribe("devices/+/telemetry")
    c.loop_start()
