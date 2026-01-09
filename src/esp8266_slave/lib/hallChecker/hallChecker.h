#ifndef hallChecker_H

#define hallChecker_H

#include <Arduino.h>

class hallChecker
{

public:
    hallChecker(byte signal_pin);
    bool isHome();

private:
    byte _signal_pin;
}

#endif