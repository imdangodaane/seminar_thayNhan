#!/usr/bin/env python
import serial
from time import sleep

ser = serial.Serial ("/dev/ttyAMA0", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    ser.write(received_data)                #transmit data serially 
    print (received_data)                   #print received data
