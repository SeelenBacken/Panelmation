from MationSim.__main__ import MationSim
from time import sleep
from threading import Thread
from animation_1 import animation as anim
import api
"""
sim = MationSim()

sleep(4)
sim.setPixel(3,5,(0,0,255))
sim.setPixel(2,5,(0,255,0))

#def Motion():
 #   sim.start()

def Color():
    count = 0
    if count == 0:
        sim.setPixel(10,10,(255,255,255))
        count = count-1
    elif count == 1:
        sim.setPixel(10,10,(100,0,0))
        count += 1
        
#motionThread = Thread(target=Motion)
#colorThread = Thread(target=Color)

#colorThread.start
#motionThread.start
        
sim.start()"""

a = anim()
api.init()
a.start()