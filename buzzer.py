import RPi.GPIO as GPIO
import time

BUZZ_PIN = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZ_PIN, GPIO.OUT)

GPIO.output(BUZZ_PIN, False)

print 'Getting ready to buzz'

pwm = GPIO.PWM(BUZZ_PIN, 1000)
pwm.start(0)
##pwm.ChangeDutyCycle(50)
##time.sleep(2)
##pwm.ChangeDutyCycle(20)
##time.sleep(2)
##pwm.ChangeDutyCycle(10)
##time.sleep(2)
##pwm.ChangeDutyCycle(90)
##time.sleep(2)

for dc in range(0, 100, 10):
    pwm.ChangeDutyCycle(dc)
    time.sleep(1)

for freq in range(1000, 10000, 200):
    pwm.ChangeFrequency(freq)
    time.sleep(0.5)


GPIO.cleanup()
