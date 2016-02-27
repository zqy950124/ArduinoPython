# -*- coding: utf-8 -*-
"""
This recipe opens a simple window in PyQt to poll the serial port for 
"""

import sys, time, threading, random, queue
from PyQt4 import QtGui, QtCore as qt

from ArduinoSerial_PyQt_Demo_Global import  *
from ArduinoSerial_PyQt_Demo_GuiPart import *

class ThreadedUIClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, uiperiodicinterval):
        
        self.uiperiodicinterval = uiperiodicinterval
        # Set up the GUI part
        self.gui = GuiPart(self.endApplication)
        self.gui.show()

        # A timer to periodically call periodicCall :-)
        self.timer = qt.QTimer()
        
        qt.QObject.connect(self.timer,
                           qt.SIGNAL("timeout()"),
                           self.periodicCall)
       
        # Start the timer -- this replaces the initial call to periodicCall
        # Check every uiperiodicinterval  ms if there is something new in the queue.
        self.timer.start(self.uiperiodicinterval)
        self.running = 1

    def periodicCall(self):
        self.gui.processIncoming()
        if not self.running:
            root.quit()

    def endApplication(self):
        self.running = 0


