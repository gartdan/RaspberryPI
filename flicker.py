import RPi.GPIO as GPIO
import time
import random

pins = [11, 15, 29]
pwms = []
blink = 0.05

GPIO.setmode(GPIO.BOARD)

for(i, pin) in enumerate(pins):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 500)
    pwm.start(100)
    pwms.append(pwm)


try:
    while True:
        brightness = random.randint(0, 100)
        for(i, pwm) in enumerate(pwms):
            pwm.ChangeDutyCycle(brightness)
        time.sleep(blink)
except KeyboardInterrupt:
    GPIO.cleanup()
