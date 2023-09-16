# Write a program to calculate element-wise difference
# between the neighboring elements of a given array.
import numpy as np
lst = []
num = int(input("How many numbers do you want to add into array:\n"))
for i in range(0,num):
    x = int(input("Enter the number:\n"))
    lst.append(x)
print()
print(lst)
print("\nElement wise difference between the neighboring element:")
print(np.diff(lst))