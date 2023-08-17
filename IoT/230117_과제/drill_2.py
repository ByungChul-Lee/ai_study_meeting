import spidev
import RPi.GPIO as gpio
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 976000

light_channel = 0

switch_pin = 12
led_pin = 5

gpio.setmode(gpio.BCM)

gpio.setup(led_pin, gpio.OUT)

gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)

def button():
    isClicked = False
    if gpio.input(switch_pin) == 0:
        isClicked = True
    return isClicked

def readChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((adc[1] & 3) << 8) + adc[2]
    return adc_out
    
def convert2volts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts
    
try:
    while True:
        light_level = readChannel(light_channel)
        light_volts = convert2volts(light_level, 2)
        
        print("-------------------------------------")
        print("Light: %d (%f V)" %(light_level, light_volts))
        
        if light_level <=700 :
            gpio.output(led_pin, True)
            print("Light level 700 under LED ON")
            
        elif button() == True:
            gpio.output(led_pin, True)
            print("SWITCH ON and LED ON")
            
        else :
            gpio.output(led_pin, False)
            print("SWITCH OFF and LED OFF")
        
        time.sleep(0.2)
    
except KeyboardInterrupt:
    print("Finished")
    spi.close()