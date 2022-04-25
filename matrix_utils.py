from statistics import linear_regression
import numpy as np

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
        if len(matrix) == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix) == len(matrix[0]) and len(matrix) > 0:
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
        det = MatrixUtils.det(matrix)
        if det == 0:
            return None
        else:
            if len(matrix) == 2:
                return [[matrix[1][1]/det, (-1)*matrix[0][1]/det], [(-1)*matrix[1][0]/det, matrix[0][0]/det]]
            elif len(matrix) == len(matrix[0]):
                transpose = MatrixUtils.transpose(MatrixUtils.algebraic_complements(matrix))
                return [[float(y/det) for y in range(len(transpose[x]))] for x in range(len(transpose))]
            else:
                return None
    
    @staticmethod
    def linear_regression(matrix:list):
        x = [matrix[x][0] for x in range(len(matrix))]
        y = [matrix[x][1] for x in range(len(matrix))]
        X = [[1 for x in range(len(x))], x]
        dot1 = np.dot(X, MatrixUtils.transpose(X))
        inverse = MatrixUtils.inverse([list(x) for x in list(dot1)])
        dot2 = np.dot(y, MatrixUtils.transpose(X))
        return list(np.dot(inverse, dot2))

    @staticmethod
    def vector_length(vector:list):
        v = np.array(vector)
        return pow((np.dot(v,v)), 1/2)

    @staticmethod
    def projection(u:list, v:list):
            u = np.array(u)
            v = np.array(v)
            return list((np.dot(v,u) / np.dot(u,u)) * u)

    @staticmethod
    def qr_decomposition(matrix:list, epsilon:float = 0.00001):
        temp = MatrixUtils.transpose(matrix)
        Q = []
        all_U = [temp[0]]
        e = list(np.array(all_U[0]) / MatrixUtils.vector_length(all_U[0]))
        Q.append(e)
        for x in range(1, len(temp)):
            u = np.array(temp[x])
            for y in range(len(all_U)):
                u = u - np.array(MatrixUtils.projection(all_U[y], temp[x]))
            u = list(u)
            all_U.append(u)
            e = list(np.array(u) / MatrixUtils.vector_length(u))
            Q.append(e)
        R = np.dot(np.array(Q), np.array(matrix))
        R = [list(x) for x in R]
        for x in range(len(R)):
            for y in range(len(R[x])):
                if abs(R[x][y]) < epsilon:
                    R[x][y] = 0
        return MatrixUtils.transpose(Q), list(R)


class Matrix:
    value:list = None
    shape:tuple = None
    det:float = None
    transposed:list = None
    algebraic_complements:list = None
    inverse:list = None
    linear_regression:list = None

    def __init__(self, matrix:list):
        self.value = matrix
        self.shape = (len(matrix), len(matrix[0]))
        self.det = MatrixUtils.det(self.value)
        self.transposed = MatrixUtils.transpose(self.value)
        self.algebraic_complements = MatrixUtils.algebraic_complements(self.value)
        self.inverse = MatrixUtils.inverse(self.value)
        self.linear_regression = MatrixUtils.linear_regression(self.value)
    
    def __str__(self):
        return str({
            'value': self.value,
            'shape': self.shape,
            'det': self.det,
            'transposed': self.transposed,
            'algebraic complements': self.algebraic_complements,
            'inverse': self.inverse,
            'linear_regression': self.linear_regression
        })


# mat = Matrix([[2,1],[5,2],[7,3],[8,3]])
# print(mat)

# print(MatrixUtils.qr_decomposition([[2,1], [1,0], [0,2]]))
print(MatrixUtils.qr_decomposition([[2,3,2], [1,0,3], [0,1,1]]))