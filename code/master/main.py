import os
# from core.constants import HOME_SPEED
from datetime import datetime

from core.communication import Communication
from core.config import Config

name = 'Kinetic Wall Clock'
in_movement = False

message = ''
firs_animation = True

comm = None  # Acceso a protocolo RS485
conf = None  # Acceso a archivos de configuracion


def init_system():
    global comm, conf

    # Init config data
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    conf = Config(config_path)

    try:
        # Check if communication between RS485 is enabled.
        if conf.config().getboolean('app', 'send_to_rs485'):
            print('Initializing RS485 Communication...')
            comm = Communication()
        else:
            print('RS485 Communication disabled in config.')
    except Exception as e:
        print(f"Warning: Could not initialize Communication: {e}")


def update():
    config = conf.config()
    # print(config['app']['send_to_rs485'])
    if can_send():

        comm.send_message('PING')
        response = comm.receive_data()
        print(f'Response: {response}')
        comm.close()


def can_send():
    result = True
    if not comm:
        result = False

    return result


if __name__ == '__main__':
    init_system()
    while True:
        update()
