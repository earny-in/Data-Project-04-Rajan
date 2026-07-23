import pandas as pd

df = pd.read_csv("data/stocks.csv")

print(df.info())
print()
print(df.describe())