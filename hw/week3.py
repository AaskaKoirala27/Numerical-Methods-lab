# Gauss-Seidel Method in Python

print("Enter coefficients of equations:")

a11 = float(input("a11: "))
a12 = float(input("a12: "))
a13 = float(input("a13: "))
b1 = float(input("b1: "))

a21 = float(input("a21: "))
a22 = float(input("a22: "))
a23 = float(input("a23: "))
b2 = float(input("b2: "))

a31 = float(input("a31: "))
a32 = float(input("a32: "))
a33 = float(input("a33: "))
b3 = float(input("b3: "))

# Initial guesses
x = 0
y = 0
z = 0

iterations = int(input("Enter number of iterations: "))

# Gauss-Seidel Iteration
for i in range(iterations):

    x = (b1 - a12*y - a13*z) / a11

    y = (b2 - a21*x - a23*z) / a22

    z = (b3 - a31*x - a32*y) / a33

print("Iteration", i+1)
print("x =", x)
print("y =", y)
print("z =", z)
print() 
   
print("Final Solution:")
print("x =", x)
print("y =", y)
print("z =", z)



