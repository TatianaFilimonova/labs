import pandas as pd
import matplotlib.pyplot as plt
import csv

def rotate(A,B,C):
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])

def jarvismarch(A):
    n = len(A)
    P = list(range(n))
    for i in range(1, n):
        if A[P[i]][0] > A[P[0]][0]:
            P[i], P[0] = P[0], P[i]
    H = [P[0]]
    del P[0]
    P.append(H[0])
    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(A[H[-1]], A[P[right]], A[P[i]]) > 0:
                right = i
        if P[right] == H[0]:
#            H.append(H[0])
            break
        else:
            H.append(P[right])
            del P[right]
    return H

all_points = []
my_points = []
i = 0

res1 = pd.read_csv(r'C:\Users\filim\Downloads\convex.csv', header=None)
var = 14 - 1

i = 0
while i < 1000: # массив с координатами вообще всех точек
    all_points.append([res1.loc[var, i], res1.loc[var, i + 1]])
    i += 2
#print(all_points)

my_points = jarvismarch(all_points) # получили положение в массиве координат только точек оболочки
#print(my_points)

k = 0
for k in range(len(my_points)): # Получили обратно сами точки оболочки
    my_points[k] = all_points[my_points[k]]
#print(my_points)

excess_point = [i for i in all_points if i not in my_points]
#print(excess_point)

i = 0
X0 = []
Y0 = []
while i < len(excess_point):
    X0.append(excess_point[i][0])
    Y0.append(excess_point[i][1])
    i += 1
plt.scatter(X0, Y0, color = "gold")

X1 = []
Y1 = []
i = 0
while i < len(my_points):
    X1.append(my_points[i][0])
    Y1.append(my_points[i][1])
    i += 1
X1.append(X1[0])
Y1.append(Y1[0])
plt.plot(X1, Y1, color = "red")
plt.scatter(X1, Y1, color = "brown")
plt.title("Variant 14")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('My_points_graf.png')
plt.show()


X1.reverse()
Y1.reverse()

pd.DataFrame({'X': X1, 'Y': Y1}).to_csv('My_points.csv')