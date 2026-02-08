from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active.append(websocket)

    def disconnect (self, websocket: WebSocket):
        if websocket in self.active:
            self.active.remove(websocket)
    
    async def broadcast(self,data):
        dead = []
        for ws in self.active:
            try:
                await ws.send_json(data)
            except:
                dead.append(ws)
        for ws in dead:
            self.disconnect(ws)

manager = ConnectionManager()