#include "NRFControl.h"



/* SET UP */
void setup()
{
	/* Begin Serial baudrate = 115200*/
	Serial.begin(115200);
	delay(1000);

	/* Set up for the NRF24L01+ module */
	setupNRF24();
}

/* LOOP */
void loop()
{
	static uint8_t count = 0;
	// Status register
	uint8_t testBuff[] = {0x01,0x02,0x03,0x04,(count++)};

	/*
		Code	
	*/

	// calling write function
	writeNRF24(testBuff,sizeof(testBuff)/sizeof(testBuff[0]));

}
