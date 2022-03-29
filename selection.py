import random
import numpy as np

def get_from_file(file):
    ans = []
    with open(file, "r") as file:
        for line in file:
            ans.append(list(map(lambda x: float(x), line.replace("\n", "").split())))
    return ans

def suffle(dataset1):
    temp = dataset1.copy()
    for x in range(len(dataset1)):
        temp[x] = dataset[x].copy()
        temp[x][-1] = random.choice([0,1])
    return temp

def sort_by_key(dataset):
    ans = {}
    for point in dataset:
        if point[-1] not in ans.keys():
            ans[point[-1]] = [point]
        else:
            ans[point[-1]].append(point)
    return ans

def euclidean_distance(list1, list2, delete=True):
    if delete:
        x = max(len(list1), len(list2)) - 1
        a = np.array(list1[:x])
        b = np.array(list2[:x])
    else:
        a = np.array(list1)
        b = np.array(list2)
    c = b - a
    return pow(np.dot(c, c), 1/2)

def central_spots(sorted_dataset):
    ans = {}
    for key in sorted_dataset.keys():
        temp = {}
        for x in range(len(sorted_dataset[key])):
            dist = 0
            for y in range(len(sorted_dataset[key])):
                if x != y:
                    dist += euclidean_distance(sorted_dataset[key][x], sorted_dataset[key][y])
            temp[tuple(sorted_dataset[key][x])] = dist
        ans[key] = list(list(temp.keys())[list(temp.values()).index(min(temp.values()))])
    return ans

def decision(point, central_spots):
    temp = central_spots.copy()
    for key in central_spots.keys():
        temp[key] = euclidean_distance(point, central_spots[key])
    ans = [x for x,y in temp.items() if y == min(temp.values())]
    if len(ans) > 1:
        return None
    return ans[0]

def seggregate(dataset1, dataset2):
    swaps = 1
    while swaps > 0:
        swaps = 0
        sorted_dataset = sort_by_key(dataset1)
        actual_central_spots = central_spots(sorted_dataset)
        for x in range(len(dataset1)):
            if decision(dataset1[x], actual_central_spots) != dataset1[x][-1]:
                dataset1[x][-1] = decision(dataset1[x], actual_central_spots)
                swaps += 1
        print(check_diff(dataset1, dataset2))
    return dataset

def check_diff(dataset1, dataset2):
    diff = 0
    for x in range(len(dataset1)):
        if (dataset1[x][-1] != dataset2[x][-1]):
            diff += 1

    return str((len(dataset1) - diff) / len(dataset1) * 100) + "%"


dataset = get_from_file("australian.dat")
dataset_suffled = suffle(dataset)
# sorted_dataset = sort_by_key(dataset)
# actual_central_spots = central_spots(sorted_dataset)
dataset_end = seggregate(dataset_suffled, dataset)