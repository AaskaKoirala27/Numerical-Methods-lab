# #  RK4 Method for System of Differential Equations 
# def f1(t, y1, y2):
#     return y2

# def f2(t, y1, y2):
#     return -y1

# t = float(input("Enter initial time t0: "))
# y1 = float(input("Enter initial value y1: "))
# y2 = float(input("Enter initial value y2: "))
# h = float(input("Enter step size h: "))
# n = int(input("Enter number of iterations: "))

# print("\nt\t y1\t\t y2")

# for i in range(n):
#     k1_1 = h * f1(t, y1, y2)
#     k1_2 = h * f2(t, y1, y2)

#     k2_1 = h * f1(t + h/2, y1 + k1_1/2, y2 + k1_2/2)
#     k2_2 = h * f2(t + h/2, y1 + k1_1/2, y2 + k1_2/2)

#     k3_1 = h * f1(t + h/2, y1 + k2_1/2, y2 + k2_2/2)
#     k3_2 = h * f2(t + h/2, y1 + k2_1/2, y2 + k2_2/2)

#     k4_1 = h * f1(t + h, y1 + k3_1, y2 + k3_2)
#     k4_2 = h * f2(t + h, y1 + k3_1, y2 + k3_2)

#     y1 += (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6
#     y2 += (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) / 6

#     t += h

#     print(round(t, 2), "\t", round(y1, 5), "\t", round(y2, 5))



# Power Method for Smallest Eigenvalue

import numpy as np

n = int(input("Enter matrix size: "))

A = []
print("Enter matrix row by row:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)

iterations = int(input("Enter number of iterations: "))

x = np.ones(n)
x = x / np.linalg.norm(x)

for i in range(iterations):
    y = np.linalg.solve(A, x)
    x = y / np.linalg.norm(y)

eigenvalue = np.dot(x.T, np.dot(A, x)) / np.dot(x.T, x)

print("\nSmallest Eigenvalue Approximation:", round(eigenvalue, 5))

