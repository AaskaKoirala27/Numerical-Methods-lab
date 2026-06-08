# WEEKLY PROJECT
## Week 2 : Transportation Expense Analysis Using Gaussian Elimination Method
# Pseudocode 

Step 1: START

Step 2: Input n (number of variables)

Step 3: Create empty matrix A

Step 4: FOR i = 1 to n
            Input row i of augmented matrix
        END FOR

Step 5: Display initial matrix A

Step 6: FOR i = 1 to n

            pivot = A[i][i]

            FOR j = i to n+1
                A[i][j] = A[i][j] / pivot
            END FOR

            FOR k = i+1 to n

                factor = A[k][i]

                FOR j = i to n+1
                    A[k][j] = A[k][j] - factor * A[i][j]
                END FOR

            END FOR

        END FOR

Step 7: Initialize solution array x[n]

Step 8: FOR i = n down to 1

            x[i] = A[i][n+1]

            FOR j = i+1 to n
                x[i] = x[i] - A[i][j] * x[j]
            END FOR

        END FOR

Step 9: Print x[1], x[2], x[3]

Step 10: STOP




