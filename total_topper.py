import pandas as pd
import numpy as np

df = pd.read_csv("data.txt", sep=",")
print(df)

df["total"] = df[["Math", "Physics", "Chemistry", "English"]].sum(axis=1)
print(df)

total = df[["Name", "total"]]
sorted_total = total.sort_values(ascending=False, by="total")
topper = sorted_total.iloc[0]
print(f"The overall topper is {topper['Name']} with total marks {topper['total']}")