# Write a program to create a 5*5 array with random values
# and find the minimum and maximum values using NumPy.
import numpy as np
print("5*5 array with random values:\n")
arr = np.random.randint(50,size=(5,5))
print(arr)
print("\nMaximum value from the array:",arr.max())
print("Minimum value from the array:",arr.min())