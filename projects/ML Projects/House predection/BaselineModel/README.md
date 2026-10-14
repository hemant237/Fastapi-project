# House Price Prediction - Model Experiments

Target: `Price_INR_Lakhs`. All models use the same 80/20 split (`random_state=42`).

| Notebook | What it does |
|---|---|
| 20 | Linear Regression baseline |
| 21-23 | Random Forest baseline, feature importance, tuning |
| 25-26 | HistGradientBoosting baseline and first tuning |
| 27 | Early stopping, `max_leaf_nodes`, regularisation tuning |
| 28 | 5-fold cross-validation, baseline vs tuned |
| 29 | Log-transformed target experiment |
| 30 | Comparison of all models |
| 31 | Error analysis by price band and city |
| 32 | Final model trained on all data, saved to `../models/` |
| 33 | Predictions for `test.csv` -> `../submission.csv` |

## Results (validation set)

| Model | MAE (lakhs) | RMSE (lakhs) | R2 |
|---|---|---|---|
| Linear Regression | 47.94 | 86.03 | 0.6657 |
| Random Forest | 34.05 | 70.43 | 0.7760 |
| HistGB baseline | 32.85 | 68.67 | 0.7870 |
| **HistGB tuned** | **32.58** | **68.06** | **0.7908** |

Tuned parameters: `learning_rate=0.05, max_iter=500, max_leaf_nodes=15, min_samples_leaf=100, l2_regularization=1.0` (early stopping on).

5-fold CV R2: baseline 0.7842, tuned 0.7880 (tuned wins on every fold).

## Notes
- Always set `random_state` on HistGradientBoosting: with more than 10,000 rows it uses early stopping on a random validation split, so results change between runs without it.
- The log target lowered MAE but reduced R2, so the raw target is kept.
- Largest errors are on Mumbai and Delhi and on the most expensive houses.
