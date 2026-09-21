import pandas as pd

df = pd.read_csv("data/raw/House_Prices.csv")

print(df.shape)
print(df.info())
df = df.drop(columns=['Id'])
print(df)
