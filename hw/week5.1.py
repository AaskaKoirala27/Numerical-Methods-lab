import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline
from sklearn.linear_model import LinearRegression

# Days
days = np.arange(1, 31)

# Temperature data with missing values
temp = np.array([
    22.86, 22.90, 22.79, 23.13, 23.85,
    23.10, 22.77, np.nan, 23.39, 22.03,
    22.15, 22.44, 22.87, 23.02, 22.91,
    22.53, 22.35, np.nan, 22.61, 22.47,
    np.nan, 22.74, 22.58, 22.39, np.nan,
    22.18, 22.24, 22.41, np.nan, 22.32
])

# -----------------------------
# Cubic Spline Interpolation
# -----------------------------

mask = ~np.isnan(temp)

x_known = days[mask]
y_known = temp[mask]

cs = CubicSpline(x_known, y_known)

missing_days = [8, 18, 21, 25, 29]

for day in missing_days:
    temp[day - 1] = cs(day)

print("========== INTERPOLATED VALUES ==========")

for day in missing_days:
    print(f"Day {day} = {temp[day - 1]:.4f}")

# -----------------------------
# Linear Regression
# -----------------------------

X = days.reshape(-1, 1)

model = LinearRegression()
model.fit(X, temp)

slope = model.coef_[0]
intercept = model.intercept_

print("\n========== REGRESSION MODEL ==========")
print(f"Slope (m) = {slope:.4f}")
print(f"Intercept (c) = {intercept:.4f}")

print(f"\nRegression Equation:")
print(f"y = {slope:.4f}x + {intercept:.4f}")

# -----------------------------
# Future Predictions
# -----------------------------

future_days = np.array([31, 32, 33, 34, 35]).reshape(-1, 1)

predictions = model.predict(future_days)

print("\n========== FUTURE PREDICTIONS ==========")

for day, pred in zip(future_days.flatten(), predictions):
    print(f"Day {day} = {pred:.4f}")

# -----------------------------
# Graph
# -----------------------------

plt.figure(figsize=(10, 6))

plt.plot(days, temp,
         marker='o',
         label='Temperature Data (After Interpolation)')

plt.plot(
    future_days.flatten(),
    predictions,
    marker='x',
    linestyle='--',
    label='Future Predictions'
)

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Analysis Using Cubic Spline Interpolation and Linear Regression")
plt.legend()
plt.grid(True)

plt.show()




