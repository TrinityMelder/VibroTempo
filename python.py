import asyncio
import websockets
import serial
import nest_asyncio

# Patch the existing event loop
nest_asyncio.apply()

# Setup serial connection
ser = serial.Serial('COM8', 9600)

async def handler(websocket, path):
    async for message in websocket:
        print("Received message from client:", message)
        if message.startswith("start") or message == "stop":
            ser.write(f"{message}\n".encode())
            await websocket.send("Command sent to Arduino")

# Start the server
start_server = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
