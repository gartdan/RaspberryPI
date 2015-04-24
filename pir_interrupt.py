import RPi.GPIO as GPIO
import time, os, subprocess

GPIO.setmode(GPIO.BCM)

pir_pin = 12

GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

def say_something(something):
	subprocess.call(["./button-to-speech/speech.sh", something])

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
        blink(1, 1.25)
        blink(2, 1)
        blink(2, 0.5)
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

def motion_handler(pin):
        print("Motion Detected!")
        say_something("Hi there Veronica. I heard your favorite color is pink. I made some pretty lights for you.")
        lightShow()

print("Awaiting motion...")

try:
        GPIO.add_event_detect(pir_pin, GPIO.RISING, callback=motion_handler)
        while True:
                time.sleep(5.00)
except KeyboardInterrupt:
    GPIO.cleanup()
