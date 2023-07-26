# socket based communication
import asyncio
import websockets

async def handler(websocket, path):
    data = await websocket.recv()
    reply = "Data received: {}".format(data)
    await websocket.send(reply)

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()