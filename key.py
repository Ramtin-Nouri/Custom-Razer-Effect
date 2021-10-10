"""Custom key class"""
from threading import Thread, Event
import time
import numpy as np
from getConfig import *

class Key(Thread):
    """
        Key Class. Inherits from Thread.

        Each key is defined by its x and y position in the 
        LED matrix.

        Attributes:
        ----------
        matrix: reference to device.fx.advanced.matrix
        update: reference to function
            reference to the function that updates the hardware
        x: int
        y: int
        _startSignal: Event
            Thread will wail for this event to start the animation

    """
    def __init__(self,x,y,matrix,updateFunc):
        """Set arguments, set the color to static and start thread."""
        Thread.__init__(self)
        self.matrix = matrix
        self.update = updateFunc
        self.x = x
        self.y = y
        self.setStatic()
        self._startSignal = Event()
        self.start()

    def run(self):
        """Thread function executed in a loop.
        
        Waits for start signal.
        Then exectes a linear interpolation of the reactive color to the background color.
        """
        while True:
            self._startSignal.wait()
            self._startSignal.clear()

            self.startTime = time.time()
            while time.time()-self.startTime < REACTIVE_TIME:
                time.sleep(.1)# sleep so we don't execute too often and exhaust resources
                linInterpAmount = float(time.time()-self.startTime) / REACTIVE_TIME
                color2 = np.array(COLOR_REACT)
                color1 = np.array(COLOR_BG)
                smoothColor = (color1 - color2) * linInterpAmount + color2
                self.matrix[self.x,self.y] = list(smoothColor)
                self.update()

            self.matrix[self.x,self.y] = COLOR_BG
            self.update()
        

    def setStatic(self):
        """Set the color of this key's LED to the static/background color"""
        self.matrix[self.x, self.y] = COLOR_BG

    def setReact(self):
        """Set the color of this key's LED to the reactive color"""
        self.matrix[self.x, self.y] = COLOR_REACT

    def setAnimation(self):
        """start/reset the animation"""
        self.startTime = time.time()
        self._startSignal.set()