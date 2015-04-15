import RPi.GPIO as GPIO
import time

led = 29
led2 = 15
led3 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

turnondelay = 0.02500
turnoffdelay = 0.0500

try:
        for i in range(0, 1000) :
                GPIO.output(led, GPIO.HIGH)
                time.sleep(turnondelay)
                GPIO.output(led2, GPIO.HIGH)
                time.sleep(turnondelay)
                GPIO.output(led3, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led, GPIO.LOW)
                time.sleep(turnoffdelay)
                GPIO.output(led2, GPIO.LOW)
                time.sleep(turnoffdelay)
                GPIO.output(led3, GPIO.LOW)
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()
