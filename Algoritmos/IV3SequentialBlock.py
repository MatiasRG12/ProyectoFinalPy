from Algoritmos.IMatrixMultiplication import IMatrixMultiplication

class IV3SequentialBlock(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param


    def v3SequentialBlock(self, matrizA, matrizB, size1, size2):
        matrizRes = [[0.0 for _ in range(size1)] for _ in range(size1)]
        for i1 in range(0, size1, size2):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizRes[i][j] += matrizA[i][k] * matrizB[k][j]
        return matrizRes

    def multiply(self,matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB[0])
        return self.v3SequentialBlock(matrizA, matrizB, N, P)