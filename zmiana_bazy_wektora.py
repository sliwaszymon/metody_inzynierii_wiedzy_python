import numpy as np

def vlen(v):
    return pow((np.dot(v,v)), 1/2)

v1 = np.array([1,1,1,1,1,1,1,1])
v2 = np.array([1,1,1,1,-1,-1,-1,-1])
v3 = np.array([1,1,-1,-1,0,0,0,0])
v4 = np.array([0,0,0,0,1,1,-1,-1])
v5 = np.array([1,-1,0,0,0,0,0,0])
v6 = np.array([0,0,1,-1,0,0,0,0])
v7 = np.array([0,0,0,0,1,-1,0,0])
v8 = np.array([0,0,0,0,0,0,1,-1])

Xa = np.array([8,6,2,3,4,6,6,5])

# macierz matrix w danych wejściowych jest TRANSPOZYCJĄ BAZY!
matrix = np.array([v1,v2,v3,v4,v5,v6,v7,v8])
norm = np.array([x/vlen(x) for x in matrix], dtype=np.float64)

ans = np.dot(norm, Xa.T)
print(ans)
