#Self Multiplex
import numpy as np
lst = []
row = int(input("Enter the number of row:\n"))
column = int(input("Enter the number of column:\n"))
print("Enter the elements row wise")
for i in range(0,row*column):
    if i%column == 0:
        print()
    x = int(input())
    lst.append(x)
matrix = np.array(lst).reshape(row,column)
print("Matrix:\n",matrix)
print("Self multiplex:\n",np.dot(matrix,matrix))