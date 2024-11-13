import math
import IMatrixMultiplication

class WinogradScaled(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param

    def multiply_with_scalar(self, matrix, scalar):
        n, m = len(matrix), len(matrix[0])
        result = [[matrix[i][j] * scalar for j in range(m)] for i in range(n)]
        return result

    def norm_inf(self, matrix):
        max_sum = float('-inf')
        for row in matrix:
            row_sum = sum(abs(x) for x in row)
            if row_sum > max_sum:
                max_sum = row_sum
        return max_sum

    def alg_winograd_original(self, A, B, N, P, M):
        upsilon = P % 2
        gamma = P - upsilon
        y = [0.0] * M
        z = [0.0] * N
        res = [[0.0] * M for _ in range(N)]

        for i in range(M):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += A[i][j] * A[i][j + 1]
            y[i] = aux

        for i in range(N):
            aux = 0.0
            for j in range(0, gamma, 2):
                aux += B[j][i] * B[j + 1][i]
            z[i] = aux

        if upsilon == 1:
            PP = P - 1
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    res[i][k] = aux - y[i] - z[k] + A[i][PP] * B[PP][k]
        else:
            for i in range(M):
                for k in range(N):
                    aux = 0.0
                    for j in range(0, gamma, 2):
                        aux += (A[i][j] + B[j + 1][k]) * (A[i][j + 1] + B[j][k])
                    res[i][k] = aux - y[i] - z[k]

        return res
    

    def alg_winograd_scaled(self, matrizA, matrizB, N, P, M):
        a = self.norm_inf(matrizA)
        b = self.norm_inf(matrizB)
        lambda_ = math.floor(0.5 + math.log(b / a) / math.log(4))
    
        copyA = self.multiply_with_scalar(matrizA, 2 ** lambda_)
        copyB = self.multiply_with_scalar(matrizB, 2 ** -lambda_)

        return self.alg_winograd_original(copyA, copyB, N, P, M)
    

    def multiply(self, matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB)
        M = len(matrizB[0])
        self.alg_winograd_scaled(matrizA, matrizB, N, P, M)

