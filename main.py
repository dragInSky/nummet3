import math

epsilon = 0.5 * 10 ** -4


def Jacobi():
    prev_x1 = 0
    prev_x2 = 0
    prev_x3 = 0
    x1 = 1.70
    x2 = 4.70
    x3 = -2.75
    n = 0
    while (math.fabs(x1 - prev_x1) > epsilon and
           math.fabs(x2 - prev_x2) > epsilon and
           math.fabs(x3 - prev_x3) > epsilon):
        n += 1
        prev_x1 = x1
        prev_x2 = x2
        prev_x3 = x3
        x1 = (1.70 + 0.50 * prev_x2 - 0.10 * prev_x3) / 0.95
        x2 = (4.70 + 0.15 * prev_x1 - 1.15 * prev_x3) / 1.55
        x3 = (-2.75 + 0.35 * prev_x1 + 0.25 * prev_x2) / -0.60

    print(f"Jacobi\n{n} итераций\nx1 - {x1}\nx3 - {x2}\nx2 - {x3}\n")


def GaussSeidel():
    prev_x1 = 0
    prev_x2 = 0
    prev_x3 = 0
    x1 = 1.70
    x2 = 4.70
    x3 = -2.75
    n = 0
    while (math.fabs(x1 - prev_x1) > epsilon and
           math.fabs(x2 - prev_x2) > epsilon and
           math.fabs(x3 - prev_x3) > epsilon):
        n += 1
        prev_x1 = x1
        prev_x2 = x2
        prev_x3 = x3
        x1 = (1.70 + 0.50 * prev_x2 - 0.10 * prev_x3) / 0.95
        x2 = (4.70 + 0.15 * x1 - 1.15 * x3) / 1.55
        x3 = (-2.75 + 0.35 * x1 + 0.25 * x2) / -0.60

    print(f"GaussSeidel\n{n} итераций\nx1 - {x1}\nx3 - {x2}\nx2 - {x3}\n")


Jacobi()
GaussSeidel()
