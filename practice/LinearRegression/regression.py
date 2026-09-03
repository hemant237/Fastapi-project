import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 55, 60, 65, 70])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Model parameters
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Prediction
prediction = model.predict([[6]])

print("Prediction:", prediction[0])

y_pred = model.predict(X)

print("Actual:", y)
print("Predicted:", y_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

A = np.array([[1], [2], [3], [4], [5]])
b = np.array([52, 54, 63, 64, 72])

model = LinearRegression()

model.fit(A, b)

y_pred = model.predict(A)

print("Actual:", b)
print("Predicted:", y_pred)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(b, y_pred)
mse = mean_squared_error(b, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

from sklearn.metrics import r2_score

r2 = r2_score(b, y_pred)
print("R²:", r2)