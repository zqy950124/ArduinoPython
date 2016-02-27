# -*- coding: utf-8 -*-

import queue
from PyQt4 import QtGui, QtCore as qt

from ArduinoSerial_PyQt_Demo_Global import  *

class GuiPart(QtGui.QMainWindow):

    def __init__(self, endcommand, *args):
        QtGui.QMainWindow.__init__(self, *args)
        self.setWindowTitle('Arduino Serial Demo')
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
        while queue.qsize():
            try:
                msg = queue.get(0)
                # Check contents of message and do what it says
                # As a test, we simply print it
                self.editor.insertPlainText(str(msg))
            except queue.Empty:
                pass

