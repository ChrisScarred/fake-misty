import uvicorn
from fastapi import FastAPI, WebSocket

# APP
app = FastAPI(
    title="Fake API",
    debug=True,
)

@app.get("/")
@app.post("/")
async def a():
    return {
        "status": "Success"
    }

@app.get("/{a}")
@app.post("/{a}")
async def b(a: str):
    return {
        "status": "Success",
        "message": f"/{a}"
    }

@app.get("/{a}/{b}")
@app.post("/{a}/{b}")
async def c(a: str, b: str):
    if a=="api":
        if b=="audio":
            return {
                "status": "Success",
                "content": b"RIFF$\x07\x06\x00WA",
                "result": {
                    "base64": b"RIFF$\x07\x06\x00WA"
                }
            }
    return {
        "status": "Success",
        "message": f"/{a}/{b}"
    }

@app.delete("/{a}/{b}")
async def x(a: str, b: str):
    return {
        "status": "Success"
    }

@app.get("/{a}/{b}/{c}")
@app.post("/{a}/{b}/{c}")
async def d(a: str, b: str, c: str):
    if a=="api":
        if b=="tts":
            if c=="speak":
                return {
                    "status": "Success"
                }
        if b=="audio":
            if c=="list":
                return {
                    "status": "Success",
                    "result": [
                        {
                            "name": "yada.wav",
                            "systemAsset": False
                        }
                    ]
                }
    return {
        "status": "Success",
        "message": f"/{a}/{b}/{c}"
    }

@app.get("/{a}/{b}/{c}/{d}")
@app.post("/{a}/{b}/{c}/{d}")
async def c(a: str, b: str, c: str, d: str):
    return {
        "status": "Success",
        "message": f"/{a}/{b}/{c}/{d}"
    }

@app.websocket("/pubsub")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except Exception as e:
        print(e, flush=True)

# RUN PROGRAMATICALLY

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host="127.0.0.1",
        port=5002,
        log_level="info"
    )
