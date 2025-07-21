import RPi.GPIO as GPIO
from time import sleep

in1, in2, en = 17, 27, 22

GPIO.setmode(GPIO.BCM)
GPIO.setup([in1, in2, en], GPIO.OUT)

pwm = GPIO.PWM(en, 1000)
pwm.start(50)  # 50% duty cycle

# Forward
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
sleep(2)

# Reverse
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
sleep(2)

# Stop
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
pwm.stop()
GPIO.cleanup()
