# Gaussian Elimination with User Input + Steps Display

n = int(input("Enter number of variables (e.g., 3): "))

# Augmented matrix input
A = []

print("\nEnter augmented matrix coefficients row by row:")
print("Format: a b c d (last value is constant)\n")

for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nInitial Augmented Matrix:")
for row in A:
    print(row)

# Gaussian Elimination
for i in range(n):

    pivot = A[i][i]

    print(f"\n--- Step {i+1}: Pivot = {pivot} ---")

    # Normalize pivot row
    for j in range(i, n+1):
        A[i][j] = A[i][j] / pivot

    print(f"Row {i+1} after normalization:")
    print(A[i])

    # Eliminate below rows
    for k in range(i+1, n):

        factor = A[k][i]

        print(f"R{k+1} = R{k+1} - ({factor}) * R{i+1}")

        for j in range(i, n+1):
            A[k][j] = A[k][j] - factor * A[i][j]

        print(f"Updated Row {k+1}: {A[k]}")

# Back Substitution
x = [0] * n

print("\nBack Substitution Process:")

for i in range(n-1, -1, -1):

    x[i] = A[i][n]

    for j in range(i+1, n):
        x[i] -= A[i][j] * x[j]

    print(f"x{i+1} = {x[i]}")

# Final Output
print("\nFinal Results:")
print("Bus =", x[0])
print("Taxi =", x[1])
print("Fuel =", x[2])


