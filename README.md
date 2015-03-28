# SIGFOX_KAP_PYTHON
Python code example to control the key app device through serial AT commands


## Introduction

SIGFOX - http://sigfox.com/ - is the first and only company providing global cellular connectivity for the Internet of Things, fully dedicated to low-throughput communications. SIGFOX is re-inventing connectivity by radically lowering prices and energy consumption for connected devices.
Your device connects to SIGFOX network and the messages received are pushed to the customer’s backend trhough an API.

    device <---> antennas <---> SIGFOX cloud <---> your backend

The purpose of this turorial is to show a simple integration of the API in the case of a rails application.

## Key app
Key app are demo devices that allow to connect to SIGFOX network. You can control them through a serial connection so you can connect it to your computer, a raspberry pi, an arduino... 
This python 2 and 3 code example allows you to connect very easily to the key app. You can then build your own application around and then use this piece of code to send the data to SIGFOX's network.

## Pyserial library
You will have to onstall this library before using the code. You can find several tutorials online. Here is one <http://www.zilogic.com/blog/tutorial-pyserial.html>

## Code to change
The serial port name can be different from one device to another depending on which OS you are on (linux users - you should be fine). You have to make to change the name to the good serial port accordingly to the key app connected.
Also the data payload to send will depend on the application you are building. So feel free to change it!


