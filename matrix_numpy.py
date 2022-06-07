import numpy as np
import sys
import math

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

def eigenvalues(matrix, stop=5000): # (oparte o ciąg Ak -> RQ do momentu aż macież będzie trójkątną górną) np.linalg.eigvals(a)
    i = 0
    if (matrix == np.transpose(matrix)).all():
        while not is_upper_triangular(matrix):
            if i == stop:
                break
            matrix = next_A(matrix)
            i = i + 1
    return np.fliplr(matrix).diagonal()

def gauss_elimination(matrix):
    matrix = np.array(matrix, dtype=np.float64)
    matrix.dtype = np.float64
    for x in range(len(matrix)):
        if matrix[x][x] == 0.0:
            sys.exit("dzielenie przez 0")
        for y in range (x+1, len(matrix)):
            ratio = matrix[y][x]/matrix[x][x]
            for z in range(len(matrix)+1):
                matrix[y][z] = matrix[y][z] - ratio * matrix[x][z]
    return matrix

def back_substitution(matrix):
    ans = np.zeros(len(matrix))
    ans[len(matrix)-1] = matrix[len(matrix)-1][len(matrix)]/matrix[len(matrix)-1][len(matrix)-1]
    for x in range(len(matrix)-2, -1, -1):
        ans[x] = matrix[x][len(matrix)]
        for y in range(x+1, len(matrix)):
            ans[x] = ans[x] - matrix[x][y]*ans[y]
        ans[x] = ans[x]/matrix[x][x]
    return ans

def gauss_equation_solving(matrix):
    return back_substitution(gauss_elimination(matrix))

def svd(A):
    AAT = np.dot(A, A.T)
    ATA = np.dot(A.T, A)
    
    if AAT.shape[0] * AAT.shape[1] > ATA.shape[0] * ATA.shape[1]:
        EIGVALS = np.sort(np.linalg.eigvals(AAT))[::-1] # wartości własne z numpy bo szybciej działa
        EIGVALS = [x if math.fabs(x) > 0.000001 else 0 for x in EIGVALS]
        SINGVALS = np.array([pow(x, 1/2) for x in EIGVALS if x != 0])
        U = np.linalg.eigh(AAT)[1]
        for y in range(U.shape[0]):
            for x in range(U.shape[1]):
                if math.fabs(U[y][x]) < 0.000001:
                    U[y][x] = 0 
        # np.linalg.eigh zwraca macierze wyliczone z lambd posortowanych ROSNĄCO więc trzeba wiersze przekręcić od dołu do góry
        U = U.T
        U = U[::-1]
        U = U.T

        V = []
        for x in range(ATA.shape[0]):
            V.append(np.dot(A.T, U.T[x]) * (1/SINGVALS[x]))
        V = np.array(V)
    else:
        EIGVALS = np.sort(np.linalg.eigvals(ATA))[::-1]
        EIGVALS = [x if math.fabs(x) > 0.000001 else 0 for x in EIGVALS]
        SINGVALS = np.array([pow(x, 1/2) for x in EIGVALS if x != 0])
        V = np.linalg.eigh(ATA)[1]
        for y in range(V.shape[0]):
            for x in range(V.shape[1]):
                if math.fabs(V[y][x]) < 0.000001:
                    V[y][x] = 0 

        V = V.T
        V = V[::-1]
        V = V.T

        U = []
        for x in range(AAT.shape[0]):
            U.append(np.dot(A, V.T[x]) * (1/SINGVALS[x]))
        U = np.array(U)
    
    
    SIGMA = np.zeros(A.shape)
    for y in range(SIGMA.shape[0]):
        for x in range(SIGMA.shape[1]):
            if y == x:
                SIGMA[y][x] = SINGVALS[x]
    
    # SZCZERZE MÓWIĄC NIE WIEM JAK ZAPROGRAMOWAĆ WEKTORY DO MACIERZY U I V RĘCZNIE BEZ BIBLIOTEK
    # BO GAUSS ŚREDNIO PASUJE 

    return U, SIGMA, V.T



######### TEST SECTION #########
# matrix = np.array([[1,1,0,], [1,0,1], [0,1,1]])
# matrix = np.array([[4,-2,4,-2,8],[3,1,4,2,7],[2,4,2,1,10],[2,-2,4,2,2]])
matrix = np.array([[1,-2,0],[0,-2,1]])
# print(np.linalg.eigvals(matrix))    # [-1.  1.  2.]
# print(eigenvalues(ma trix))          # [ 0.  -0.50001144  0.]
# coś jest źle...
# print(gauss_elimination(matrix))
# print(back_substitution(gauss_elimination(matrix)))
# print(gauss_equation_solving(matrix))


print("=== MOJE SVD ===")
U, SIGMA, VT = svd(matrix)
print("===== U =====")
print(U)
print("=== SIGMA ===")
print(SIGMA)
print("===== VT =====")
print(VT)
# print("=== powrót do A ===")
# print(np.dot(np.dot(U, SIGMA), VT))

# print("=== NUMPY SVD ===")
# u, s, vh = np.linalg.svd(matrix)
# print("===== U =====")
# print(u)
# print("=== SIGMA ===")
# print(s)
# print("===== VT =====")
# print(vh)

