#include <Arduino.h>
#include "ledRGB.h"

int miEntero = 0;
ledRGB miLed(2, 3, 4);

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  miLed.showRandomColors();
  delay(1000);
}