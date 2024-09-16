import RPi.GPIO as GPIO
from time import sleep

# init configs
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor 1 (EN1, IN1, IN2)
Ena, In1, In2 = 2, 3, 4
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
pwm1 = GPIO.PWM(Ena, 100)
pwm1.start(0)

# Motor 2 (ENB, IN3, IN4)
Enb, In3, In4 = 17, 27, 22
GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)
pwm2 = GPIO.PWM(Enb, 100)
pwm2.start(0)

while True:
    # Motor 1 forward
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm1.ChangeDutyCycle(30)

    # Motor 2 forward
    GPIO.output(In3, GPIO.LOW)
    GPIO.output(In4, GPIO.HIGH)
    pwm2.ChangeDutyCycle(30)

    sleep(5)

    # Stop both motors
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    sleep(5)
