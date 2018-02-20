#include <SPI.h>  
#include "RF24.h"


#define WRITING_PIPE 	0xF0F0F0F0E1LL
#define READING_PIPE 	0xF1F1F1F1E1LL
#define NRF_CHANNEL 	0x76

#define SEND_DELAY_MS	100
#define SETUP_DELAY_MS	1000

#define CE_PIN 			9
#define CSN_PIN 		10

/* Declaring raido object, Params:
	First:		CE 	pin
	Second:		CSN pin
*/
RF24 radio(CE_PIN, CSN_PIN);



void setupNRF24(){
	radio.begin(); 

	radio.setChannel(NRF_CHANNEL); 
	radio.setPALevel(RF24_PA_MAX);
	radio.setDataRate(RF24_1MBPS);

	radio.openWritingPipe(WRITING_PIPE);
	radio.enableDynamicPayloads();
	radio.powerUp();
	delay(SETUP_DELAY_MS);
}

void writeNRF24(uint8_t send_buffer[], uint8_t byte_count){
	radio.write(send_buffer,byte_count);
	delay(SEND_DELAY_MS);
}