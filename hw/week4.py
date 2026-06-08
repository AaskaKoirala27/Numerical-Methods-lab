# # import math

# # def f(x):
# #     return x**3 - x - 2

# # def df(x):
# #     return 3*x**2 - 1

# # x = float(input("Enter initial guess: "))
# # tolerance = float(input("Enter tolerance: "))
# # max_iter = int(input("Enter maximum iterations: "))

# # print("\nIteration\tValue of x")

# # for i in range(max_iter):
# #     x_new = x - f(x)/df(x)

# #     print(i + 1, "\t\t", round(x_new, 6))

# #     if abs(x_new - x) < tolerance:
# #         print("\nRoot found =", round(x_new, 6))
# #         break

# #     x = x_new



# import math

# def f(x, y):
#     return x**2 + y**2 - 4

# def g(x, y):
#     return x - y - 1

# def fx(x, y):
#     return 2*x

# def fy(x, y):
#     return 2*y

# def gx(x, y):
#     return 1

# def gy(x, y):
#     return -1

# x = float(input("Enter initial value of x: "))
# y = float(input("Enter initial value of y: "))

# tolerance = float(input("Enter tolerance: "))
# max_iter = int(input("Enter maximum iterations: "))

# print("\nIteration\t x\t\t y")

# for i in range(max_iter):

#     J = fx(x, y)*gy(x, y) - fy(x, y)*gx(x, y)

#     x_new = x - ((f(x, y)*gy(x, y) - g(x, y)*fy(x, y)) / J)

#     y_new = y - ((fx(x, y)*g(x, y) - gx(x, y)*f(x, y)) / J)

#     print(i + 1, "\t\t", round(x_new, 6), "\t", round(y_new, 6))

#     if abs(x_new - x) < tolerance and abs(y_new - y) < tolerance:
#         print("\nSolution:")
#         print("x =", round(x_new, 6))
#         print("y =", round(y_new, 6))
#         break

#     x = x_new
#     y = y_new


import math

def f(x):
    return x**3 - x - 2

x0 = float(input("Enter first guess: "))
x1 = float(input("Enter second guess: "))

tolerance = float(input("Enter tolerance: "))
max_iter = int(input("Enter maximum iterations: "))

print("\nIteration\tValue of x")

for i in range(max_iter):

    x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

    print(i + 1, "\t\t", round(x2, 6))

    if abs(x2 - x1) < tolerance:
        print("\nRoot found =", round(x2, 6))
        break

    x0 = x1
    x1 = x2

