# Numerical-Methods-lab

# Week 2 - Inverse of Matrix using Gauss-Jordan Method

## Pseudo Code 
 
START

Input n
Input matrix A[n][n]

Create identity matrix I[n][n]

FOR i = 0 to n-1

    pivot = A[i][i]

    Normalize row i of A and I by dividing by pivot
    

    FOR k = 0 to n-1
        IF k != i THEN

            factor = A[k][i]

            FOR j = 0 to n-1
                A[k][j] = A[k][j] - factor * A[i][j]
                I[k][j] = I[k][j] - factor * I[i][j]
            END FOR

        END IF
    END FOR

END FOR

PRINT matrix I

STOP


# Week 3 - Implementation of Gauss–Seidel Method

## Pseudo Code 


START

Input coefficients and constants

Initialize x = 0
Initialize y = 0
Initialize z = 0

Input number of iterations

FOR i = 1 to iterations

    x = (b1 - a12*y - a13*z) / a11

    y = (b2 - a21*x - a23*z) / a22

    z = (b3 - a31*x - a32*y) / a33

END FOR

Print x, y, z

STOP

# Week 4 - Implementation of Numerical Methods Using Python

## Development, Debugging, and Testing of Newton Raphson Method, Two Equations of Newton Raphson Method, and Secant Method Using Python

## Pseudo Code - Newton Raphson Method

START

Input initial guess x
Input tolerance
Input maximum iterations

Define function f(x)
Define derivative f'(x)

FOR each iteration
    x_new = x - f(x)/f'(x)

    IF absolute(x_new - x) < tolerance
        PRINT root
        STOP
    END IF

    x = x_new
END FOR

PRINT final approximation

STOP


## Week 5 - Pseudocode: Two Equations Newton Raphson Method

START

Input x and y
Input tolerance
Input maximum iterations

Define equations f(x,y) and g(x,y)

FOR each iteration

    Calculate Jacobian determinant

    Calculate new x and y values

    IF error < tolerance
        PRINT solution
        STOP
    END IF

    Update x and y

END FOR

STOP

## Pseudocode: Secant Method

START

Input x0 and x1
Input tolerance
Input maximum iterations

Define function f(x)

FOR each iteration

    x2 = x1 - [f(x1)(x1 - x0)] / [f(x1) - f(x0)]

    IF absolute(x2 - x1) < tolerance
        PRINT root
        STOP
    END IF

    x0 = x1
    x1 = x2

END FOR

STOP


# Cubic Spline Interpolation in Python
## Pseudocode

START

Input n
Input x[0..n], y[0..n]

Create spline function using x and y

Generate x_new values

FOR each value in x_new
    compute y_new using spline
END FOR

Display results

Plot original points and spline curve

END


# Week 5 - Application of Interpolation and Regression Techniques in Environmental Data Analysis
## Pseudocode

START

Load dataset

Identify missing values

Apply Cubic Spline Interpolation

FOR each missing observation
      Construct spline equations
      Solve spline coefficients
      Estimate missing value
END FOR

Store completed dataset

Apply Linear Regression

Compute slope and intercept

Construct regression equation

FOR future days 31 to 35
      Predict temperature
END FOR

Display results

END


