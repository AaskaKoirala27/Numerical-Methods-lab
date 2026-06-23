# # CA7.1 Python Program
# # Least Squares Curve Fitting for Nusselt Number Model
# import numpy as np

# # Given data
# Di_Do = np.array([0.02, 0.05, 0.10, 0.25, 0.50, 1.00])
# Nu = np.array([32.337, 17.46, 11.56, 7.3708, 5.7382, 4.8608])

# # Convert to Do/Di
# x = 1 / Di_Do

# # Design matrix
# A = np.column_stack((np.ones(len(x)), x, x**2))

# # Least squares solution
# coeff = np.linalg.lstsq(A, Nu, rcond=None)[0]

# a, b, c = coeff

# print("Least Squares Coefficients")
# print("-------------------------")
# print("a =", a)
# print("b =", b)
# print("c =", c)

# print("\nModel:")
# print(f"Nu = {a:.6f} + {b:.6f}(Do/Di) + {c:.6f}(Do/Di)^2")

# # Predicted values
# Nu_pred = A @ coeff

# print("\nComparison Table")
# print("Do/Di\tActual\tPredicted")

# for xi, actual, pred in zip(x, Nu, Nu_pred):
#     print(f"{xi:.0f}\t{actual:.4f}\t{pred:.4f}")


# CA8.4 Python Program
# Numerical Integration

import numpy as np
from scipy.integrate import fixed_quad

# Function
def f(x):
    return 1/(1 + np.exp(x))

# Exact value
true_value = 1 + np.log(2/(1 + np.e))

print("True Integral Value =", true_value)

# -----------------------------
# Trapezoidal Rule
# -----------------------------
def trapezoidal(n):
    a, b = 0, 1
    h = (b-a)/n

    x = np.linspace(a, b, n+1)
    y = f(x)

    return h * (0.5*y[0] + np.sum(y[1:n]) + 0.5*y[n])

print("\nTRAPEZOIDAL RULE")
for n in [6, 12, 24, 48]:
    result = trapezoidal(n)
    error = abs(result - true_value)

    print(f"Panels={n:2d}  Integral={result:.12f}  Error={error:.12e}")

# -----------------------------
# Simpson's Rule
# -----------------------------
def simpson(n):
    a, b = 0, 1
    h = (b-a)/n

    x = np.linspace(a, b, n+1)
    y = f(x)

    return (h/3)*(y[0] + y[-1]
                  + 4*np.sum(y[1:-1:2])
                  + 2*np.sum(y[2:-2:2]))

print("\nSIMPSON'S RULE")
for n in [10, 20, 50]:
    result = simpson(n)
    error = abs(result - true_value)

    print(f"Panels={n:2d}  Integral={result:.12f}  Error={error:.12e}")

# -----------------------------
# Gauss-Legendre Quadrature
# -----------------------------
print("\nGAUSS-LEGENDRE QUADRATURE")

for n in [3, 5, 7, 9]:
    result, _ = fixed_quad(f, 0, 1, n=n)
    error = abs(result - true_value)

    print(f"Points={n:2d}  Integral={result:.12f}  Error={error:.12e}")
