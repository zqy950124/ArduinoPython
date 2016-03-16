
TornadoArduinoDHT11
===========

Tornado web server on PC which listens for serial communication from Arduino 

TornadoArduinoDHT11 enables real time plotting of DHT11 signals in the browser

## Technical

tornado server + websocket + flotr2

## Python package

    python-serial
    tornado

## Arduino sketch  

 Open DHTSensor.ino, build and upload it  

## Launching the server

python app.py

## Enjoying live data

Open a web browser and go to :

   http://localhost:8000  

You should see the graph window and be able to select the curves to display.
