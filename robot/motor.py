import RPi.GPIO as gpio

class Motor:

    # Max value of PWM
    MAX_PWM_VALUE = 100

    # default frequency
    freq = 1000
    # Pins of Motors
    MotorPins = None

    # Initilalize the motor, pins should be a list of 2 numbers, red and black wire of motor.
    def __init__(self, pins):
        self.MotorsPins = pins
        # Set pins as OUTPUTS, default freq and start them at 0
        gpio.setup(pins[0], gpio.OUT)
        gpio.PWM(pins[0], self.freq).start(0)
        gpio.setup(pins[1], gpio.OUT)
        gpio.PWM(pins[1], self.freq).start(0)

    # Set Motor to move forward with a duty cycle of v (0 - 100)
    def forward(self, v):
        gpio.PWM(self.MotorsPins[0], self.freq).ChangeDutyCycle(v)
        gpio.PWM(self.MotorsPins[1], self.freq).ChangeDutyCycle(0)

    # Set Motor to move backward with a duty cycle of v (0 - 100)
    def backward(self, v):
        gpio.PWM(self.MotorsPins[0], self.freq).ChangeDutyCycle(0)
        gpio.PWM(self.MotorsPins[1], self.freq).ChangeDutyCycle(v)

    # Clean GPIO's
    def __exit__(self):
        gpio.cleanup()
