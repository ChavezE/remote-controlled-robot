#include "RobotController.h"
#include "Motor.h"


// LOS PINES DE LOS MOTORES TALVES ESTAN ALREVES. Ejem [10,9] en vez de [9, 10]
uint8_t pinMotorLF[2]{9,10};
uint8_t pinMotorLB[2]{4,5};
uint8_t pinMotorRF[2]{11,12};
uint8_t pinMotorRB[2]{2,3}; 

Motor motorLF(pinMotorLF[0], pinMotorLF[1]);
Motor motorLB(pinMotorLB[0], pinMotorLB[1]);
Motor motorRF(pinMotorRF[0], pinMotorRF[1]);
Motor motorRB(pinMotorRB[0], pinMotorRB[1]);

RobotController robotController(motorLF, motorLB, 
    motorRF, motorRB);

void setup() {

    // SETUP UP NRF24
}

void loop() {
    uint8_t arrayCommands[5];

    //READ COMMAND ARRAY

    robotController.parseNewCommand(arrayCommands);
}
