from threading import Thread, Event
import time
import numpy as np
from .getConfig import *

class Key(Thread):
    def __init__(self,x,y,matrix,updateFunc):
        Thread.__init__(self)
        self.matrix = matrix
        self.update = updateFunc
        self.x = x
        self.y = y
        self.setStatic()
        self._startSignal = Event()
        self.start()

    def run(self):
        while True:
            self._startSignal.wait()
            self._startSignal.clear()

            self.startTime = time.time()
            while time.time()-self.startTime < REACTIVE_TIME:
                time.sleep(.1)
                linInterpAmount = float(time.time()-self.startTime) / REACTIVE_TIME
                color2 = np.array(COLOR_REACT)
                color1 = np.array(COLOR_BG)
                smoothColor = (color1 - color2) * linInterpAmount + color2
                self.matrix[self.x,self.y] = list(smoothColor)
                self.update()

            self.matrix[self.x,self.y] = COLOR_BG
            self.update()
        

    def setStatic(self):
        self.matrix[self.x, self.y] = COLOR_BG

    def setReact(self):
        self.matrix[self.x, self.y] = COLOR_REACT

    def setAnimation(self):
        self.startTime = time.time()
        self._startSignal.set()