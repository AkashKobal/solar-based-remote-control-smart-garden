from machine import Pin
import utime

 

#f lect for mot tput, Setting pin
motor_out = machine.Pin(16, machine.Pin.OUT)

#ect for butt

button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)

 

while True:
    if button.value() == 1:
        motor_out.value(1)
        print ('motor on')
        utime.sleep(2)
        print ('motor off')
        motor_out .value(0)
