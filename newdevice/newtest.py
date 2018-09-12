#!/usr/bin/env python
import cayenne.client
import time
# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "b1b00600-7457-11e8-b047-71b75b4bd75d"
MQTT_PASSWORD  = "5d43f8a4636b024c3e020035197563efe50150c9"
MQTT_CLIENT_ID = "49ba49c0-8a8c-11e8-9c05-61f9e9bc1eea"
# The callback for when a message is received from Cayenne.
def on_message(message):
    print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.
client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)
a = 55
b = 99
timestamp = 0
while True:
    client.loop()
    if (time.time() > timestamp + 10):
        client.virtualWrite(1, a)
        client.virtualWrite(20, b)
        timestamp = time.time()

