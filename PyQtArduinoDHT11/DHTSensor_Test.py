# -*- coding: utf-8 -*-

import serial

ser = serial.Serial('COM3', 9600)

humidity = 0
temperature = 0 
heat_index = 0

getvalue = True
newitem = False

def getvalue(line, itemname, unitstr):
    index = line.find (itemname)
    value = ''
    itemnamelen = len(itemname)
    if index > -1:
        startIndex = index + itemnamelen
        index = line.find(unitstr, startIndex + 1)
        value = line [startIndex: index]
    print(value)
    return float(value)

while getvalue:

    line = ser.readline().decode()
    print(line)
    humidity = getvalue(line, " Humidity: ", '%')
    temperature = getvalue(line, " Temperature: ", '*C') 
    heat_index = getvalue(line, " Heat index: ", '*C')

    print('湿度=', humidity, '温度=', temperature, '体感温度=', heat_index)
            
   

 
  
