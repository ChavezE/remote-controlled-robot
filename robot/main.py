import RPi.GPIO as GPIO
import time
from NRFControl import *


def main():
    #############
    # Main Loop #
    #############
    while True:

        # if Package available, status from controller is 
        #   status = [j1_vertical, j1_horizontal, j2_vertical, j2_horizontal, pushbtns_bits]
        available, receivedMessage = getNRFPackage()
        if(available):
            print receivedMessage
       
            


if __name__ == '__main__':
    main()