import pandas as pd

df = pd.read_csv("data/raw/House_Prices.csv")

print(df.shape)
print(df.info())
df = df.drop(columns=['Id'])
print(df)

# print(df.isna().sum())

df["MSSubClass"] = df["MSSubClass"].astype(str)
df["MoSold"] = df["MoSold"].astype(str)
df["YrSold"] = df["YrSold"].astype(str)

# print(df.info())

missing = df.isnull().sum()

print(missing[missing > 0])