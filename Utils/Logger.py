import os
from datetime import datetime

class Logger:
    # Define la ruta del archivo de log
    LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "Logs", "ExecutionTimes.log")

    @staticmethod
    def log_execution_time(algorithm_name, time, rows_a, cols_a, rows_b, cols_b):
        # Asegúrate de que el directorio de logs exista
        os.makedirs(os.path.dirname(Logger.LOG_FILE_PATH), exist_ok=True)

        with open(Logger.LOG_FILE_PATH, 'a') as file:
            file.write(f"{datetime.now()} - Algorithm: {algorithm_name}, Time: {time} ms, "
                       f"Matrix A: {rows_a}x{cols_a}, Matrix B: {rows_b}x{cols_b}\n")
