#!/usr/bin/env python
import time
import serial

# UART initialization:
ser = serial.Serial ("/dev/ttyAMA0", 9600,timeout=0)

while True:
    node1getdata = "node1getdata"
    ser.write(node1getdata)
    n1_line = ser.readline()
    n1 = n1_line.strip()  
    print(n1)
    time.sleep(5)
    node2getdata = "node2getdata"
    ser.write(node2getdata)
    n2_line = ser.readline()
    n2 = n2_line.strip() 
    print(n2)
    time.sleep(5)
