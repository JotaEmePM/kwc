# Kinetic Wall Clock

An IoT project that implements an analog clock constructed from multiple individual clocks.

Initially comprised of 24 clocks organized in a matrix of 3 rows and 8 columns.

The project consists of two main components: a Raspberry Pi (master) responsible for calculating, according to the active visualization scheme, the position each hand should adopt and sending the corresponding commands to each ESP32 (slave) to execute the movements. The master determines both the target position and movement speed of each hand.

## Main Components

### Master

- Raspberry Pi 4B → Acts as the system's brain, responsible for managing clock states, calculating animations, and sending commands to the slaves.

- RS485 → Serial communication via RS485 protocol, a standard widely used in automation and data control applications. Its main advantage lies in allowing multiple RS485 devices to be connected on the same bus, facilitating communication between multiple nodes. KWC uses this protocol for transmitting main commands.

### Slave

- ESP32 → Responsible for receiving commands and controlling the main components of each clock. At the physical level, each slave manages 4 stepper motors, 4 Hall sensors, and a DIP switch to select the clock it should control.

## Technical Aspects

The clock has the ability to determine the position of each hand using a Hall sensor located at the 12 o'clock position, which allows resetting its position in case of any incident, such as power failures or unexpected actions.

### Basic Commands

- HOME(I,R,M,S) → Command that requests positioning a hand at the zero position. 
    Where: 
        I: Slave identifier, range from 0 to 11.
        R: Clock identifier, each slave controls two clocks: 0 and 1.
        M: Hand identifier, each clock controls two hands: 0 and 1.
        S: Movement speed. <!-- TODO: Pending definition of maximum and minimum values. -1 for default speed. -->
- HOME_ALL: Executes the default initialization program applicable to all slaves.
- MOVE(I,R,M,A,S) → Command that requests moving the hands to a specific angle at a determined speed.
    Where: 
        I: Slave identifier, range from 0 to 11.
        R: Clock identifier, each slave controls two clocks: 0 and 1.
        M: Hand identifier, each clock controls two hands: 0 and 1.
        A: Destination angle.
        S: Movement speed. <!-- TODO: Pending definition of maximum and minimum values. -1 for default speed. -->

