from Algoritmos.IMatrixMultiplication import IMatrixMultiplication

class NaivOnArrays(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param

    def algNaivOnArray(self, matrizA, matrizB, N, P, M):
        matrizRes = [[0.0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                for k in range(P):
                    matrizRes[i][j] += matrizA[i][k] * matrizB[k][j]
        return matrizRes

    def multiply(self, matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])
        return self.algNaivOnArray(matrizA, matrizB, N, P, M)