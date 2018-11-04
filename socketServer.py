#!/usr/bin/env python

import asyncio
import datetime
import random
import websockets
import json

buffer = []
clients = []
names = {}

async def time(websocket, path):
    global clients
    global buffer
    clients.append(websocket)
    print('[*] A new client came in ^_^.')
    print('Clients: {}'.format(len(clients)))
    try:
        while True:
            msg = await websocket.recv()
            m = json.loads(msg)
            if m['msg'] =='draw':
                for client in clients:
                    await client.send(msg)
            elif m['msg'] == 'newstudent':
                if str(m['roomID']) in names:
                    if m['name'] not in names[str(m['roomID'])]:
                        names[str(m['roomID'])].append(m['name'])
                else:
                    names[str(m['roomID'])] = []
                    names[str(m['roomID'])].append(m['name'])
                r = {'msg':'stulist','data':names}
                r = json.dumps(r)
                for client in clients:
                    await client.send(r)
    except websockets.exceptions.ConnectionClosed:
        clients.remove(websocket)
        print('[*] A client just leave ~owo~')
        print('Clients: {}'.format(len(clients)))


start_server = websockets.serve(time, '10.203.65.168', 9999)
print('[*] Server is listening on 127.0.0.1:9999...')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
