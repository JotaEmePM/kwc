import configparser


class Config:
    """
    Acceso a datos de configuracion
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, path_config_file):
        if self._initialized:
            return
        self._initialized = True

        self._parser = configparser.ConfigParser()

        self._path_config_file = path_config_file
        self.setup()

    def setup(self):
        self._parser.read(self._path_config_file)

    def config(self):
        return self._parser


# # Leer el archivo
# config.read('config.ini')

# # Acceder a los valores
# db_host = config['database']['host']
# debug_mode = config.getboolean('app', 'debug') # Para booleanos

# print(f"Host de la BD: {db_host}")
# print(f"Modo Debug: {debug_mode}")
