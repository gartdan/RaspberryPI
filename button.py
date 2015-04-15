import RPi.GPIO as GPIO
import time

pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try: 
    while True:
            input_state = GPIO.input(pin)
            if input_state == False:
                print('Button Pressed')
                time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
