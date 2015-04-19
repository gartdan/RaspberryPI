import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.OUT)

try:
    while True:
        if(GPIO.input(17) == False):
            print('Button 1 pressed')
            GPIO.output(22, GPIO.HIGH)
        if(GPIO.input(18) == False):
            print('Button 2 pressed')
            GPIO.output(22, GPIO.LOW)
        time.sleep(0.2)
finally:
    GPIO.cleanup()
        
