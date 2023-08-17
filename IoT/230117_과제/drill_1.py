import RPi.GPIO as gpio
import time

switch_pin = 12

trig_pin = 13
echo_pin = 19

led_pin_g = 4
led_pin_y = 5
led_pin_r = 6

gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)

gpio.setup(led_pin_g, gpio.OUT)
gpio.setup(led_pin_y, gpio.OUT)
gpio.setup(led_pin_r, gpio.OUT)

gpio.setmode(gpio.BCM)
gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)

def button():
    isClicked = False
    if gpio.input(switch_pin) == 0:
        isClicked = True
    return isClicked

try:
    while True:
        if button() == True:
            print("Switch On")
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
            
            if distance >= 40.0 :
                gpio.output(led_pin_g, True)
                gpio.output(led_pin_y, False)
                gpio.output(led_pin_r, False)
               
                print("Distance 40 over :  %5.2f " % distance, " GREEN LED On")
                
            elif distance > 20.0:
                gpio.output(led_pin_g, False)
                gpio.output(led_pin_y, True)
                gpio.output(led_pin_r, False)
                print("Distance 20~40 :  %5.2f " % distance, " YELLOW LED On")
                
            else :
                gpio.output(led_pin_g, False)
                gpio.output(led_pin_y, False)
                gpio.output(led_pin_r, True)
                print("Distance 20 under :  %5.2f " % distance, " RED LED On")
                
            time.sleep(0.5)
                
        else :
            gpio.output(led_pin_g, False)
            gpio.output(led_pin_y, False)
            gpio.output(led_pin_r, False)
            print("Switch Off")
            time.sleep(0.5)
            
except KeyboardInterrupt:
    gpio.cleanup()