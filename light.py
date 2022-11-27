
import paho.mqtt.client as mqtt #import the client1
import time
def pub(msg):
    client = mqtt.Client("P1") #create new instance
    client.connect("broker.hivemq.com") #connect to broker
    client.publish("iot", str(msg))#publish
    time.sleep(1)

