import RPi.GPIO as GPIO
import os, subprocess, time


TRIG_PIN = 23
ECHO_PIN = 24
BUZZ_PIN = 25

ENABLE_BUZZ = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZ_PIN, GPIO.OUT)

GPIO.output(TRIG_PIN, False)
GPIO.output(BUZZ_PIN, False)

pwm = GPIO.PWM(BUZZ_PIN, 1000)

def say(something):
	subprocess.call(["./button-to-speech/speech.sh", something])

print 'Distance Measurement in Progress'
say('Distance Measurement in Progress')



def init_buzzer():
    pwm.start(0)

if ENABLE_BUZZ:
    init_buzzer()

def buzz(distance_in_meters):
    freq_factor = 1000
    # if you are 5 meters away, it should sound at 1000 / 5 = 200 hz
    # if you are 1 meter away, it will become more shrill: 1000 / 1 = 1000 hz
    # if you are all up in its face (e.g. 10 cm) it will shreik: 1000 / 0.1 = 10000hz
    if distance_in_meters > 5:
        #stop the buzzer
        pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeDutyCycle(80)
        freq = freq_factor / distance_in_meters
        #lets not get too high pitched
        if freq > 10000:
            freq = 10000
        pwm.ChangeFrequency(freq)
        

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

def too_close():
    say('You are too close!. Stand back!')
    time.sleep(1)
    

print 'Waiting for sensor to settle'

time.sleep(2)

try:
    while True:
        trigger()
        distance = get_distance()
        distance_in_meters = distance / 100.0
        print "Distance: ", distance, "cm ", distance_in_meters, "m"

        if distance <= 100:
            too_close()
        if ENABLE_BUZZ:
            buzz(distance_in_meters)
        time.sleep(1)
finally:
    GPIO.cleanup()
