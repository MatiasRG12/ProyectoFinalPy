import IMatrixMultiplication

class v3SequentialBlock(IMatrixMultiplication):

    def alg_V_3_Sequential_Block(self, matrizA, matrizB, size1, size2):
        # Inicialización de la matriz de resultados
        matrizRes = [[0.0 for _ in range(size1)] for _ in range(size1)]
    
        # Multiplicación de matrices por bloques
        for i1 in range(0, size1, size2):
            for j1 in range(0, size1, size2):
                for k1 in range(0, size1, size2):
                    for i in range(i1, min(i1 + size2, size1)):
                        for j in range(j1, min(j1 + size2, size1)):
                            for k in range(k1, min(k1 + size2, size1)):
                                matrizRes[k][i] += matrizA[k][j] * matrizB[j][i]
        return matrizRes


    def multiply(self, matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB[0])
        self.alg_V_3_Sequential_Block(matrizA, matrizB, N, P)

