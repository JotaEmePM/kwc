# Reloj de Pared Cinético

[English version](README.md)

Proyecto IoT que implementa un reloj analógico construido a partir de múltiples relojes individuales.

Inicialmente consta de 24 relojes organizados en una matriz de 3 filas y 8 columnas.

El proyecto se compone de dos elementos principales: una Raspberry Pi (maestro) encargada de calcular, según el esquema de visualización activo, la posición que debe adoptar cada manecilla y enviar los comandos correspondientes a cada uno de los ESP32 (esclavos) para ejecutar los movimientos. El maestro determina tanto la posición destino como la velocidad de movimiento de cada manecilla.

## Componentes Principales

### Maestro

- Raspberry Pi 4B → Actúa como el cerebro del sistema, responsable de gestionar los estados del reloj, calcular las animaciones y enviar los comandos a los esclavos.

- RS485 → Comunicación serial mediante protocolo RS485, estándar ampliamente utilizado en aplicaciones de automatización y control de datos. Su principal ventaja radica en permitir la conexión de múltiples dispositivos RS485 en el mismo bus, facilitando la comunicación entre varios nodos. KWC utiliza este protocolo para la transmisión de comandos principales.

### Esclavo

- ESP32 → Responsable de recibir los comandos y controlar los componentes principales de cada reloj. A nivel físico, cada esclavo gestiona 4 motores paso a paso, 4 sensores Hall y un interruptor DIP para seleccionar el reloj que debe controlar.

## Aspectos Técnicos

El reloj posee la capacidad de determinar la posición de cada manecilla mediante un sensor Hall ubicado en la posición de las 12 horas, lo que permite reiniciar su posición en caso de cualquier incidente, como apagones o acciones inesperadas.

### Comandos Básicos

- HOME(I,R,M,S) → Comando que solicita posicionar una manecilla en la posición cero. 
    Donde: 
        I: Identificador del esclavo, rango de 0 a 11.
        R: Identificador del reloj, cada esclavo controla dos relojes: 0 y 1.
        M: Identificador de la manecilla, cada reloj controla dos manecillas: 0 y 1.
        S: Velocidad de movimiento. <!-- TODO: Pendiente de definir valores máximos y mínimos. -1 para velocidad por defecto. -->
- HOME_ALL: Ejecuta el programa de inicialización por defecto aplicable a todos los esclavos.
- MOVE(I,R,M,A,S) → Comando que solicita mover las manecillas a un ángulo específico con una velocidad determinada.
    Donde: 
        I: Identificador del esclavo, rango de 0 a 11.
        R: Identificador del reloj, cada esclavo controla dos relojes: 0 y 1.
        M: Identificador de la manecilla, cada reloj controla dos manecillas: 0 y 1.
        A: Ángulo destino.
        S: Velocidad de movimiento. <!-- TODO: Pendiente de definir valores máximos y mínimos. -1 para velocidad por defecto. -->

