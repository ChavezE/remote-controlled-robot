#ifndef ROBOT_CONTROLLER_H
#define ROBOT_CONTROLLER_H

#include "math.h"
#include "Motor.h"

class RobotController {
public:
    RobotController(const Motor motorLF, const Motor motorLB, const Motor motorRF, const Motor motorRB);

    void parseNewCommand(uint8_t commandArray[5]);


private:
    void moveWithCommandsValue(uint8_t commandArray[5]);
    void fromRectangularOfControllerToPolar(int xComponent, int yComponent, int &magnitud, int &angle);
    int fromPiMinusPiPlusTo360Angle(double angle);

    const int HALF_VALUE_JOYSTICK = 127;

    const Motor motorLF;
    const Motor motorLB;
    const Motor motorRF;
    const Motor motorRB;

};


RobotController::RobotController(const Motor motorLF, 
    const Motor motorLB, const Motor motorRF, 
    const Motor motorRB) : motorLF(motorLF), motorLB(motorLB),
    motorRF(motorRF), motorRB(motorRB) {

}


void RobotController::parseNewCommand(uint8_t commandArray[5]) {
    this->moveWithCommandsValue(commandArray);
}


void RobotController::moveWithCommandsValue(uint8_t commandArray[5]) {
    int magnitud, angle;
    fromRectangularOfControllerToPolar(commandArray[1], commandArray[0], 
        magnitud, angle);
    
    if (magnitud >= 25) {
        // Preferencia a movernos con joystick 1

        if (angle >= 45 and angle <= 135) {
            motorLF.forward(magnitud);
            motorLB.forward(magnitud);
            motorRF.forward(magnitud);
            motorRB.forward(magnitud);
        } else if (angle >= 225 and angle <= 315) {
            motorLF.backward(magnitud);
            motorLB.backward(magnitud);
            motorRF.backward(magnitud);
            motorRB.backward(magnitud);
        } else if (angle > 135 and angle < 225) {
            motorLF.backward(magnitud);
            motorLB.forward(magnitud);
            motorRF.forward(magnitud);
            motorRB.backward(magnitud);
        } else {
            motorLF.forward(magnitud);
            motorLB.backward(magnitud);
            motorRF.backward(magnitud);
            motorRB.forward(magnitud);
        }

    } else {
        // The Joystick 2
        fromRectangularOfControllerToPolar(commandArray[3], 
            commandArray[2], magnitud, angle);

        if (magnitud >= 25) {
            if (angle > 135 and angle < 225) {
                motorLF.backward(magnitud);
                motorLB.backward(magnitud);
                motorRF.forward(magnitud);
                motorRB.forward(magnitud);
            } else if (angle < 45 or angle > 315) {
                motorLF.forward(magnitud);
                motorLB.forward(magnitud);
                motorRF.backward(magnitud);
                motorRB.backward(magnitud);
            }

        } else {
            motorLF.stop();
            motorLB.stop();
            motorRF.stop();
            motorRB.stop();
        }

    }

}


int RobotController::fromPiMinusPiPlusTo360Angle(double angle) {
    int degreeValue = (int) round((angle * 180.0) / M_PI);

    if (degreeValue < 0) {
        return 360 + degreeValue;
    } else {
        return degreeValue;
    }
}


void RobotController::fromRectangularOfControllerToPolar(
    int xComponent, int yComponent, int &magnitud, 
    int &angle) {

    magnitud = sqrt(pow(xComponent - HALF_VALUE_JOYSTICK, 2)  + 
        pow(yComponent - HALF_VALUE_JOYSTICK, 2));
        
    double angleDouble = atan2(xComponent - HALF_VALUE_JOYSTICK, 
        yComponent - HALF_VALUE_JOYSTICK);
    angle = this->fromPiMinusPiPlusTo360Angle(angleDouble);
}


#endif
