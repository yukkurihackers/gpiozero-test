#This is test2.py Thank you for seeing this program code!!!
from gpiozero import Button,LED
from signal import pause

def say_hello():
    print("Hello!")
    
button1 = Button(24, pull_up=False)

button1.when_pressed = say_hello

pause()
