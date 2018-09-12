#!/usr/bin/env python
import cayenne.client
import time
import RPi.GPIO as GPIO

# GPIO_SETUP.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT, initial=0)
GPIO.setup(20, GPIO.OUT, initial=0)

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "5a7d4fe0-d2cd-11e7-b556-b7f707866213"
MQTT_PASSWORD  = "25c23a742ed72996f997a430c4e072a7839053c4"
MQTT_CLIENT_ID = "ab6ae910-600a-11e8-a700-878cdd8a64eb"


# The callback for when a message is received from Cayenne.
def on_message(message):
    #print("message received: " + str(message))
    #a = str(message)
    #channel = a[74:76]
    #value = a[29]
    # Xu ly tin hieu channel de biet NODE.
    channel_n = int(message.channel)
    if (channel_n < 10):
       node = '0' 
    elif (channel_n > 9 and channel_n < 20):
       node = '1'
    else:
       node = '2'

    #node = str(node)
    #print ("\nRX=" + a + "\n")

    print ("Node=" + node)

    #print ("Channel=" + channel)
    #print ("Value=" + value)
    #print ("\n")

    print ("Topic=" + str(message.topic))
    print ("Channel=" + str(message.channel))
    print ("Value=" + str(message.value))

    if (node == '1'):
       if (message.value == '1'):
          GPIO.output(20, 1)
       else:
          GPIO.output(20, 0)
    elif (node == '2'):
       if (message.value == '1'):
          GPIO.output(21, 1)
       else:
          GPIO.output(21, 0)

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

    if (time.time() > timestamp + 1):
        #client.celsiusWrite(1, i)
        #client.luxWrite(2, i*10)
        #client.hectoPascalWrite(3, i+800)
        #client.celsiusWrite(255, i*20)
        timestamp = time.time()
        i = i+1

