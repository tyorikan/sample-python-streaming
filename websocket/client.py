#!/usr/bin/env python

import asyncio
import os
import websockets

host = os.environ.get("WS_HOST", "localhost")
port = os.environ.get("WS_PORT", "8080")


async def hello():
    uri = "ws://" + host + ":" + port
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print(await websocket.recv())

asyncio.run(hello())
