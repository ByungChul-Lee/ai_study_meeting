import paho.mqtt.client as mqtt
import time
import random

import RPi.GPIO as gpio
import time

pir_pin = 12

gpio.setmode(gpio.BCM)
gpio.setup(pir_pin, gpio.IN)


mqttc = mqtt.Client()

mqttc.connect("localhost")

mqttc.loop_start()

try:
    while True:
        if gpio.input(pir_pin) == True:
            infot = mqttc.publish("sensor/person", 1)
            print("Human detected")
            infot.wait_for_publish()
        else:
            infot = mqttc.publish("sensor/person", 0)
            print("Human not detected")
            infot.wait_for_publish()
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
