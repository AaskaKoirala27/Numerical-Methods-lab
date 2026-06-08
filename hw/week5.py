import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# -----------------------------
# USER INPUT
# -----------------------------
n = int(input("Enter number of data points: "))

x = []
y = []

print("\nEnter x values:")
for i in range(n):
    x.append(float(input(f"x[{i}]: ")))

print("\nEnter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}]: ")))

x = np.array(x)
y = np.array(y)

# -----------------------------
# CUBIC SPLINE MODEL
# -----------------------------
cs = CubicSpline(x, y)

# -----------------------------
# INTERPOLATION AT A POINT
# -----------------------------
x_interp = float(input("\nEnter the x value for interpolation: "))
y_interp = cs(x_interp)

print("\n===== INTERPOLATED RESULT =====")
print(f"Interpolated value at x = {x_interp} is y = {y_interp:.4f}")

# -----------------------------
# GENERATE SMOOTH CURVE
# -----------------------------
x_new = np.linspace(min(x), max(x), 200)
y_new = cs(x_new)

# -----------------------------
# SAMPLE INTERPOLATED POINTS
# -----------------------------
print("\n===== SAMPLE INTERPOLATED POINTS =====")
for i in range(0, len(x_new), 40):
    print(f"x = {x_new[i]:.2f}, y = {y_new[i]:.4f}")

# -----------------------------
# PLOTTING GRAPH
# -----------------------------
plt.figure(figsize=(8, 5))

# original points
plt.scatter(x, y, color='red', s=60, label='Original Data Points')

# spline curve
plt.plot(x_new, y_new, linewidth=2, label='Cubic Spline Curve')

# interpolated point (IMPORTANT)
plt.scatter(x_interp, y_interp, color='green', s=100, zorder=5,
            label=f'Interpolated Point ({x_interp}, {y_interp:.4f})')

plt.title("Cubic Spline Interpolation")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.legend()

plt.show()