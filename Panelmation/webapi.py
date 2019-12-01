import websockets
import asyncio

async def hello(r, g, b):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        sendtext = 'setLED {} '.format(25*60)
        for x in range(25):
            for y in range(60):
                sendtext = sendtext + '{} {} {} {} {} '.format(y, x, r, g, b)

        await websocket.send(sendtext)
        print(sendtext)

speed = 2
loops = int(255/speed)
for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(0, 0, z*speed))

for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(0, z*speed, loops))

for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(z*2, speed, speed))

for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(250, 250, 250-z*2))

for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(250, 250-z*2, 0))

for z in range(speed):
    asyncio.get_event_loop().run_until_complete(hello(250-z*2, 0, 0))
