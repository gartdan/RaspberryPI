import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

def blink(numTimes, duration):
    for x in range(1, numTimes):        
        showLights()
        time.sleep(duration)
        hideLights()
        time.sleep(duration/2.0)

def showLights():
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)

def hideLights():
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

def lightShow():
    print('Starting the light show')
    for x in range(0, 2):
        blink(2, 1.5)
        blink(2, 1.25)
        blink(2, 1)
        blink(3, 0.5)
        blink(20, 0.25)
        blink(40, 0.1)
        blink(1, 3)
        blink(1, 5)
        blink(1, 2)
        blink(1, 1)
        blink(3, 0.5)
        blink(5, 0.25)
        blink(20, 0.1)
    print('Light show is complete.')
        
        

lightShow()



GPIO.cleanup()
