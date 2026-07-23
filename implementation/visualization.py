import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/stocks.csv")

plt.plot(df["Close"])
plt.title("Stock Closing Price")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()