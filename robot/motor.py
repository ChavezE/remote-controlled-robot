import RPi.GPIO as GPIO


class Motor:

    # Max value of PWM
    MAX_PWM_VALUE = 100


    # Initilalize the motor, pins should be a list of 2 numbers, red and black wire of motor.
    def __init__(self, pins):
        GPIO.setmode(GPIO.BOARD)
        self.motorsPWM = []
        # default frequency
        self.freq = 1000

        # Set pins as OUTPUTS, default freq and start them at 0
        GPIO.setup(pins[0], GPIO.OUT)
        self.motorsPWM.append(GPIO.PWM(pins[0], self.freq))
        self.motorsPWM[0].start(0)

        GPIO.setup(pins[1], GPIO.OUT)
        self.motorsPWM.append(GPIO.PWM(pins[1], self.freq))
        self.motorsPWM[1].start(0)

    # Set Motor to move forward with a duty cycle of v (0 - 100)
    def forward(self, v):
        self.motorsPWM[0].ChangeDutyCycle(v)
        self.motorsPWM[1].ChangeDutyCycle(0)

    # Set Motor to move backward with a duty cycle of v (0 - 100)
    def backward(self, v):
        self.motorsPWM[0].ChangeDutyCycle(0)
        self.motorsPWM[1].ChangeDutyCycle(v)

    # Stop the motor
    def stop(self):
        self.motorsPWM[0].ChangeDutyCycle(0)
        self.motorsPWM[1].ChangeDutyCycle(0)

    # Clean GPIO's
    def __exit__(self):
        GPIO.cleanup()
