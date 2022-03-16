def get_from_file(file):
    ans = []
    with open(file, "r") as file:
        for line in file:
            ans.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return ans

def euclidean_distance(list1, list2):
    if abs(len(list1)-len(list1)) == 1 or abs(len(list1)-len(list1)) == 0:
        sum = 0
        for x in range(max(len(list1), len(list2))-1):
            sum += pow(list2[x] - list1[x], 2)
        return pow(sum, 1/2)
    else:
        return False

def distances(macierz):
    ans = {}
    for x in range(len(macierz)):
        if macierz[x][-1] not in ans.keys():
            ans[int(macierz[x][-1])] = [euclidean_distance(macierz[0], macierz[x])]
        else:
            ans[macierz[x][-1]].append(euclidean_distance(macierz[0], macierz[x]))
    return ans

def distance_between(x, lista):
    ans = {}
    for y in range(len(lista)):
        if lista[y][-1] not in ans.keys():
            ans[int(lista[y][-1])] = [euclidean_distance(x, lista[y])]
        else:
            ans[lista[y][-1]].append(euclidean_distance(x, lista[y]))
    return ans

def _distance_between(x, lista):
    ans = []
    for y in range(len(lista)):
        ans.append((int(lista[y][-1]), euclidean_distance(x, lista[y])))
    return ans

def _grupujemy(lista, n):
    ans = {}
    for x in lista:
        if x[0] not in ans.keys():
            ans[x[0]] = [x[1]]
        else:
            ans[x[0]].append(x[1])
    for key in ans.keys():
        ans[key].sort()
        temp = 0
        for x in range(n):
            temp += ans[key][x]
        ans[key] = temp
    return ans        
    
    

macierz = get_from_file("australian.dat")
dystanse = distances(macierz)
# print(dystanse)

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(_grupujemy(_distance_between(x, macierz), 5))