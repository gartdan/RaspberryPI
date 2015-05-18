import os, subprocess, glob, time
import RPi.GPIO as GPIO

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
          time.sleep(0.2)
          lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
          temp_string = lines[1][equals_pos+2:]
          temp_c = float(temp_string) / 1000.0
          temp_f = temp_c * 9.0 / 5.0 + 32
          return temp_c, temp_f

def say_temp():
    temp_c, temp_f = read_temp()
    msg1 = 'The temp in Celsius is ' + str(temp_c) + ' degrees.'
    print msg1
    say_something(msg1)
    msg2 = 'The temp in farenheight is '+ str(temp_f)  + ' degrees.'
    print msg2
    say_something(msg2)

def say_something(something):
	subprocess.call(["./button-to-speech/speech.sh", something])


print('Waiting for input')
try:  
    while True:
            if GPIO.input(pin)== False:
                    say_temp()
            time.sleep(0.2)
finally:
    GPIO.cleanup()
