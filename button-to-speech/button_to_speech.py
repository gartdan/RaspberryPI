#!/usr/bin/python
import time, os, subprocess
import RPi.GPIO as GPIO


# set up GPIO on pin 17 for button press
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.OUT)


def say_something(something):
        subprocess.call(["chmod", "u+x", "./speech.sh"])
	subprocess.call(["./speech.sh", something])

try:
        while True:
                if GPIO.input(17)== False:
                        print('Button 1 Pressed')
                        GPIO.output(22, GPIO.HIGH)
                        say_something('You pressed button 1')
                if GPIO.input(18) == False:
                        print('Button 2 Pressed')
                        GPIO.output(22, GPIO.LOW)
                        say_something('You pressed button 2')
                time.sleep(0.2)
finally:
        GPIO.cleanup()
                
