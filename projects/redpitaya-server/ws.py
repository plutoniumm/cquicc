import websockets

# Define the WebSocket server's behavior when a connection is established.
async def websocket_handler(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            # Process the received message (You can define your own logic here)
            print("Received message:", message)
            response = "Server received: " + message
            await websocket.send(response)
        except websockets.exceptions.ConnectionClosed:
            break