import pyautogui
import socket
import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_adress_name = (s.getsockname()[0])
s.close()


app = FastAPI()


@app.get("/")
async def indexPage():
    return FileResponse("./templates/index.html")


@app.get("/sendCommand")
async def sendCommand(command: str):
    if (command == "previous"):
        pyautogui.press("left")
    if (command == "next"):
        pyautogui.press("right")
    return {"message": "Hello"}



if __name__ == "__main__":
    print("SERVER IS RUNNING AT ", ip_adress_name)
    uvicorn.run(app=app, host="0.0.0.0")