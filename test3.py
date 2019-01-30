from gpiozero import LED,Button
from signal import pause

led=LED(23)
button=Button(24,pull_up=False)

button.when_pressed=led.on
button.when_released=led.off

pause()
