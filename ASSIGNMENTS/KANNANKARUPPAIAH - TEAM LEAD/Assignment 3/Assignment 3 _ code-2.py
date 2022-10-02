from gpiozero import Button, TrafficLights, Buzzer
from time import sleep

buzzer = Buzzer(15)
button = Button(21)
lights = TrafficLights(25, 8, 7)

while True:
    button.wait_for_press()
    buzzer.on()
    light.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
    buzzer.off()
