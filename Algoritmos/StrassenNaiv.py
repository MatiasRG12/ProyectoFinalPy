import math
from Algoritmos.IMatrixMultiplication import IMatrixMultiplication

class StrassenNaiv(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param

    def max(self, N, P):
        return P if N < P else N

    def add(self, A, B, C, size):
        for i in range(size):
            for j in range(size):
                C[i][j] = A[i][j] + B[i][j]

    def subtract(self, A, B, C, size):
        for i in range(size):
            for j in range(size):
                C[i][j] = A[i][j] - B[i][j]

    def algStrassenNaiv(self, matrizA, matrizB, matrizRes, N, P, M):
        maxSize = max(N, P)
        if maxSize < 16:
            maxSize = 16
        k = int(math.log(maxSize, 2)) - 4
        m = int(maxSize * (2 ** -k)) + 1
        newSize = m * (2 ** k)
    
        newA = [[0.0] * newSize for _ in range(newSize)]
        newB = [[0.0] * newSize for _ in range(newSize)]
        auxResult = [[0.0] * newSize for _ in range(newSize)]
    
        for i in range(newSize):
            for j in range(newSize):
                newA[i][j] = 0.0
                newB[i][j] = 0.0
            
        for i in range(N):
            for j in range(P):
                newA[i][j] = matrizA[i][j]
            
        for i in range(N):
            for j in range(M):
                newB[i][j] = matrizB[i][j]
            
        self.strassenNaivStep(newA, newB, auxResult, newSize, m)
    
        for i in range(N):
            for j in range(M):
                matrizRes[i][j] = auxResult[i][j]
    
    def strassenNaivStep(self, matrizA, matrizB, matrizRes, N, m):
        if N % 2 == 0 and N > m:
            newSize = N // 2

            # Initialize submatrices
            varA11 = [[0] * newSize for _ in range(newSize)]
            varA12 = [[0] * newSize for _ in range(newSize)]
            varA21 = [[0] * newSize for _ in range(newSize)]
            varA22 = [[0] * newSize for _ in range(newSize)]
            varB11 = [[0] * newSize for _ in range(newSize)]
            varB12 = [[0] * newSize for _ in range(newSize)]
            varB21 = [[0] * newSize for _ in range(newSize)]
            varB22 = [[0] * newSize for _ in range(newSize)]

            resultadoPart11 = [[0] * newSize for _ in range(newSize)]
            resultadoPart12 = [[0] * newSize for _ in range(newSize)]
            resultadoPart21 = [[0] * newSize for _ in range(newSize)]
            resultadoPart22 = [[0] * newSize for _ in range(newSize)]

            helper1 = [[0] * newSize for _ in range(newSize)]
            helper2 = [[0] * newSize for _ in range(newSize)]

            aux1 = [[0] * newSize for _ in range(newSize)]
            aux2 = [[0] * newSize for _ in range(newSize)]
            aux3 = [[0] * newSize for _ in range(newSize)]
            aux4 = [[0] * newSize for _ in range(newSize)]
            aux5 = [[0] * newSize for _ in range(newSize)]
            aux6 = [[0] * newSize for _ in range(newSize)]
            aux7 = [[0] * newSize for _ in range(newSize)]

            # Fill in the submatrices
            for i in range(newSize):
                for j in range(newSize):
                    varA11[i][j] = matrizA[i][j]
                    varA12[i][j] = matrizA[i][j + newSize]
                    varA21[i][j] = matrizA[i + newSize][j]
                    varA22[i][j] = matrizA[i + newSize][j + newSize]
                    varB11[i][j] = matrizB[i][j]
                    varB12[i][j] = matrizB[i][j + newSize]
                    varB21[i][j] = matrizB[i + newSize][j]
                    varB22[i][j] = matrizB[i + newSize][j + newSize]

            self.add(varA11, varA22, helper1, newSize)
            self.add(varB11, varB22, helper2, newSize)
            self.strassenNaivStep(helper1, helper2, aux1, newSize, m)

            self.add(varA21, varA22, helper1, newSize)
            self.strassenNaivStep(helper1, varB11, aux2, newSize, m)

            self.subtract(varB12, varB22, helper1, newSize)
            self.strassenNaivStep(varA11, helper1, aux3, newSize, m)

            self.subtract(varB21, varB11, helper1, newSize)
            self.strassenNaivStep(varA22, helper1, aux4, newSize, m)

            self.add(varA11, varA12, helper1, newSize)
            self.strassenNaivStep(helper1, varB22, aux5, newSize, m)

            self.subtract(varA21, varA11, helper1, newSize)
            self.add(varB11, varB12, helper2, newSize)
            self.strassenNaivStep(helper1, helper2, aux6, newSize, m)

            self.subtract(varA12, varA22, helper1, newSize)
            self.add(varB21, varB22, helper2, newSize)
            self.strassenNaivStep(helper1, helper2, aux7, newSize, m)

            # Calculate final parts of the result matrix
            self.add(aux1, aux4, resultadoPart11, newSize)
            self.subtract(resultadoPart11, aux5, resultadoPart11, newSize)
            self.add(resultadoPart11, aux7, resultadoPart11, newSize)

            self.add(aux3, aux5, resultadoPart12, newSize)
            self.add(aux2, aux4, resultadoPart21, newSize)

            self.add(aux1, aux3, resultadoPart22, newSize)
            self.subtract(resultadoPart22, aux2, resultadoPart22, newSize)
            self.add(resultadoPart22, aux6, resultadoPart22, newSize)

            # Store results back to matrizRes
            for i in range(newSize):
                for j in range(newSize):
                    matrizRes[i][j] = resultadoPart11[i][j]
                    matrizRes[i][j + newSize] = resultadoPart12[i][j]
                    matrizRes[i + newSize][j] = resultadoPart21[i][j]
                    matrizRes[i + newSize][j + newSize] = resultadoPart22[i][j]
        else:
            # Standard naive algorithm for small matrices
            self.algoritmoNaivStandard(matrizA, matrizB, matrizRes, N, N, N)

    def algoritmoNaivStandard(self, matrizA, matrizB, matrizRes, N, P, M):
        for i in range(N):
            for j in range(M):
                aux = 0.0
                for k in range(P):
                    aux += matrizA[i][k] * matrizB[k][j]
                matrizRes[i][j] = aux

    def multiply(self, matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])
        matrizRes = [[0.0 for _ in range(M)] for _ in range(N)]
        self.algStrassenNaiv(matrizA, matrizB, matrizRes, N, P, M)
        return matrizRes

