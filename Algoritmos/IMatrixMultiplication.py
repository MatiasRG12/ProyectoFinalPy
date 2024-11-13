from abc import ABC, abstractmethod

class IMatrixMultiplication(ABC):

    @abstractmethod
    def multiply(self, matrizA, matrizB):
        pass