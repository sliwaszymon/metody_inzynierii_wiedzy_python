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


# PRACA DOMOWA 1
# def distances(macierz):
#     ans = {}
#     for x in range(1, len(macierz), 1):
#         if macierz[x][-1] not in ans.keys():
#             ans[int(macierz[x][-1])] = [euclidean_distance(macierz[0], macierz[x])]
#         else:
#             ans[macierz[x][-1]].append(euclidean_distance(macierz[0], macierz[x]))
#     return ans

# NIBY DOBRZE ALE ZAMIAST DO SLOWNIKA MAJA BYC TUPLE
# def distance_between(x, lista):
#     ans = {}
#     for y in range(len(lista)):
#         if lista[y][-1] not in ans.keys():
#             ans[int(lista[y][-1])] = [euclidean_distance(x, lista[y])]
#         else:
#             ans[lista[y][-1]].append(euclidean_distance(x, lista[y]))
#     return ans

def _distance_between(x, lista):
    ans = []
    for y in range(len(lista)):
        ans.append((int(lista[y][-1]), euclidean_distance(x, lista[y])))
    return ans

def _group(lista):
    ans = {}
    for x in lista:
        if x[0] not in ans.keys():
            ans[x[0]] = [x[1]]
        else:
            ans[x[0]].append(x[1])
    return ans

def _knn(dictionary, k):
    for key in dictionary.keys():
        dictionary[key].sort()
        dictionary[key] = sum(dictionary[key][:k])
    return dictionary

def aggregate(dictionary):
    ans = [x for x,y in dictionary.items() if y == min(dictionary.values())]
    if len(ans) > 1:
        return None
    return ans[0]
    # return list(dictionary.keys())[list(dictionary.values()).index(min(dictionary.values()))]



macierz = get_from_file("australian.dat")
# dystanse = distances(macierz)
# print(dystanse)

x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(aggregate(_knn(_group(_distance_between(x, macierz)), 5)))