# remote-controlled-robot
Robot powered by a Raspberrypi(receptor) and an Arduino Nano(emisor). This repository contains the documentation of a dual operation mode robot.

Mode 1: RF controller, using the NRF24L01+
  + For the emisor(Arduino Nano), the standar RF24.h library along with the SPI.h are used to send data.
  
  + For the reciver, lib form https://github.com/BLavery/lib_nrf24 along with simple modifications at the begin() function.
  
        def begin(self, csn_pin, ce_pin=0):   # csn & ce are RF24 terminology. csn = SPI's CE!
        # Initialize SPI bus..
        # ce_pin is for the rx=listen or tx=trigger pin on RF24 (they call that ce !!!)
        # CE optional (at least in some circumstances, eg fixed PTX PRX roles, no powerdown)
        # CE seems to hold itself as (sufficiently) HIGH, but tie HIGH is safer!
        self.spidev.open(0, csn_pin)
        self.spidev.max_speed_hz = 4000000   # THIS LINE WAS ADDED, SEEMS TO BE THAT THE PROBLEM IS FROM THE SPI LIB FROM RASP
        self.ce_pin = ce_pin


Mode 2: key-controlled over an interface with the raspberrypy and a computer.
