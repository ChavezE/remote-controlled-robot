#include "NRFControl.h"


RF24 myRadio (9, 10);



/* SET UP */
void setup()
{
	/* Begin Serial baudrate = 115200*/
	Serial.begin(115200);
	delay(1000);

	/* Set up for the NRF24L01+ module */

}

/* LOOP */
void loop()
{
	uint8_t testBuff[] = {0x01,0x02,0x03,0x04,0x05};
	writeNRF24(testBuff,sizeof(testBuff)/sizeof(testBuff[0]));

}