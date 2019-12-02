import websockets
import asyncio
import pyaudio
import numpy as np
import random


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        sendtext = 'setLED {} '.format(25*60)
        for x in range(25):
            for y in range(60):
                sendtext = sendtext + '{} {} {} {} {} '.format(y, x, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        '''sendtext = sendtext + '1 1 255 255 0 '
        sendtext = sendtext + '1 2 255 255 0 '
        sendtext = sendtext + '1 3 255 255 0 '
        sendtext = sendtext + '1 4 255 255 0 '
        sendtext = sendtext + '2 2 255 255 0 '
        sendtext = sendtext + '3 3 255 255 0 '
        sendtext = sendtext + '4 1 255 255 0 '
        sendtext = sendtext + '4 2 255 255 0 '
        sendtext = sendtext + '4 3 255 255 0 '
        sendtext = sendtext + '4 4 255 255 0 '
        sendtext = sendtext + '6 1 255 255 0 '
        sendtext = sendtext + '6 2 255 255 0 '
        sendtext = sendtext + '6 3 255 255 0 '
        sendtext = sendtext + '7 4 255 255 0 '
        sendtext = sendtext + '8 4 255 255 0 '
        sendtext = sendtext + '9 1 255 255 0 '
        sendtext = sendtext + '9 2 255 255 0 '
        sendtext = sendtext + '9 3 255 255 0 '
        sendtext = sendtext + '11 1 255 255 0 '
        sendtext = sendtext + '12 1 255 255 0 '
        sendtext = sendtext + '13 1 255 255 0 '
        sendtext = sendtext + '14 1 255 255 0 '
        sendtext = sendtext + '15 1 255 255 0 '
        sendtext = sendtext + '13 2 255 255 0 '
        sendtext = sendtext + '13 3 255 255 0 '
        sendtext = sendtext + '13 4 255 255 0 '
        sendtext = sendtext + '17 1 255 255 0 '
        sendtext = sendtext + '18 1 255 255 0 '
        sendtext = sendtext + '19 1 255 255 0 '
        sendtext = sendtext + '20 1 255 255 0 '
        sendtext = sendtext + '21 1 255 255 0 '
        sendtext = sendtext + '19 2 255 255 0 '
        sendtext = sendtext + '19 3 255 255 0 '
        sendtext = sendtext + '19 4 255 255 0 '
        sendtext = sendtext + '23 1 255 255 0 '
        sendtext = sendtext + '23 2 255 255 0 '
        sendtext = sendtext + '23 3 255 255 0 '
        sendtext = sendtext + '23 4 255 255 0 '
        sendtext = sendtext + '23 5 255 255 0 '
        sendtext = sendtext + '24 1 255 255 0 '
        sendtext = sendtext + '25 1 255 255 0 '
        sendtext = sendtext + '24 3 255 255 0 '
        sendtext = sendtext + '24 5 255 255 0 '
        sendtext = sendtext + '25 5 255 255 0 '''

        await websocket.send(sendtext)
        print(sendtext)


if __name__ == '__main__':
    CHUNK = 2 ** 11
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)
    for i in range(int(10 * RATE / 1024)):
        data = np.fromstring(stream.read(CHUNK, exception_on_overflow=False
                                         ), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        bars = "#"*int(50*peak/2**16)
        print("%04d %05d %s" % (i, peak, bars))

    stream.stop_stream()
    stream.close()
    p.terminate()

    '''for x in range(200):
        asyncio.get_event_loop().run_until_complete(hello())'''

    """speed = 2
    loops = int(255/speed)
    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(0, 0, z*speed))

    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(0, z*speed, loops))

    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(z*2, speed, speed))

    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(250, 250, 250-z*2))

    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(250, 250-z*2, 0))

    for z in range(loops):
        asyncio.get_event_loop().run_until_complete(hello(250-z*2, 0, 0))"""
