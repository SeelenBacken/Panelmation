import websockets
import asyncio

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    if name == "Banane":
        print("- Erfolg!")

    await websocket.send(greeting)
    print(f"> {greeting}")

def run():
    start_server = websockets.serve(hello, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
