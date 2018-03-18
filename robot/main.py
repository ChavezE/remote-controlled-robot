import RPi.GPIO as GPIO
import time
from NRFControl import *
from RobotController import RobotController
from motor import Motor


def main():
    GPIO.setmode(GPIO.BOARD)

    motorRF = Motor([3,5])      # GPIO  2 , 3 +
    motorRB = Motor([31,33])    # GPIO  6, 13


    motorLB = Motor([38,40])    # GPIO 20, 21  +
    motorLF = Motor([35,37])    # GPIO 19, 26  +
    

    robot_controller = RobotController(motorLF, motorLB, motorRF, motorRB)

    #############
    # Main Loop #
    #############
    while True:
        # motorLF.backward(50)
        # motorLB.backward(50)
        # motorRF.backward(50)
        # motorRB.backward(50)

        # if Package available, status from controller is 
        #   status = [j1_vertical, j1_horizontal, j2_vertical, j2_horizontal, pushbtns_bits]
        available, receivedMessage = getNRFPackage()
        if(available):
            robot_controller.parseNewCommand(receivedMessage)
            print receivedMessage
        else:
            motorRB.stop()
            motorRF.stop()
            motorLB.stop()
            motorLF.stop()
       
            


if __name__ == '__main__':
    main()