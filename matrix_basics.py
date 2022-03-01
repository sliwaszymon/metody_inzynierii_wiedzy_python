def transpose(matrix):
    ans = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            ans[x][y] = matrix[y][x]
    return ans


example = [
    [2,5,3],
    [6,7,3]
]
