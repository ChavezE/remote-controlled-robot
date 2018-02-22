import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev


######################
# Defining constants #
######################

PAYLOAD_SIZE 	= 32
NRF_CHANNEL 	= 0x76
WRITING_PIPE	= [0xE8, 0xE8, 0xF0, 0xF0, 0xE1]
READING_PIPE 	= [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]



######################
# NRF24 setup		 #
######################


# Seting GIPIO nomenclature as Board
GPIO.setmode(GPIO.BOARD)

# Declaring radio object
radio = NRF24(GPIO, spidev.SpiDev())

# CE and SCK
radio.begin(0, 11)

# Common params
radio.setPayloadSize(PAYLOAD_SIZE)
radio.setChannel(NRF_CHANNEL)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

# Print details of configuration
radio.printDetails()

# Open Reading Pipe and start listening
radio.openReadingPipe(1,READING_PIPE)
radio.startListening()



######################
# Functions			 #
######################

def getNRFPackage():
	 # check if new package is received
    if(radio.available(0)):
        receivedMessage = []
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
        return True, receivedMessage
    # if no data, sent False and empty list
    else:
        time.sleep(0.1)
        return False, []

