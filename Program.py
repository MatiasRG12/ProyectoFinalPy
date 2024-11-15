import os
import time
from Model.ExecutionResults import ExecutionResult
from Utils.Constants import Constants
from Utils.LoadMatrix  import LoadMatrix
from AlgoritmosImpl.MatrixMultiplicationContext import MatrixMultiplicationContext
from Utils.Plot import Plot

execution_times = {}
results = []

for algorithm in Constants.ALGORITHMS:
    for size in Constants.SIZES:
        log_file_path_a = os.path.join("Matrices", f"MatrixA_{size}x{size}.txt")
        log_file_path_b = os.path.join("Matrices", f"MatrixB_{size}x{size}.txt")

        # Cargar las matrices desde los archivos
        matrix_a = LoadMatrix.load_matrix_from_file(log_file_path_a)
        matrix_b = LoadMatrix.load_matrix_from_file(log_file_path_b)

        # Ejecutar el algoritmo de multiplicación
        context = MatrixMultiplicationContext(algorithm)
        start_time = time.time()
        result = context.execute(matrix_a, matrix_b)
        execution_times[f"{size}x{size}"] = (time.time() - start_time) * 1000  # Tiempo en ms

    results.append(ExecutionResult(algorithm, execution_times.copy()))
    execution_times.clear()

# Graficar los tiempos de ejecución
Plot.plot_execution_times(results)