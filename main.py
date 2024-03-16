from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/main")
async def main_page():
    return FileResponse("./index.html")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You said: {data}")