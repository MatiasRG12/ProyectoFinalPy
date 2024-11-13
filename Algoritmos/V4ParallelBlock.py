from concurrent.futures import ThreadPoolExecutor
import IMatrixMultiplication

class v4ParallelBlock(IMatrixMultiplication):

    def __init__(self, some_param = None):
        self.some_param = some_param

    def block_multiply(self, matrizA, matrizB, matrizC, i1, size1, size2):
        for j1 in range(0, size1, size2):
            for k1 in range(0, size1, size2):
                for i in range(i1, min(i1 + size2, size1)):
                    for j in range(j1, min(j1 + size2, size1)):
                        for k in range(k1, min(k1 + size2, size1)):
                            matrizC[k][i] += matrizA[k][j] * matrizB[j][i]


    def alg_V_4_ParallelBlockTres(self, matrizA, matrizB, size1, size2):
        matrizC = [[0.0 for _ in range(size1)] for _ in range(size1)]
        num_blocks = (size1 + size2 - 1) // size2  # Calculate the number of blocks
        with ThreadPoolExecutor() as executor:
            # Dispatch each block to a separate thread
            futures = [executor.submit(self.block_multiply, matrizA, matrizB, matrizC, i1, size1, size2)
                    for i1 in range(0, size1, size2)]
            for future in futures:
                future.result()  # Wait for all threads to complete
        return matrizC
    

    def multiply(self, matrizA, matrizB):
        N = len(matrizA)
        P = len(matrizB[0])
        self.alg_V_4_ParallelBlockTres(matrizA, matrizB, N, P)