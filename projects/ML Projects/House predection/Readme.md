# Indian House Price Prediction

## Project Overview

This project develops a machine learning model to predict house prices using property characteristics such as city, locality type, property type, area, age, furnishing status, and available amenities.

The project uses a **synthetic Indian urban house-price dataset** and demonstrates the complete machine learning workflow, from exploratory data analysis to final predictions.

## Objectives

- Explore property features and their relationships with prices.
- Perform data quality checks and exploratory data analysis.
- Build reusable preprocessing pipelines.
- Train and compare regression models.
- Tune hyperparameters and evaluate model performance.
- Generate predictions for an unlabelled test dataset.

## Dataset

- Training dataset: 80,000 rows
- Test dataset: 20,000 rows
- Target variable: `Price_INR_Lakhs`
- Dataset type: Synthetic

The test dataset does not contain the target variable, so its prediction accuracy cannot be directly evaluated.

## Models Compared

1. Linear Regression
2. Random Forest Regressor
3. HistGradientBoosting Regressor

## Best Validation Results

The selected model was HistGradientBoostingRegressor.

| Metric | Validation Result |
|---|---:|
| R² Score | 0.7896 |
| MAE | ₹32.72 lakh |
| RMSE | ₹68.25 lakh |

These results come from a held-out validation set and are not measured test-set performance.

## Model Configuration

- Learning rate: 0.1
- Maximum iterations: 100
- Maximum leaf nodes: 15
- Random state: 42

The model uses median imputation for numerical features and most-frequent imputation plus one-hot encoding for categorical features.

## Project Workflow

1. Data understanding and quality checks
2. Exploratory data analysis
3. Feature relationship and outlier analysis
4. Train-validation split
5. Preprocessing pipelines
6. Baseline model training
7. Feature importance analysis
8. Hyperparameter tuning
9. Model comparison
10. Final training and test-set predictions
11. Prediction validation

## Output

The final prediction script generates `test_predictions.csv`, containing:

- `Property_ID`
- `Predicted_Price_INR_Lakhs`

Negative predictions are clipped to zero. This ensures non-negative outputs but does not guarantee that every prediction is realistic.

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- Matplotlib
- Seaborn

## Limitations

- The dataset is synthetic and may not represent real estate market conditions.
- Actual test-set prices are unavailable, so test-set accuracy cannot be measured.
- Validation metrics do not guarantee performance on real-world property data.
- Feature importance indicates predictive contribution, not causation.

## Future Improvements

- Evaluate the model on a reliable real-world dataset.
- Investigate prediction errors across cities and price ranges.
- Explore additional feature engineering and model tuning.
- Consider prediction intervals to communicate uncertainty.

