import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time

led_pin = 5

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("control/led")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Light : " + msg.payload.decode("utf-8"))
    if msg.payload.decode("utf-8") == "on" :
        gpio.output(led_pin, True)
          
            
    else :
        gpio.output(led_pin, False)
            

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("building/light")
    client.disconnect()
