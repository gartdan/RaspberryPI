from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 100)
pwm.start(5)

def set(property, value)
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()
    except:
        print("error writing to "+ property + " value: " + value)

def setServo(angle)
    set("servo", str("angle"))

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
                      orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)



#root = Tk()
#root.wm_title('Servo Control')
#app = App(root)
#root.geometry("200x50+0+0")
#root.mainloop()

set("delayed", 0)
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

delay_period = 0.01

while True:
    for angle in range(0, 180)
        setServo(angle)
        time.sleep(delay_period)
    for(angle in range(0, 180)
        setServo(180-angle)
        time.sleep(delay_period)

        
