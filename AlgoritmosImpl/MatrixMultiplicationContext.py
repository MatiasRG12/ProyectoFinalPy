import time
from Algoritmos import StrassenNaiv, WinogradOriginal #Terminar de importar las clases

class MatrixMultiplicationContext:
    def __init__(self, nombre_algoritmo):
        # Diccionario de algoritmos
        self._diccionario = {
            "StrassenNaiv": StrassenNaiv(),
            "WinogradOriginal": WinogradOriginal(),
            # Agrega aquí el resto de implementaciones...
        }
        self._algorithm = self._diccionario[nombre_algoritmo]

    def execute(self, matrixA, matrixB):
        start_time = time.time()
        
        # Llama a la implementación del método multiply
        result = self._algorithm.multiply(matrixA, matrixB)
        
        elapsed_time = (time.time() - start_time) * 1000  # Tiempo en milisegundos
        
        # Opcional: imprimir el resultado si la matriz es pequeña
        if len(matrixA) == 4:
            self._print_mat(result)
            print("------------------------------------------------")

        # Registrar el tiempo de ejecución (puedes implementar un logger similar)
        print(f"Execution Time ({self._algorithm.__class__.__name__}): {elapsed_time:.2f} ms")
        
        return result, elapsed_time

    def _print_mat(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))
        print()