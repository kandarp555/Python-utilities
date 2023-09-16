# Write a program using NumPy to multiply two user-defined
# matrices of size n*n where n > 2.
import numpy as np

lst1 = []
lst2 = []
lst3 = []
row1 = int(input("Enter the number of rows for matrix1:\n"))
column1 = int(input("Enter the number of columns for matrix1:\n"))
print("Enter the elements row wise:")
for i in range(0, row1 * column1):
    if i % column1 == 0:
        print()
    elem1 = int(input())
    lst1.append(elem1)
matrix1 = np.array(lst1).reshape(row1, column1)
print("\nMatrix1:\n", matrix1)
row2 = int(input("\nEnter the number of rows for matrix2:\n"))
column2 = int(input("Enter the number of columns for matrix2:\n"))
print("Enter the elements row wise:")
for i in range(0, row2 * column2):
    if i % column2 == 0:
        print()
    elem2 = int(input())
    lst2.append(elem2)
matrix2 = np.array(lst2).reshape(row2, column2)
print("\nMatrix2:\n", matrix2)
res = np.dot(matrix1, matrix2)
print("\nMultiplication of two matrices:\n", res)
