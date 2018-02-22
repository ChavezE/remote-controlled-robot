import RPi.GPIO as GPIO
import time
from NRFControl import *
import RobotController
import motor


def main():
    motorLF = Motor([0,0])
    motorLB = Motor([0,0])
    motorRF = Motor([0,0])
    motorRB = Motor([0,0])

    robot_controller = RobotController(motorLF, motorLB, motorRF, motorRB)

    #############
    # Main Loop #
    #############
    while True:

        # if Package available, status from controller is 
        #   status = [j1_vertical, j1_horizontal, j2_vertical, j2_horizontal, pushbtns_bits]
        available, receivedMessage = getNRFPackage()
        if(available):
            robot_controller.parseNewCommand(receivedMessage)
       
            


if __name__ == '__main__':
    main()