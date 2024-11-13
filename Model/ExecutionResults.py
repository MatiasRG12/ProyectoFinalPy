class ExecutionResult:
    def __init__(self, name, times=None):
        self._name = name
        self._times = times if times is not None else {}

    def add_time(self, key, value):
        #Agrega un tiempo al diccionario.
        self._times[key] = value

    def get_time(self, key):
        #Obtiene el tiempo asociado a una clave; si no existe, retorna 0.
        return self._times.get(key, 0)

    def get_name(self):
        #Retorna el nombre asociado al resultado.
        return self._name
