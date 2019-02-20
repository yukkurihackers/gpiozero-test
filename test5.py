#This is my fifth program
from gpiozero import Servo
from time import sleep

servo1 = servo(17,min_pulse_width=0.55/1000,max_pulse_width=2.60/1000,frame_width=25/1000)
while True:
    servo1.min()
    sleep(1)
    servo1.mid()
    sleep(1)
    servo1.max()
    sleep(1)