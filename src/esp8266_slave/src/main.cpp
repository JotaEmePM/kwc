#include <Arduino.h>


void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Configura el pin como salida
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Enciende el LED (en ESP8266, HIGH apaga, LOW enciende)
  delay(1000);                     // Espera 1 segundo
  digitalWrite(LED_BUILTIN, LOW);  // Apaga el LED (en ESP8266, LOW enciende, HIGH apaga)
  delay(1000);                     // Espera 1 segundo
}