import pandas as pd

df = pd.read_csv("expenses.csv")
print(df)
print(df.dtypes)
print(df["amount"].sum())