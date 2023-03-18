#import libraries
#from machine import Pin
import utime
from machine import ADC, Pin
import RPi.GPIO as GPIO
#import spidev.GPIO as GPIO

#GPIO setup pin 29 as moisture sensor inpu

GPIO. setmode(GPIO.BOARD)
GPIO.setup(20,GPIO.IN)

try:
    while True:
        if (GPIO.input(20))==0:
            print('Wet')
        elif (GPIO.input(20) )==1:
            print('Dry')
        time.sleep(.25)

finally:
#cleanup the GPIO pins before ending
    GPIO.cleanup()
