# -*- coding: utf-8 -*-
"""

http://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips


binding-a-pyqt-pyside-widget-to-a-local-variable-in-python

http://stackoverflow.com/questions/21992849/binding-a-pyqt-pyside-widget-to-a-local-variable-in-python#

"""

import functools 

def event(func):
    """Makes a method notify registered observers"""
    def modified(obj, *arg, **kw):
        func(obj, *arg, **kw)
        
        obj._Observed__fireCallbacks(func.__name__, *arg, **kw)
        
        functools.update_wrapper(modified, func)
    return modified


class Observed(object):
    """Subclass me to respond to event decorated methods"""

    def __init__(self):
        self.__observers = {}  # Method name -> observers

    def addObserver(self, methodName, observer):
        s = self.__observers.setdefault(methodName, set())
        s.add(observer)

    def __fireCallbacks(self, methodName, *arg, **kw):
        if methodName in self.__observers:
            for o in self.__observers[methodName]:
                o(*arg, **kw)
                
                
class receivedmsg(Observed):
   
    def __init__(self):
        Observed.__init__(self)
    
    @event
    def receivedmsgok(self, data):
        print("Something happened with %s" % (data,))

def myCallback(data):
    print("callback fired with %s" % (data,))

f = receivedmsg()
f.addObserver('receivedmsgok', myCallback)

f.receivedmsgok('Hello, World')               
