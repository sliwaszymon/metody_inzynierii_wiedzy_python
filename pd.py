import random as rand
import numpy as np

#############################################
# na 30.03.2022
#############################################
def sqrt(value, epsilon):
    a, b = value, 1
    while abs(a-b) > epsilon:
        a, b = (a+b)/2, value/((a+b)/2)
    return a

# print(sqrt(4, 0.00000000000000000001))

def montecarlo_integration(foo, xp, xk, sample):
    minimum, maximum = foo(xp), foo(xp)
    for i in np.arange(xp+0.1, xk+0.1, 0.1):
        if foo(i) < minimum:
            minimum = foo(i)
        if foo(i) > maximum:
            maximum = foo(i)
    minimum, maximum = minimum+10, maximum+10
    points = 0
    for j in range(sample):
        x = rand.uniform(xp, xk)
        y = rand.uniform(minimum, maximum)
        if y <= foo(x):
            points += 1
    print(points)
    return (xk-xp)*(maximum-minimum)*(points/sample)

def foo(x):
    # return x**2 + 2*x   # to jest funkcja
    return (x**3+ 3*x**2)/3   # to jest całka powyzszej

print(montecarlo_integration(foo, 4, 7, 1000000))

#############################################
# na 06.04.2022
#############################################
# WERSJA EASY
# def mean_average(list1):
#     sum = 0
#     for x in list1:
#         sum += x
#     return x / len(list1)

# def variance(list1):
#     mean_avg = mean_average(list1)
#     sum = 0
#     for x in list1:
#         sum += pow((x-mean_avg),2)
#     return sum / len(list1)

# def standard_deviation(list1):
#     return pow(variance(list1), 1/2)

# WERSJA HARD
def mean_average(list1):
    return sum(list1) / len(list1)

def variance(list1):
    return sum([pow((x-mean_average(list1)), 2) for x in list1]) / len(list1)

def standard_deviation(list1):
    return pow(variance(list1), 1/2)