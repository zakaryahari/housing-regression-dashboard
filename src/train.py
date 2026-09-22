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

from sklearn.metrics import r2_score

y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
print(f"Linear Regression R2 Score: {score}")



from sklearn.linear_model import Ridge


ridge_model = Ridge()
ridge_model.fit(X_train, y_train)


ridge_pred = ridge_model.predict(X_test)
ridge_score = r2_score(y_test, ridge_pred)
print(f'Ridge Regression R2 Score: {ridge_score}')


from sklearn.ensemble import RandomForestRegressor


rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)


rf_pred = rf_model.predict(X_test)
rf_score = r2_score(y_test, rf_pred)
print(f"Random Forest R2 Score: {rf_score}")

