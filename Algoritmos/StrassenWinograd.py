import math
from Algoritmos.IMatrixMultiplication import IMatrixMultiplication

class StrassenWinograd(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param

    def max(self, a, b):
        return a if a > b else b
    

    def add(self, A, B, C, size):
        for i in range(size):
            for j in range(size):
                C[i][j] = A[i][j] + B[i][j]


    def subtract(self, A, B, C, size):
        for i in range(size):
            for j in range(size):
                C[i][j] = A[i][j] - B[i][j]


    def standard_multiply(self, A, B, C, N, P, M):
        for i in range(N):
            for j in range(M):
                C[i][j] = 0
                for k in range(P):
                    C[i][j] += A[i][k] * B[k][j]


    def strassen_winograd_step(self, A, B, C, size, min_size):
        if size <= min_size:
            self.standard_multiply(A, B, C, size, size, size)
            return

        new_size = size // 2
        # Creating submatrices
        A11 = [[0] * new_size for _ in range(new_size)]
        A12 = [[0] * new_size for _ in range(new_size)]
        A21 = [[0] * new_size for _ in range(new_size)]
        A22 = [[0] * new_size for _ in range(new_size)]
        B11 = [[0] * new_size for _ in range(new_size)]
        B12 = [[0] * new_size for _ in range(new_size)]
        B21 = [[0] * new_size for _ in range(new_size)]
        B22 = [[0] * new_size for _ in range(new_size)]
        C11 = [[0] * new_size for _ in range(new_size)]
        C12 = [[0] * new_size for _ in range(new_size)]
        C21 = [[0] * new_size for _ in range(new_size)]
        C22 = [[0] * new_size for _ in range(new_size)]
        tempA = [[0] * new_size for _ in range(new_size)]
        tempB = [[0] * new_size for _ in range(new_size)]

        # Dividing matrices into quarters
        for i in range(new_size):
            for j in range(new_size):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j + new_size]
                A21[i][j] = A[i + new_size][j]
                A22[i][j] = A[i + new_size][j + new_size]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j + new_size]
                B21[i][j] = B[i + new_size][j]
                B22[i][j] = B[i + new_size][j + new_size]

        # Strassen's recursive steps
        self.add(A11, A22, tempA, new_size)
        self.add(B11, B22, tempB, new_size)
        self.strassen_winograd_step(tempA, tempB, C11, new_size, min_size)  # P1

        self.add(A21, A22, tempA, new_size)
        self.strassen_winograd_step(tempA, B11, C21, new_size, min_size)  # P2

        self.subtract(B12, B22, tempB, new_size)
        self.strassen_winograd_step(A11, tempB, C12, new_size, min_size)  # P3

        self.subtract(B21, B11, tempB, new_size)
        self.strassen_winograd_step(A22, tempB, C22, new_size, min_size)  # P4

        self.add(A11, A12, tempA, new_size)
        self.strassen_winograd_step(tempA, B22, tempA, new_size, min_size)  # P5
        self.add(tempA, C11, C11, new_size)
        self.subtract(C12, tempA, C12, new_size)

        self.subtract(A21, A11, tempA, new_size)
        self.add(B11, B12, tempB, new_size)
        self.strassen_winograd_step(tempA, tempB, tempA, new_size, min_size)  # P6
        self.add(C22, tempA, C22, new_size)

        self.subtract(A12, A22, tempA, new_size)
        self.add(B21, B22, tempB, new_size)
        self.strassen_winograd_step(tempA, tempB, tempA, new_size, min_size)  # P7
        self.subtract(C21, tempA, C21, new_size)

        # Combining the results into the result matrix C
        for i in range(new_size):
            for j in range(new_size):
                C[i][j] = C11[i][j]
                C[i][j + new_size] = C12[i][j]
                C[i + new_size][j] = C21[i][j]
                C[i + new_size][j + new_size] = C22[i][j]


    def algStrassenWinograd(self, A, B, C, N, P, M):
        maxSize = max(N, P)
        maxSize = max(maxSize, M)
        if maxSize < 16:
            maxSize = 16
        valorK = int(math.log(maxSize, 2) - 4)
        valorM = int(maxSize * pow(2, -valorK) + 1)
        newSize = valorM * int(pow(2, valorK))

        newA = [[0] * newSize for _ in range(newSize)]
        newB = [[0] * newSize for _ in range(newSize)]
        auxResultado = [[0] * newSize for _ in range(newSize)]

        for i in range(newSize):
            for j in range(newSize):
                newA[i][j] = 0.0 if i >= N or j >= P else A[i][j]
                newB[i][j] = 0.0 if i >= P or j >= M else B[i][j]

        self.strassen_winograd_step(newA, newB, auxResultado, newSize, 16)

        for i in range(N):
            for j in range(M):
                C[i][j] = auxResultado[i][j]


    def multiply(self, A, B):
        N = len(A)
        P = len(B)
        M = len(B[0])
        C = [[0] * M for _ in range(N)]
        self.algStrassenWinograd(A, B, C, N, P, M)
        return C
