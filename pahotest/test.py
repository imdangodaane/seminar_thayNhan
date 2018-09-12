import paho.mqtt.client as mqtt
import time

data='Hello from Raspberry Pi!'
data2='CV dep trai'
client=mqtt.Client()
client.username_pw_set("lenbaxjq","Cp6Gt00Sq3Ra")#replace with your user name and password
client.connect("m13.cloudmqtt.com",13336,60)
while True:
  client.publish("pi",data2)#pi is topic
  time.sleep(1)
client.disconnect()
