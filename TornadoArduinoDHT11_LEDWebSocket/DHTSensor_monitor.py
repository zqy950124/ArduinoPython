# -*- coding: utf-8 -*-

import serial
import time

global ser
global t0
t0 = time.time()


def getvalue(line, itemname, unitstr):
    index = line.find(itemname)
    value = ''
    itemnamelen = len(itemname)
    if index > -1:
        startIndex = index + itemnamelen
        index = line.find(unitstr, startIndex + 1)
        value = line[startIndex: index]
    return float(value)


def openSerial():
    global ser
    port = 'COM3'
    baudrate = 9600
    try:
        print("Trying...", port)
        ser = serial.Serial(port, baudrate)
        print("Connected on ", port)
        time.sleep(1.5)  # Arduino is reset when opening port so wait before communicating
    except:
        print("Failed to connect on ", port)


def getTHD():
    global ser
    humidity = 0
    temperature = 0
    heat_index = 0

    line = ser.readline().decode()
    # print(line)
    humidity = getvalue(line, " Humidity: ", '%')
    temperature = getvalue(line, " Temperature: ", '*C')
    heat_index = getvalue(line, " Heat index: ", '*C')

    print('湿度=', humidity, '温度=', temperature, '体感温度=', heat_index)

    global t0
    t = time.time() - t0

    return t, {"t": temperature, "h": humidity, "a": heat_index}
