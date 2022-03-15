def get_from_file(file):
    ans = []
    with open(file, "r") as file:
        for line in file:
            ans.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return ans

def euclidean_distance(list1, list2):
    if len(list1) == len(list1):
        sum = 0
        for x in range(len(list1)-1):
            sum += pow(list2[x] - list1[x], 2)
        return pow(sum, 1/2)
    else:
        return False

def distances(macierz):
    ans = {0: [], 1: []}
    for x in range(1, len(macierz), 1):
        ans[macierz[x][len(macierz[x])-1]].append(euclidean_distance(macierz[0], macierz[x]))
    return ans


macierz = get_from_file("australian.dat")
dystanse = distances(macierz)
print(dystanse)