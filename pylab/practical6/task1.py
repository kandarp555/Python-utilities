import pandas as pd
from random import sample

lst = []
fle = open("life.txt", "r")
print("1.")
print(fle.read(), "\n")
print("2.")
with open("life.txt", "r") as fle:
    for j, data in enumerate(fle):
        lst.append(j)
        if j % 2 != 0:
            print("Line:", j, "Text:", data)
print("3.")
str = sample(lst, 3)
with open("life.txt", "r") as fle:
    for j, data in enumerate(fle):
        if j in str:
            print("Line:", j, "Text:", data)
print("4.")
df = pd.read_fwf("life.txt")
print(df)