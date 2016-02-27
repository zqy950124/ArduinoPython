# -*- coding: utf-8 -*-
"""
"""

import sys
from PyQt4 import QtGui, QtCore as qt

from ArduinoSerial_PyQt_Demo_Global import  *
from ArduinoSerial_PyQt_Demo_ThreadMonitorSerial import  *
from ArduinoSerial_PyQt_Demo_QTimerClient import  *

root = QtGui.QApplication(sys.argv)
monitor = ThreadArduino(SERIALPORT, monitorinterval)
uiclient = ThreadedUIClient(uiperiodicinterval)
sys.exit(root.exec_())

