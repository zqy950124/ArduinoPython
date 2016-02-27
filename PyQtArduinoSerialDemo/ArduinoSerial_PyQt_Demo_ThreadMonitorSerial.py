# -*- coding: utf-8 -*-

import queue
import threading
import serial

import random
import time

from ArduinoSerial_PyQt_Demo_Global import  *

class ThreadArduino:
    """
    """
    def __init__(self, port, delay):
        
        self.SERIALPORT = port
        self.running = 1
        self.msg = ''
        self.delay = delay
        self.thread1 = threading.Thread(target=self.worker)
        self.thread1.start()

    def worker(self):
        """
        This is where we handle the asynchronous I/O. 
        Put your stuff here.
        """
        # rand = random.Random()
        ser = serial.Serial(SERIALPORT, 9600)
        while self.running:
            time.sleep(self.delay)
            # self.msg = str(random.random()) + '\n'
            # This is where we poll the Serial port. 
            self.msg = ser.readline().decode();
            if (self.msg):
                queue.put(self.msg)
                
            else: pass  

        if self.running == 0:
           ser.close()



