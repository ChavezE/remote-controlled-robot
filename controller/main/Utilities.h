#ifndef UTILITIES_H
#define UTILITIES_H

uint8_t addBoolValueInInt(const bool value, const int placeOfTheBit, const uint8_t intWhereInsert) {
    // Cast the boolean value to int
    uint8_t integerToAdd = (uint8_t) value;

    // Move n places the bit inside the number
    integerToAdd = integerToAdd<<placeOfTheBit;

    // Insert the value in the number
    return intWhereInsert | integerToAdd;
}

#endif