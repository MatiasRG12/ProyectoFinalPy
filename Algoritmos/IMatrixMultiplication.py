from abc import ABC, abstractmethod

class IMatrixMultiplication(ABC):

    @abstractmethod
    def Multiply(self, matrizA, matrizB):
        pass