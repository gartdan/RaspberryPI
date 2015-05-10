import RPi.GPIO as GPIO
import time

TRIG_PIN = 23
ECHO_PIN = 24

print 'Distance Measurement in Progress'

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(TRIG_PIN, False)

def trigger():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

def get_distance():
    while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
    

print 'Waiting for sensor to settle'

time.sleep(2)

try:
    while True:
        trigger()
        distance = get_distance()
        print "Distance: ", distance, "cm"
        time.sleep(1)
finally:
    GPIO.cleanup()
