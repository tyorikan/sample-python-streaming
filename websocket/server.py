#!/usr/bin/env python

import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        print("received message from client : " + message)
        message = "sent message from server : " + message
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8080):
        await asyncio.Future()

asyncio.run(main())
