#!/usr/bin/env python
import cayenne.client
import time
import serial

# UART initialization:
ser = serial.Serial ("/dev/ttyAMA0")

# Cayenne authentication information. Obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "5a7d4fe0-d2cd-11e7-b556-b7f707866213"
MQTT_PASSWORD  = "25c23a742ed72996f997a430c4e072a7839053c4"
MQTT_CLIENT_ID = "cd52e270-72ad-11e8-84d1-4d9372e87a68"

# The callback for when a message is received from Cayenne.
def on_message(message):
   #dat nguong nhiet do (node1)
    if (message.channel == 16):
       packet_ch15 = str(message.channel) + str(message.value)
       ser.write(packet_ch16)
       print(packet_ch16)

   #dat khoang thoi gian bom luan phien (node2)
    elif (message.channel == 27):
       packet_ch26 = str(message.channel) + str(message.value)
       ser.write(packet_ch27)
       print(packet_ch27)

   #ON/OFF may bom
    elif (message.channel == 28):
       packet_ch27 = str(message.channel) + str(message.value)
       ser.write(packet_ch28)
       print(packet_ch28)
         

    chnl = int(message.channel)
    if   (chnl < 10):
       node = '0'
    elif (chnl >  9 and chnl < 20):
       node = '1'
    elif (chnl > 19 and chnl < 30):
       node = '2'
    elif (chnl > 29 and chnl < 40):
       node = '3'
    elif (chnl > 39 and chnl < 50):
       node = '4'
    elif (chnl > 49 and chnl < 60):
       node = '5'

    print ("Node=" + node)
    print ("Topic=" + str(message.topic))
    print ("Channel=" + str(message.channel))
    print ("Value=" + str(message.value))

    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

timestamp = 0

while True:
    client.loop()
   #LAY DU LIEU TU NODE 1
    node1getdata = 'node1getdata'
    ser.write(node1getdata)
    n1_line = ser.readline()
    n1_t = n1_line[6:8]
    n1_h = n1_line[9:11]
    n1_hdat = n1_line[12:14]
    n1_latitude = n1_line[15:24]
    n1_longtitude = n1_line[25:35]
    n1_vandientu = n1_line[36:37]

   #LAY DU LIEU TU NODE 2
    node2getdata = 'node2getdata' 
    ser.write(node2getdata)
    n2_line = ser.readline()
    n2_t = n2_line[6:8]
    n2_h = n2_line[9:11]
    n2_hdat = n2_line[12:14]
    n2_latitude = n2_line[15:24]
    n2_longtitude = n2_line[25:35]
    n2_pH = n2_line[36:39]
    n2_maybom = n2_line[40:41]

    if (time.time() > timestamp + 1):
       client.celsiusWrite(11, n1_t)
       client.virtualWrite(12, n1_h)
       client.virtualWrite(13, n1_hdat)
       client.virtualWrite(14, n1_latitude)
       client.virtualWrite(15, n1_longtitude)
       client.virtualWrite(17, n1_vandientu)

       client.celsiusWrite(21, n2_t)
       client.virtualWrite(22, n2_h)
       client.virtualWrite(23, n2_hdat)
       client.virtualWrite(24, n2_latitude)
       client.virtualWrite(25, n2_longtitude)
       client.virtualWrite(26, n2_pH)
       client.virtualWrite(29, n2_maybom)
       timestamp = time.time()
    print(n1_line)
    print(n2_line)
