import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/processed/engineered_house_prices.csv")

# print(df)


y = df['SalePrice']
x = df.drop(columns='SalePrice')

print(x)
print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
