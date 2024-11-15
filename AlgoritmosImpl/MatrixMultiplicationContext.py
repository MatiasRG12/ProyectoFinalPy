import time
from Algoritmos.StrassenNaiv import StrassenNaiv
from Algoritmos.WinogradOriginal import WinogradOriginal
from Algoritmos.IV3SequentialBlock import IV3SequentialBlock
from Algoritmos.NaivLoopUnrollingFour import NaivLoopUnrollingFour
from Algoritmos.NaivLoopUnrollingTwo import NaivLoopUnrollingTwo
from Algoritmos.NaivOnArrays import NaivOnArrays
from Algoritmos.V3SequentialBlock import V3SequentialBlock
from Algoritmos.V4ParallelBlock import V4ParallelBlock
from Algoritmos.StrassenWinograd import StrassenWinograd
from Algoritmos.WinogradScaled import WinogradScaled
from Algoritmos.IMatrixMultiplication import IMatrixMultiplication


class MatrixMultiplicationContext:
    def __init__(self, nombre_algoritmo):
        # Diccionario de algoritmos
        self._diccionario = {
            "StrassenNaiv": StrassenNaiv(),
            "WinogradOriginal": WinogradOriginal(),
            "IV3SequentialBlock": IV3SequentialBlock(),
            "NaivLoopUnrollingFour": NaivLoopUnrollingFour(),
            "NaivLoopUnrollingTwo": NaivLoopUnrollingTwo(),
            "NaivOnArrays": NaivOnArrays(),
            "V3SequentialBlock": V3SequentialBlock(),
            "V4ParallelBlock": V4ParallelBlock(),
            "StrassenWinograd": StrassenWinograd(),
            "WinogradScaled": WinogradScaled()
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
