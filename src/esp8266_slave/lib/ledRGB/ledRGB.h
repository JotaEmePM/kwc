#ifndef ledRGB_h

#define ledRGB_h

#include <Arduino.h>

class ledRGB
{

public:
    ledRGB(byte red, byte green, byte blue);
    void showRandomColors();
    void showRed();

private:
    byte _red;
    byte _green;
    byte _blue;
    void initializeRandomNumbers();
}

#endif
