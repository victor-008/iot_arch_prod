# """
# Loads  configuratiion values like API keys, database URLs 
# from a .env file into the python environment
# """

# from dotenv import load_dotenv
# import os

# load_dotenv()

# MQTT_BROKER = os.getenv("MQTT_BROKER", "127.0.0.1")
# MQTT_TOPIC = "sensors"


import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER")
REDIS_HOST = os.getenv("REDIS_HOST")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
JWT_SECRET = os.getenv("JWT_SECRET")
