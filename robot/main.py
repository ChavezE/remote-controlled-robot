import RPi.GPIO as GPIO
import time
from NRFControl import *


def main():
    #############
    # Main Loop #
    #############
    while True:

        # if Package available, status from controller is 
        #   status = [X_vertical,Y_vertical,X_horizontal, Y_vertial, pushbtns_bits]
        available,status = getNRFPackage()
        if(available):
            print status
       
            


if __name__ == '__main__':
    main()