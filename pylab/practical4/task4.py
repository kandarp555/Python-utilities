# Write a program to solve three linear equations with
# variables x, y, and z using NumPy.
import numpy as np

lst1 = []
lst2 = []
lst3 = []
j, elem2 = 0, 0
print("Enter the coefficients of x y z and RHS:")
for i in range(0, 9):
    if i % 3 == 0:
        j = j + 1
        print("For equation", j)
        elem1 = int(input("x:"))
    elif i == 1 or i == 4 or i == 7:
        elem1 = int(input("y:"))
    else:
        elem1 = int(input("z:"))
        elem2 = int(input("RHS:"))
        lst2.append(elem2)
    lst1.append(elem1)
A = np.array(lst1).reshape(3, 3)
print("A =\n", A)
B = np.array(lst2).reshape(3, 1)
print("B =\n", B)
print("\nWe have to find X\nFrom equation A.X = B\n")
X = np.dot(np.linalg.inv(A), B)
print("X =\n", X)
print("Where\nx =",X[0],"\ny =",X[1],"\nz =",X[2])
