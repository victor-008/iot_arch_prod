# """
# REST API for historical data endpoint

# """
# from fastapi import APIRouter
# from app.database.db import cursor

# router = APIRouter()

# @router.get("/history")
# def history():
#     cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 100")
#     rows = cursor.fetchall()

#     return[
#         {
#         "timestamp" : r[1],
#         "temperature" : r[2],
#         "humidity" : r[3]
#         } for r in rows      
#     ]