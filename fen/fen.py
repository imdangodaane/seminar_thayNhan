#!/usr/bin/env python

import cayenne.client
import time
import serial

# UART initialization:
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0)

# Data types
TYPE_BATTERY = "batt" # Battery
TYPE_PROXIMITY = "prox" # Proximity
TYPE_RELATIVE_HUMIDITY = "rel_hum" # Relative Humidity
TYPE_VOLTAGE = "voltage" # Voltage
# Unit types
UNIT_PERCENT = "p" # % (0 to 100)
UNIT_RATIO = "r" # Ratio
UNIT_VOLTS = "v" # Volts
UNIT_CENTIMETER = "cm" # Centimeter
UNIT_METER = "m" # Meter
UNIT_DIGITAL = "d" # Digital (0/1)
UNIT_MILLIVOLTS = "mv" # Millivolts

# Cayenne authentication information. Obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "b1b00600-7457-11e8-b047-71b75b4bd75d"
MQTT_PASSWORD  = "5d43f8a4636b024c3e020035197563efe50150c9"
MQTT_CLIENT_ID = "6efa3340-7839-11e8-98bf-b1d14010b9df"

# The callback for when a message is received from Cayenne.
def on_message(message):
    if (message.channel == 16):
       packet_ch16 = str(message.channel) + str(message.value)
       ser.write(packet_ch16)
    elif (message.channel == 27):
       packet_ch27 = str(message.channel) + str(message.value)
       ser.write(packet_ch27)
    elif (message.channel == 28):
       packet_ch28 = str(message.channel) + str(message.value)
       ser.write(packet_ch28)

    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
timestamp = 0
clientstamp = 0
node = "node2getdata"


while True:
    client.loop()

    if(time.time() > timestamp + 60):
       if(node == "node2getdata"):
          node = "node1getdata"
       else:
          node = "node2getdata"
       print(node + " SENT@")
       ser.write(node)
       n_line = ser.readline()
       n_line = n_line.strip()
       n_line1 = n_line.split('|')
       print(n_line)
       print(n_line1)
       timestamp = time.time()

    if(time.time() > clientstamp + 10): 
       #node_c = n_line[0:5]
       if(n_line1[0] == "Node1"):

         #IN DU LIEU LEN WEBSERVER CAYENNE NODE 1
         client.celsiusWrite(11, n_line1[1])
         client.virtualWrite(12, n_line1[2], TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
         client.virtualWrite(13, n_line1[3], TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
         client.virtualWrite(14, n_line1[4])
         client.virtualWrite(15, n_line1[5])
         client.virtualWrite(17, n_line1[6])
       elif(n_line1[0] == "Node2"):

         #IN DU LIEU LEN WEBSERVER CAYENNE NODE 2
         client.celsiusWrite(21, n_line1[1])
         client.virtualWrite(22, n_line1[2], TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
         client.virtualWrite(23, n_line1[3])
         client.virtualWrite(24, n_line1[4])
         client.virtualWrite(25, n_line1[5])
         client.virtualWrite(29, n_line1[6])
       clientstamp = time.time()

