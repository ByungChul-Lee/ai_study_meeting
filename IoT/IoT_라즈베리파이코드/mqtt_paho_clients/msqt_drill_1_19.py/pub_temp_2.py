import paho.mqtt.client as mqtt
import random
import time

def getMsg():
    d = random.randrange(20, 30)
    msg = str(d)                
    return msg                

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("192.168.0.82")
mqttc.loop_start()

try:
    while True:
        t = getMsg()
        print("temp", t)
        
        infot = mqttc.publish("building/temperature", t)
        infot.wait_for_publish()
        
        time.sleep(2)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()

