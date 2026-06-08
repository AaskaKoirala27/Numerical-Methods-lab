# Inverse of Matrix using Gauss-Jordan Method

n = int(input("Enter size of matrix: "))
A = []
I = []
print("Enter matrix elements:")
for i in range(n):
    A.append(list(map(float, input().split())))

# Identity matrix
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1.0)
        else:
            row.append(0.0)
    I.append(row)

# Gauss-Jordan elimination
for i in range(n):

    pivot = A[i][i]

    # Normalize pivot row
    for j in range(n):
        A[i][j] /= pivot
        I[i][j] /= pivot

    # Eliminate other rows
    for k in range(n):
        if k != i:

            factor = A[k][i]

            for j in range(n):
                A[k][j] -= factor * A[i][j]
                I[k][j] -= factor * I[i][j]

# Output inverse
print("\nInverse Matrix:")

for row in I:
    print(row)


    
    