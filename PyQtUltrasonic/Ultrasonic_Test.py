# -*- coding: utf-8 -*-

import serial

ser = serial.Serial('COM4', 9600)

distance = 0
getvalueok = True
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

while getvalueok:

    line = ser.readline().decode()
    print(line)
    
    distance = getvalue(line, ' Distance ', 'cm')

    print('Distance=', distance)
            
   

 
  
