# Preguntas

- Factibilidad del proyecto
    - Esquema Maestro esclavo, 12 esclavos, dos motores cada esclavo, dos sensores hall digital.

- Voltaje:
    - Puedo usar una fuente de 5v 20a, como calcular el amperaje completo, me ofrecen un 5v50a.
    - El esclavo puede tener solo una entrada de 5v y reducir en ciertas partes para su uso en 3.3v
    - Esta sparación como manejarla, IA me recomienda MP2307 SMD, o puedo hacerlo sin requerir un componente extra.
    - Como conectar todos los esclavos desde la Fuente de poder.
    - Como conectar la Raspberry PI
    
- Comunicacion RS485
    - Daisy Chain para comunicar
    - es solo necesario un RS485, no requiero comunicacion ida y vuelta.
    - IA sugiere cable par trenzado entre maestro esclavo
    - Como conectar desde el 485 a los esclavos? Bornera KF350-3.5 2p
    - EL primer y ultimo esclavo requiere una Resistencia de 120 ohm, como realizar en el esquematico un jumper para crear solo un tipo de esclavo

- DIP Switch 4 botones
    - Uso para establecer el ID del esclavo
    - Puedo usar el valor binario?

- ESP32
    - Puedo usar un SMD? de solo el microcontrolador?

- ULN2003
    - Cual es la diferencia entre ULN2003 y ULN2003a?
    - El Pin puede usar desde el PCB los 5v?

- Hall Effect
    - Requiero 4 sensores?



Hola a todos! Ando en búsqueda de asesoría técnica sobre la construcción de un proyecto de hobby de un Kinetic Wall Clock. Tengo algunas nociones técnicas que me gustaría resolver para desarrollar la PCB. La idea es que fuese mediante video llamada, obviamente pagadas.





- 