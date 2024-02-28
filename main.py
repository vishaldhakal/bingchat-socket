import asyncio
import websockets
from sydney import SydneyClient

async def main(websocket, path) -> None:
    async with SydneyClient() as sydney:
        while True:
            prompt = await websocket.recv()

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            async for response in sydney.ask_stream(prompt):
                await websocket.send(response)

if __name__ == "__main__":
    start_server = websockets.serve(main, "localhost", 10000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
