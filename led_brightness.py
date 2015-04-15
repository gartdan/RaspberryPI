import RPi.GPIO as GPIO
import time

pin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 500)
pwm.start(100)

try:
    while True:
        str_brightness = input('Enter birghtness between 0 and 100')
        brightness = int(str_brightness)
        pwm.ChangeDutyCycle(brightness)
except KeyboardInterrupt:
    GPIO.cleanup()

