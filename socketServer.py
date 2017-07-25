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
    print('[*] A new client came in ^_^.')
    print(clients)
    try:
        while True:
            point = await websocket.recv()
            for client in clients:
                await client.send(point)
    except websockets.exceptions.ConnectionClosed:
        clients.remove(websocket)
        print('[*] A client just leave ~owo~')
        print(clients)

start_server = websockets.serve(time, '127.0.0.1', 9999)
print('[*] Server is listening on 127.0.0.1:9999...')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
