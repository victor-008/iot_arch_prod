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