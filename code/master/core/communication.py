import serial
import time

# Provide a lightweight GPIO stub for non-RPi environments (e.g., development on Windows).
try:
    import RPi.GPIO as GPIO
except Exception:
    class _GPIOStub:
        BCM = None
        OUT = None
        HIGH = 1
        LOW = 0
        def setmode(self, *a, **k): pass
        def setup(self, *a, **k): pass
        def output(self, *a, **k): pass
        def cleanup(self): pass
    GPIO = _GPIOStub()

from core.constants import RS485_CONTROL


class Communication:
    """Singleton RS485 communication helper.

    Usage:
        comm = Communication()
        comm.send_message('CMD', 'ARG1', 123)  # builds 'CMD|ARG1|123\n' and sends it
        response = comm.receive_data()
        comm.close()
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, port='/dev/serial0', baudrate=9600, timeout=1):
        if self._initialized:
            return
        self._initialized = True

        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RS485_CONTROL, GPIO.OUT)

        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )

    def build_message(self, *parts, sep='|'):
        """Compose a message string from parts and append newline."""
        return sep.join(map(str, parts)) + '\n'

    def send_data(self, data: str):
        """Send a complete string over RS485 (handles DE/RE pin toggling)."""
        if self.ser is None:
            raise RuntimeError('Serial port not initialized')

        GPIO.output(RS485_CONTROL, GPIO.HIGH)  # enable transmission
        time.sleep(0.01)
        try:
            self.ser.write(data.encode('utf-8'))
            self.ser.flush()
        finally:
            time.sleep(0.01)
            GPIO.output(RS485_CONTROL, GPIO.LOW)  # back to receive

    def send_message(self, *parts, sep='|'):
        msg = self.build_message(*parts, sep=sep)
        self.send_data(msg)
        return msg

    def receive_data(self):
        """Read a line from serial and return it as a stripped string."""
        if self.ser is None:
            return ''

        GPIO.output(RS485_CONTROL, GPIO.LOW)
        try:
            line = self.ser.readline()
            if not line:
                return ''
            return line.decode('utf-8', errors='ignore').strip()
        except Exception:
            return ''

    def close(self):
        if self.ser is not None and getattr(self.ser, 'is_open', False):
            try:
                self.ser.close()
            except Exception:
                pass
        try:
            GPIO.cleanup()
        except Exception:
            pass
