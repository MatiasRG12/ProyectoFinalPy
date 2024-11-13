import os
import time
from Model  import ExecutionResults
from Utils import Constants
from Utils  import LoadMatrix
from AlgoritmosImpl import MatrixMultiplicationContext
from Utils import Plot

execution_times = {}
results = []

for algorithm in Constants.ALGORITHMS:
    for size in Constants.SIZES:
        log_file_path_a = os.path.join("Matrices", f"MatrixA_{size}x{size}.txt")
        log_file_path_b = os.path.join("Matrices", f"MatrixB_{size}x{size}.txt")

        # Cargar las matrices desde los archivos
        matrix_a = LoadMatrix(log_file_path_a)
        matrix_b = LoadMatrix(log_file_path_b)

        # Ejecutar el algoritmo de multiplicación
        context = MatrixMultiplicationContext(algorithm)
        start_time = time.time()
        result = context.execute(matrix_a, matrix_b)
        execution_times[f"{size}x{size}"] = (time.time() - start_time) * 1000  # Tiempo en ms

    results.append(ExecutionResults(algorithm, execution_times.copy()))
    execution_times.clear()

# Graficar los tiempos de ejecución
Plot.plot_execution_times(results)