# Kinetic Wall Clock

Es un proyecto IOT el cual es un reloj hecho de relojes.

Inicialmente es un proyecto con 24 relojes (3 filas, 8 columnas)

El proyecto consta principalmente de dos componentes, una Raspberry PI (master) que se encargara de calcular segun el esquema en que se encuentre, que posicion debe tomar cada reloj y enviar estos comandos a cada uno de los ESP32 (slave) que ejecutaran los movimientos. El master definira la posicion que debe ir cada manecilla y la velocidad de su movimiento.

## Componentes principales

### Master

- Rasperry PI 4B -> Es el cerebro, encargado de administrar los estados del reloj, calcular animaciones, enviar los comandos a los slaves.

- RS485 -> Comunicacion serial por protocolo RS485, es un estandar de comunicacion muy utilizado en aplicaciones y control de datos. Su principal ventaja es que permite incluir varios dispositivos RS485 en el mismo BUS, lo que hace posible que varios nodos se conecten entre si. Es utilizado por KWC para enviar los comandos principales.

### Slave

- ESP32 -> Es el encargado de recibir comandos y controlar los principales componentes de cada reloj, en lo fisico el slave tiene el control de 4 motores paso a paso, 4 sensores hall, un DIP Switch para cambiar el reloj que debe controlar.

## Aspectos Tecnicos

El reloj tiene la capacidad de determinar la posicion de cada manecilla mediante un sensor hall, ubicado en el punto 12 de un reloj para reiniciar en caso de cualquier incidente, por ejemplo un apagado, encendido, o una nueva accion solicitada.

### Comandos basicos

- HOME[I][R][M][S] -> Comando que solicita a cada reloj que ubique una manecilla en la posicion cero. 
    Donde: 
        [I]: Slave a que se le comunica, van desde el 0 al 11.
        [R]: Reloj, cada slave controla dos relojes, 0 y 1.
        [M]: Manecilla, cada reloj controla dos manecillas, 0 y 1.
        [S]: Velocidad de movimiento. <!-- TODO: Pendiente de valores maximos y minimos. -1 velocidad por defecto. -->
- HOME_ALL: Ejecuta el programa de Home por defecto, este aplica para todos los slaves.
- MOVE[I][R][M][A][S] -> Comando que solicita el movimiento del los punteros a un radio especifico con una velocidad especifica.
    Donde: 
        [I]: Slave a que se le comunica, van desde el 0 al 11.
        [R]: Reloj, cada slave controla dos relojes, 0 y 1.
        [M]: Manecilla, cada reloj controla dos manecillas, 0 y 1.
        [A]: Angulo de destino.
        [S]: Velocidad de movimiento. <!-- TODO: Pendiente de valores maximos y minimos. -1 velocidad por defecto. -->

