import asyncio
import websockets

SERVER_PORT = 9999
SERVER_ADDRESS = 'localhost'


async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))
    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, SERVER_ADDRESS, SERVER_PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
