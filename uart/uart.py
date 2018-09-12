#!usr/bin/env python
import RPi.GPIO as GPIO
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
ser = serial.Serial ("/dev/ttyAMA0")
while True:
   #s = ser.read()
   a = ser.readline()
   print (a)
#      if (s == '1'):
#         GPIO.output(20, 1)
#      elif (s == '2'):
#         GPIO.output(21, 1)
#      elif (s == '0'):
#         GPIO.output(20, 0)
#         GPIO.output(21, 0)
#      del s
