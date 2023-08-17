import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import time

led_pin_g = 4
led_pin_y = 5
led_pin_r = 6

gpio.setmode(gpio.BCM)


gpio.setup(led_pin_g, gpio.OUT)
gpio.setup(led_pin_y, gpio.OUT)
gpio.setup(led_pin_r, gpio.OUT)



def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("control/led")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Light : " + msg.payload.decode("utf-8"))

    if msg.payload.decode("utf-8") == "green" :
        gpio.output(led_pin_g, True)
        gpio.output(led_pin_y, False)
        gpio.output(led_pin_r, False)
    elif msg.payload.decode("utf-8") == "yellow" :
        gpio.output(led_pin_g, False)
        gpio.output(led_pin_y, True)
        gpio.output(led_pin_r, False)
    
    elif msg.payload.decode("utf-8") == "red"  :       
        gpio.output(led_pin_g, False)
        gpio.output(led_pin_y, False)
        gpio.output(led_pin_r, True) 
            
    else :
        gpio.output(led_pin_g, False)
        gpio.output(led_pin_y, False)
        gpio.output(led_pin_r, False) 
            

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("control/light")
    client.disconnect()
