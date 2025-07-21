import RPi.GPIO as GPIO
from time import sleep

motor_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

pwm = GPIO.PWM(motor_pin, 1000)  # 1kHz frequency
pwm.start(0)

for duty in range(0, 101, 20):
    pwm.ChangeDutyCycle(duty)
    print(f"Speed: {duty}%")
    sleep(1)

pwm.stop()
GPIO.cleanup()
