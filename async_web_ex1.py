import websockets
import asyncio


async def astronout():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        is_ready = input("Are you ready?")

        await websocket.send(is_ready)
        async for message in websocket:
            print(message)
            if "BLASTOFF" in message:
                return

async def main():
     await asyncio.gather(astronout(), astronout(),astronout(),astronout())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
