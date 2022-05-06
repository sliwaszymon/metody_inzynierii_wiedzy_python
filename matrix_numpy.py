import numpy as np

def det(matrix): # napisane własnoręcznie w matrix_utils.py
    return np.linalg.det(matrix)

def inverse(matrix): # napisane własnoręcznie w matrix_utils.py
    return np.linalg.inv(matrix)

def vector_length(v):
    return pow((np.dot(v,v)), 1/2)

def projection(u,v):
    return list((np.dot(v,u) / np.dot(u,u)) * u)

def is_upper_triangular(matrix, epsilon = 0.001):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y < x:
                if matrix[x][y] > epsilon:
                    return False
    return True

def qr_decomposition(matrix, epsilon = 0.00001): # np.linalg.qr(matrix)
    matrix = np.transpose(matrix)
    Q = []
    all_U = [matrix[0]]
    e = np.array(all_U[0]) / vector_length(all_U[0])
    Q.append(e)
    for x in range(1, len(matrix)):
        U = matrix[x]
        for y in range(len(all_U)):
            U = U - projection(all_U[y], matrix[x])
        all_U.append(U)
        e = U / vector_length(U)
        Q.append(e)

    R = np.dot(Q, np.transpose(matrix))
    Q = np.transpose(Q)
    for x in range(len(R)):
        for y in range(len(R[x])):
            if abs(R[x][y]) < epsilon:
                R[x][y] = 0
    R = np.array(R)
    return (Q, R)

def next_A(matrix):
    q, r = qr_decomposition(matrix)
    return np.dot(r,q)

def eigenvalues(matrix, stop=5000): # np.inalg.eigvals(a)
    i = 0
    if (matrix == np.transpose(matrix)).all():
        while not is_upper_triangular(matrix):
            if i == stop:
                break
            matrix = next_A(matrix)
            i = i + 1
    return np.fliplr(matrix).diagonal()



######### TEST SECTION #########
matrix = np.array([[1,1,0], [1,0,1], [0,1,1]])

print(np.linalg.eigvals(matrix))    # [-1.  1.  2.]
print(eigenvalues(matrix))          # [ 0.  -0.50001144  0.]
# coś jest źle...
