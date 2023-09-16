import pandas as pd
import numpy as np
df = pd.read_excel("Book1.xlsx",sheet_name="Sheet2")
print("1.")
print(df)
print("2.")
print(df[["House Age (years)"]])
print("3.")
df = df.assign(Added_column = np.nan)
print(df)
