#!/usr/bin/env python
import cayenne.client
import time
# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "b1b00600-7457-11e8-b047-71b75b4bd75d"
MQTT_PASSWORD  = "5d43f8a4636b024c3e020035197563efe50150c9"
MQTT_CLIENT_ID = "4901b0a0-8b67-11e8-87b0-97a7dd91c15a"
# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)
a = 27
b = 80
timestamp = 0
while True:
    client.loop()
    if (time.time() > timestamp + 5):
        client.virtualWrite(23, a)
        client.virtualWrite(30, b)
        timestamp = time.time()

