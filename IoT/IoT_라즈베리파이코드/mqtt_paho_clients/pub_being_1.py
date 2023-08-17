import paho.mqtt.client as mqtt
import time
import random

def getMsg():
    d = random.random()
    if d > 0.5:
        msg = 1
    else :
        msg =0
    return msg       

mqttc = mqtt.Client()

mqttc.connect("192.168.0.82")

mqttc.loop_start()

try:
    while True:
        t = getMsg()
        print("Human ????", t)
        
        infot = mqttc.publish("building/person", t)
        infot.wait_for_publish()
        
        time.sleep(3)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
