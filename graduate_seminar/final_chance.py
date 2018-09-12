#!/usr/bin/env python
import cayenne.client
import time
import serial

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

# UART initialization:
ser = serial.Serial ("/dev/ttyAMA0", 9600, timeout=1)

# Cayenne authentication information. Obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "5a7d4fe0-d2cd-11e7-b556-b7f707866213"
MQTT_PASSWORD  = "25c23a742ed72996f997a430c4e072a7839053c4"
MQTT_CLIENT_ID = "cd52e270-72ad-11e8-84d1-4d9372e87a68"

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

timestamp0 = 0
timestamp1 = 0
n1_t = 0
n1_h = 0
n1_hdat = 0
n1_latitude = 0
n1_longitude = 0
n1_vandientu = 0
n2_t = 0
n2_h = 0
n2_hdat = 0
n2_latitude = 0
n2_longitude = 0
n2_pH = 0
n2_maybom = 0

while True:
    client.loop()
    if(time.time() > timestamp0 + 2):
        #IN DU LIEU LEN WEBSERVER CAYENNE NODE 1
        client.celsiusWrite(11, n1_t)
        client.virtualWrite(12, n1_h, TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
        client.virtualWrite(13, n1_hdat, TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
        client.virtualWrite(14, n1_latitude)
        client.virtualWrite(15, n1_longitude)
        client.virtualWrite(17, n1_vandientu)
        #IN DU LIEU LEN WEBSERVER CAYENNE NODE 2
        client.celsiusWrite(21, n2_t)
        client.virtualWrite(22, n2_h, TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
        client.virtualWrite(23, n2_hdat, TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT)
        client.virtualWrite(24, n2_latitude)
        client.virtualWrite(25, n2_longitude)
        client.virtualWrite(26, n2_pH)
        client.virtualWrite(29, n2_maybom)
        timestamp0 = time.time()
    if (time.time() > timestamp1 + 5):
       #LAY DU LIEU TU NODE 1
        node1getdata = "node1getdata"
        ser.write(node1getdata)
        n1_line = ser.readline()
        print(n1_line)
        n1_t = n1_line[6:8]
        n1_h = n1_line[9:11]
        n1_hdat = n1_line[12:14]
        n1_latitude = n1_line[15:24]
        n1_longitude = n1_line[25:35]
        n1_vandientu = n1_line[36:37]
       #LAY DU LIEU TU NODE 2
        node2getdata = "node2getdata"
        ser.write(node2getdata)
        n2_line = ser.readline()
        print(n2_line)
        n2_t = n2_line[6:8]
        n2_h = n2_line[9:11]
        n2_hdat = n2_line[12:14]
        n2_latitude = n2_line[15:24]
        n2_longitude = n2_line[25:35]
        n2_pH = n2_line[36:39]
        n2_maybom = n2_line[40:41] 
        timestamp1 = time.time()
