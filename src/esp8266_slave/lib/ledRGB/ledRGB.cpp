#include <Arduino.h>
#include ledRGB.h

ledRGB::ledRGB(byte red, byte green, byte blue)
{
    _red = red;
    _green = green;
    _blue = blue;

    pinMode(_red, OUTPUT);
    pinMode(_green, OUTPUT);
    pinMode(_blue, OUTPUT);

    digitalWrite(_red, false);
    digitalWrite(_green, false);
    digitalWrite(_blue, false);
}

void ledRGB::showRandomColors()
{
    int redValue = random(0, 2);
    int greenValue = random(0, 2);
    int blueValue = random(0, 2);

    digitalWrite(_red, redValue);
    digitalWrite(_green, greenValue);
    digitalWrite(_blue, blueValue);
}

void ledRGB::showRED()
{
    digitalWrite(_red, true);
    digitalWrite(_green, false);
    digitalWrite(_blue, false);
}

void ledRGB::initializeRandomNumbers()
{
    randomSeed(analogRead(A0));
}