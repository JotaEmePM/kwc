# Configuracion Raspberry PI
RS485_CONTROL = 18


HOME_DEFAULT_SPEED = 100

SLAVE_1 = {
    'character': 1,
    'clock_1': (0, 0),
    'clock_2': (0, 1),
    'direction': 'DOWN',
    'slave': 1
}

SLAVE_2 = {
    'character': 1,
    'clock_1': (0, 2),
    'clock_2': (1, 2),
    'direction': 'RIGHT',
    'slave': 2
}

SLAVE_3 = {
    'character': 1,
    'clock_1': (1, 1),
    'clock_2': (1, 0),
    'direction': 'UP',
    'slave': 1
}

SLAVE_4 = {
    'character': 2,
    'clock_1': (2, 0),
    'clock_2': (2, 1),
    'direction': 'DOWN',
    'slave': 4
}

SLAVE_5 = {
    'character': 2,
    'clock_1': (2, 2),
    'clock_2': (3, 2),
    'direction': 'RIGHT',
    'slave': 5
}

SLAVE_6 = {
    'character': 2,
    'clock_1': (3, 1),
    'clock_2': (3, 0),
    'direction': 'UP',
    'slave': 6
}

SLAVE_7 = {
    'character': 3,
    'clock_1': (4, 0),
    'clock_2': (4, 1),
    'direction': 'DOWN',
    'slave': 7
}

SLAVE_8 = {
    'character': 3,
    'clock_1': (4, 2),
    'clock_2': (5, 2),
    'direction': 'RIGHT',
    'slave': 8
}

SLAVE_9 = {
    'character': 3,
    'clock_1': (5, 1),
    'clock_2': (5, 0),
    'direction': 'UP',
    'slave': 9
}

SLAVE_10 = {
    'character': 4,
    'clock_1': (6, 0),
    'clock_2': (6, 1),
    'direction': 'DOWN',
    'slave': 10
}

SLAVE_11 = {
    'character': 4,
    'clock_1': (6, 2),
    'clock_2': (7, 2),
    'direction': 'RIGHT',
    'slave': 11
}

SLAVE_12 = {
    'character': 4,
    'clock_1': (7, 1),
    'clock_2': (7, 0),
    'direction': 'UP',
    'slave': 12
}

ALL_SLAVES = [
    SLAVE_1,
    SLAVE_2,
    SLAVE_3,
    SLAVE_4,
    SLAVE_5,
    SLAVE_6,
    SLAVE_7,
    SLAVE_8,
    SLAVE_9,
    SLAVE_10,
    SLAVE_11,
    SLAVE_12
]
