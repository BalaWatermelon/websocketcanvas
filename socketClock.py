#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets
import json

buffer = []
clients = []


async def time(websocket, path):
    global clients
    global buffer
    clients.append(websocket)
    try:
        while True:
            point = await websocket.recv()
            for client in clients:
                await client.send(point)
    except websockets.exceptions.ConnectionClosed:
        print('a client just leave ~owo~')
        print(clients)

start_server = websockets.serve(time, '127.0.0.1', 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
