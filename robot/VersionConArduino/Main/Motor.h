#ifndef MOTOR_H
#define MOTOR_H

class Motor{
public:
    Motor(uint8_t pinFront, uint8_t pinBack);

    void forward(uint8_t velocity);
    void backward(uint8_t velocity);
    void stop();

private:
    const uint8_t pinFront;
    const uint8_t pinBack;

};


Motor::Motor(uint8_t pinFront, uint8_t pinBack) : 
    pinFront(pinFront), pinBack(pinBack) {
    pinMode(pinFront, OUTPUT);
    pinMode(pinBack, OUTPUT);
}

void Motor::forward(uint8_t velocity) {
    analogWrite(pinFront, velocity);
    analogWrite(pinBack, 0);
}

void Motor::backward(uint8_t velocity) {
    analogWrite(pinFront, 0);
    analogWrite(pinBack, velocity);
}

void Motor::stop() {
    analogWrite(pinFront, 0);
    analogWrite(pinBack, 0);
}


#endif