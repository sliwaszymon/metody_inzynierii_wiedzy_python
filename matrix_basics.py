def transpose(matrix):
    ans = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            ans[x][y] = matrix[y][x]
    return ans


def matrix_det(matrix):
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
                ans += matrix[0][x] * pow(-1, 2+x) * matrix_det(list(matrixes.values())[x])
            return ans
    else:
        raise ValueError("dimension mismatched")


example = [
    [2,5,3,2],
    [6,7,3,4],
    [1,2,3,6],
    [7,7,7,8]
]
ex_error = [
    [2,5,3,2],
    [6,7,3,4],
    [1,2,3,6],
]

print(matrix_det(example))
print(matrix_det(ex_error))