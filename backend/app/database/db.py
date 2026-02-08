import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               temperature REAL,
               humidity REAL,
               timestamp TEXT
               )
               """)
conn.commit()

def insert_record(data):
    cursor.execute(
        "INSERT INTO sensor_data (timestamp,temperature,humidity,) VALUES(?,?,?)",
        (data["timestamp"],data["temperature"],data["humidity"])
    )
    conn.commit()