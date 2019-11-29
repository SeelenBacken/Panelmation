from MationSim.__main__ import MationSim
import asyncio

class animation:
    def start(self):
        self.sim.start()
    
    def __init__(self):
        self.sim = MationSim()
