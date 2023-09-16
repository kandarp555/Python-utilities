import pandas as pd
df = pd.read_csv("Task.csv")
print("1.")
print(df)
print("2.")
print(df[["Year","Value"]])
print("3.")
print(df.loc[0:1,:])