#include "NRFControl.h"
#include "Utilities.h"


// Joysticks analog pins
const uint8_t pinJ1Vert = A6; 
const uint8_t pinJ1Horiz = A7;
const uint8_t pinJ2Vert = A0;
const uint8_t pinJ2Horiz = A1;

// Buttons pins
const uint8_t pinJ1Btn;
const uint8_t pinJ2Btn;
const uint8_t pinBtnA;
const uint8_t pinBtnB;
const uint8_t pinBtnC;
const uint8_t pinBtnD;


/* SET UP */
void setup()
{
	// Init as input or outputs the pins
	pinMode(pinJ1Vert, INPUT);
	pinMode(pinJ1Horiz, INPUT);
	pinMode(pinJ2Vert, INPUT);
	pinMode(pinJ2Horiz, INPUT);

	// pinMode(pinJ1Btn, INPUT);
	// pinMode(pinJ2Btn, INPUT);
	// pinMode(pinBtnA, INPUT);
	// pinMode(pinBtnB, INPUT);
	// pinMode(pinBtnC, INPUT);
	// pinMode(pinBtnD, INPUT);


	/* Begin Serial baudrate = 115200*/
	Serial.begin(115200);
	delay(1000);

	/* Set up for the NRF24L01+ module */
	setupNRF24();
}

/* LOOP */
void loop()
{
	uint8_t command[5];

	// Read and map the values analog values to be between 0 and 255
	command[0] = map(analogRead(pinJ1Vert), 0, 1023, 0, 255);
	command[1] = map(analogRead(pinJ1Horiz), 0, 1023, 0, 255);
	command[2] = map(analogRead(pinJ2Vert), 0, 1023, 0, 255);
	command[3] = map(analogRead(pinJ2Horiz), 0, 1023, 0, 255);

	// Read the values of the buttons and insert them in the number in command[4]
	command[4] = 0;
	// command[4] = addBoolValueInInt(digitalRead(pinJ1Btn), 0, 0);
	// command[4] = addBoolValueInInt(digitalRead(pinJ2Btn), 1, command[4]);
	// command[4] = addBoolValueInInt(digitalRead(pinBtnA), 2, command[4]);
	// command[4] = addBoolValueInInt(digitalRead(pinBtnB), 3, command[4]);
	// command[4] = addBoolValueInInt(digitalRead(pinBtnC), 4, command[4]);
	// command[4] = addBoolValueInInt(digitalRead(pinBtnD), 5, command[4]);


	// calling write function
	writeNRF24(command, 5);

}
