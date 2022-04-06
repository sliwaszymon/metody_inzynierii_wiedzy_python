class MatrixUtils:
    @staticmethod
    def transpose(matrix:list):
        ans = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                ans[x][y] = matrix[y][x]
        return ans

    @staticmethod
    def det(matrix:list):
        if len(matrix) == len(matrix[0]) and len(matrix) > 0:
            if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            else:
                matrixes = {x:[] for x in range(len(matrix))}
                temp = matrix[1:]
                for x in range(len(matrixes.keys())):
                    for y in range(len(temp)):
                        matrixes[x].append(temp[y][:x] + temp[y][x+1:])
                ans = 0
                for x in range(len(matrixes.values())):
                    ans += matrix[0][x] * pow(-1, 2+x) * MatrixUtils.det(list(matrixes.values())[x])
                return ans
        else:
            # raise ValueError("dimension mismatched")
            return None

    @staticmethod
    def drop_row(matrix:list, index:int):
        if index < len(matrix):
            return [matrix[x] for x in range(len(matrix)) if x is not index]
        else:
            raise ValueError("row with that index does not exist")

    @staticmethod
    def drop_col(matrix:list, index:int):
        if index < len(matrix[0]):
            return [[matrix[x][y] for y in range(len(matrix[x])) if y is not index] for x in range(len(matrix))]
        else:
            raise ValueError("col with that index does not exist")
    
    @staticmethod
    def drop_L(matrix:list, row:int, col:int): #like drop col then drop row but faster
        if col < len(matrix[0]) and row < len(matrix):
            return [[matrix[x][y] for y in range(len(matrix[x])) if y is not col] for x in range(len(matrix)) if x is not row]
        else:
            if row > len(matrix):
                raise ValueError("row with that index does not exist")
            else:
                raise ValueError("col with that index does not exist")

    @staticmethod
    def algebraic_complements(matrix:list):
        if len(matrix) == len(matrix[0]) and len(matrix) > 0:
            return [[pow(-1, 2+x+y) * MatrixUtils.det(MatrixUtils.drop_L(matrix, x, y)) for y in range(len(matrix[x]))] for x in range(len(matrix))]
        else:
            # raise ValueError("dimension mismatched")
            return None
    
    @staticmethod
    def inverse(matrix:list):
        if len(matrix) == len(matrix[0]):
            det = MatrixUtils.det(matrix)
            if det == 0:
                return None
            else:
                transpose = MatrixUtils.transpose(MatrixUtils.algebraic_complements(matrix))
                return [[float(y/det) for y in range(len(transpose[x]))] for x in range(len(transpose))]
        else:
            return None


class Matrix:
    value:list = None
    shape:tuple = None
    det:float = None
    transposed:list = None
    algebraic_complements:list = None
    inverse:list = None

    def __init__(self, matrix:list):
        self.value = matrix
        self.shape = (len(matrix), len(matrix[0]))
        self.det = MatrixUtils.det(self.value)
        self.transposed = MatrixUtils.transpose(self.value)
        self.algebraic_complements = MatrixUtils.algebraic_complements(self.value)
        self.inverse = MatrixUtils.inverse(self.value)
    
    def __str__(self):
        return str({
            'value': self.value,
            'shape': self.shape,
            'det': self.det,
            'transposed': self.transposed,
            'algebraic complements': self.algebraic_complements,
            'inverse': self.inverse
        })


mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix = Matrix(mat)
print(matrix)