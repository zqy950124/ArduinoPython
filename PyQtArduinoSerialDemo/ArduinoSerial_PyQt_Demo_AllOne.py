# -*- coding: utf-8 -*-
"""
This recipe opens a simple window in PyQt to poll the serial port for
data and print it out. Uses threads and a queue.

This recipe depends on Python3.5,PyQt4 and pySerial.
Tested on Qt4.7 / Win 10 / Arduino Uno

PS: This code is meant to demonstrate a concept only, not for actual use.

"""

import sys
import time
import threading
import random
import queue
from PyQt4 import QtGui, QtCore as qt
import serial

SERIALPORT = 'COM3'


class GuiPart(QtGui.QMainWindow):

    def __init__(self, queue, endcommand, *args):
        QtGui.QMainWindow.__init__(self, *args)
        self.setWindowTitle('Arduino Serial Demo')
        self.queue = queue
        # We show the result of the thread in the gui, instead of the console
        self.editor = QtGui.QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.endcommand = endcommand

    def closeEvent(self, ev):
        self.endcommand()

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply print it
                self.editor.insertPlainText(str(msg))
            except Queue.Empty:
                pass


class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """

    def __init__(self):
        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(self.queue, self.endApplication)
        self.gui.show()

        # A timer to periodically call periodicCall :-)
        self.timer = qt.QTimer()
        qt.QObject.connect(self.timer,
                           qt.SIGNAL("timeout()"),
                           self.periodicCall)
        # Start the timer -- this replaces the initial call to periodicCall
        self.timer.start(100)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            root.quit()

    def endApplication(self):
        self.running = 0

    def workerThread1(self):
        """
        This is where we handle the asynchronous I/O.
        Put your stuff here.
        """
        # rand = random.Random()
        ser = serial.Serial(SERIALPORT, 9600)
        while self.running:
            # This is where we poll the Serial port.
            # time.sleep(random.random() * 0.3)
            # msg = random.random()
            # self.queue.put(msg)

            msg = ser.readline().decode()
            if (msg):
                self.queue.put(msg)
            else:
                pass

        if self.running == 0:
            ser.close()

root = QtGui.QApplication(sys.argv)
client = ThreadedClient()
sys.exit(root.exec_())
