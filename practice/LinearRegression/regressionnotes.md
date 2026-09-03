# Regression error metrics:
#
# MAE  = mean(|actual - predicted|)
# MSE  = mean((actual - predicted)^2)
# RMSE = sqrt(MSE)
#
# MAE → easier interpretation, less sensitive to outliers
# MSE → strongly penalizes large errors
# RMSE → same units as target


# R² (R-squared):
# Measures how much variation in the target is explained
# by the regression model.
#
# R² = 1 → perfect fit
# R² = 0 → no better than predicting the mean
# R² < 0 → worse than the mean baseline

# KFold cross Validation Method 
# WE Split the data into some equal parts and test the model on every part 
# so every part gets tested and others get trained 

# Feature Scaling:
# Makes numerical features comparable in scale.
#
# Standardization:
# Mean ≈ 0, Standard deviation ≈ 1
# Formula: (x - mean) / std
#
# Normalization:
# Commonly scales values to [0, 1]
#
# Important:
# fit scaler only on training data.
# Use transform() on test data.