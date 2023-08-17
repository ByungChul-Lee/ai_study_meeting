import paho.mqtt.client as mqtt
import time
import random

import RPi.GPIO as gpio
import time

trig_pin = 13
echo_pin = 19
pir_pin = 12

gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)

gpio.setup(pir_pin, gpio.IN)


mqttc = mqtt.Client()

mqttc.connect("localhost")

mqttc.loop_start()

try:
    while True:
        if gpio.input(pir_pin) == True:
            gpio.output(trig_pin, False)
            time.sleep(0.5)

            gpio.output(trig_pin, True)
            time.sleep(0.00001)
            gpio.output(trig_pin, False)

            while gpio.input(echo_pin) == 0:
                pulse_start = time.time()

            while gpio.input(echo_pin) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 34000 / 2
            distance = round(distance, 2)
            infot = mqttc.publish("sensor/distance", distance)
            
            print("Distance : ", distance)
            
            infot.wait_for_publish()
        else:
            infot = mqttc.publish("sensor/person", 10000)
            print("Human not detected")
            infot.wait_for_publish()
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
