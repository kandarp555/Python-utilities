# Write a program to take a 3*3 array (matrix) from the user
# and calculate its transpose as well as determinant. Also,
# find whether the matrix is invertible; if yes, find the
# inverse of the matrix.
import numpy as np

lst = []
row = int(input("Enter the number of rows for matrix:\n"))
column = int(input("Enter the number of columns for matrix:\n"))
print("Enter the elements row wise:")
for i in range(0, row * column):
    if i % column == 0:
        print()
    elem = int(input())
    lst.append(elem)
matrix = np.array(lst).reshape(row, column)
print("Matrix:\n", matrix)
matrix1 = np.transpose(matrix)
print("Transpose of Matrix:\n", matrix1)
print("Determinant:\n", np.linalg.det(matrix))
if np.linalg.det(matrix) != 0:
    print("\nMatrix is invertible\n")
    print("Inverse of the matrix:\n", np.linalg.inv(matrix))
else:
    print("Matrix is not invertible")
