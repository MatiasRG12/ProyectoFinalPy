class LoadMatrix:
    
    @staticmethod
    def load_matrix_from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Parse the file contents into a matrix
        matrix = []
        for line in lines:
            values = list(map(int, line.split()))
            matrix.append(values)
        
        return matrix
