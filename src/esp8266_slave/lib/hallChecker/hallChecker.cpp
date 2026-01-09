#include <Arduino.h>
#include hallChecker.h

int hall_state = 0;

hallChecker::hallChecker(byte signal_pin)
{
    _signal_pin = signal_pin;

    pinMode(_signal_pin, INPUT);
}

bool hallChecker::isHome()
{
    hall_state = digitalRead(_signal_pin);

    if (hall_state == LOW)
    {
        return true;
    }

    return false;
}