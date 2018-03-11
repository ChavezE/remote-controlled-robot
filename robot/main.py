import RPi.GPIO as GPIO
import time
from NRFControl import *
import RobotController
from motor import Motor


def main():
    GPIO.setmode(GPIO.BOARD)

    motorLF = Motor([3,5])      # GPIO  2 , 3
    motorLB = Motor([35,37])    # GPIO 19, 26
    motorRF = Motor([38,40])    # GPIO 20, 21
    motorRB = Motor([31,33])    # GPIO  6, 13

    # robot_controller = RobotController(motorLF, motorLB, motorRF, motorRB)

    #############
    # Main Loop #
    #############
    while True:
        motorLF.forward(50)
        motorLB.forward(50)
        motorRF.forward(50)
        motorRB.forward(50)

        # if Package available, status from controller is 
        #   status = [j1_vertical, j1_horizontal, j2_vertical, j2_horizontal, pushbtns_bits]
        # available, receivedMessage = getNRFPackage()
        # if(available):
        #     robot_controller.parseNewCommand(receivedMessage)
        #     print receivedMessage
       
            


if __name__ == '__main__':
    main()