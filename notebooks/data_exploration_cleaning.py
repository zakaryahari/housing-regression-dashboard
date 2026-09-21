import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/House_Prices.csv")

print(df.shape)
print(df.info())
df = df.drop(columns=['Id'])
print(df)

# print(df.isna().sum())

df["MSSubClass"] = df["MSSubClass"].astype(str)
df["MoSold"] = df["MoSold"].astype(str)
df["YrSold"] = df["YrSold"].astype(str)

missing = df.isnull().sum()
missing = missing[missing > 0]

cols_to_none = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 
                'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 
                'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
                'BsmtFinType2', 'MasVnrType']

cols_to_zero = ['GarageYrBlt', 'GarageArea', 'GarageCars', 'BsmtFinSF1', 
                'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 
                'BsmtHalfBath', 'MasVnrArea']


for col in missing.index:
    if col in cols_to_none:
        df[col] = df[col].fillna("None")
    elif col in cols_to_zero:
        df[col] = df[col].fillna(0)
    elif col == "LotFrontage":
        df[col] = df[col].fillna(df.groupby("Neighborhood")[col].transform("median"))
    else :
        df[col] = df[col].fillna(df[col].mode()[0])

print(df.isnull().sum().sum())

# plt.bar(
#     x= df['GrLivArea'],
#     y=df['SalePrice']
# )

plt.scatter(df['GrLivArea'], df['SalePrice'])

plt.title("GrLivArea / SalePrice",fontsize=16)
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")

plt.show()

out_values = (df['GrLivArea'] > 4000) & (df['SalePrice'] < 300000)
df = df[~out_values]




plt.scatter(df['GrLivArea'], df['SalePrice'])

plt.title("GrLivArea / SalePrice",fontsize=16)
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")

plt.show()


