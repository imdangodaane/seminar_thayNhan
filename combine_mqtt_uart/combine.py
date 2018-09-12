#!/usr/bin/env python
import cayenne.client
import time
import serial

# UART initialization:
ser = serial.Serial ("/dev/ttyAMA0")

# Cayenne authentication information. Obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "5a7d4fe0-d2cd-11e7-b556-b7f707866213"
MQTT_PASSWORD  = "25c23a742ed72996f997a430c4e072a7839053c4"
MQTT_CLIENT_ID = "ab6ae910-600a-11e8-a700-878cdd8a64eb"

# The callback for when a message is received from Cayenne.
def on_message(message):
    if (message.channel == 11):
       if (message.value == '1'):
          ser.write('1')
       else:
          ser.write('0')
    elif (message.channel == 22):
       if (message.value == '1'):
          ser.write('2')
       else:
          ser.write('0')
    elif (message.channel == 7):
       nguong = str(message.value)
       ser.write(nguong)
       print(nguong)
    elif (message.channel == 8):
       dc_delay = str(message.value)
       ser.write(str(message.channel))
       ser.write(dc_delay)
       print(dc_delay)

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

i=0
timestamp = 0

while True:
    client.loop()
    line = ser.readline()
    t = line[7:11] 
    h = line[25:30]
    #print (line)
    #print (t)
    #print (h)

    if (time.time() > timestamp + 2):
        client.virtualWrite(0, t)
        client.virtualWrite(1, h)
        #client.celsiusWrite(1, i)
        #client.luxWrite(2, i*10)
        #client.hectoPascalWrite(3, i+800)
        #client.celsiusWrite(255, i*20)
        timestamp = time.time()
        i = i+1



