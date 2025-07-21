import RPi.GPIO as GPIO
from time import sleep

step_pins = [17, 18, 27, 22]
sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

GPIO.setmode(GPIO.BCM)
for pin in step_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

for i in range(512):  # One full rotation
    for step in sequence:
        for pin in range(4):
            GPIO.output(step_pins[pin], step[pin])
        sleep(0.002)

GPIO.cleanup()
