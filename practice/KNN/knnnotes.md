# K-Nearest Neighbors (KNN)

## 1. What is KNN?

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm.

It makes predictions based on the closest training examples.

For classification:
- Find the K nearest data points.
- Count the classes of those points.
- Predict the majority class.

For regression:
- Find the K nearest data points.
- Take the average of their target values.

---

## 2. How KNN Works

For a new data point:

1. Calculate the distance between the new point and training points.
2. Sort the points based on distance.
3. Select the K nearest points.
4. Classification → majority voting.
5. Regression → average of neighbors.
6. Return the prediction.

Example:

K = 5

Nearest neighbors:
- Class A → 3
- Class B → 2

Prediction → Class A

---

## 3. K in KNN

K represents the number of neighbors used for prediction.

Small K:
- More flexible model
- Low bias
- High variance
- Sensitive to individual points
- Higher risk of overfitting

Large K:
- Smoother model
- Higher bias
- Lower variance
- Less sensitive to individual points
- Higher risk of underfitting

Important:

Small K → High Variance → Overfitting

Large K → High Bias → Underfitting

---

## 4. Distance Metrics

KNN uses distance to find the nearest neighbors.

Common distance metrics:

- Euclidean Distance
- Manhattan Distance

---

## 5. Euclidean Distance

Euclidean distance represents the straight-line distance between two points.

Formula:

d = sqrt(sum((x_i - y_i)^2))

For two dimensions:

d = sqrt((x1 - y1)^2 + (x2 - y2)^2)

Example:

A = (2, 3)
B = (5, 7)

d = sqrt((5 - 2)^2 + (7 - 3)^2)

d = sqrt(9 + 16)

d = sqrt(25)

d = 5

---

## 6. Manhattan Distance

Manhattan distance calculates distance by summing the absolute differences between dimensions.

Formula:

d = sum(|x_i - y_i|)

For two dimensions:

d = |x1 - y1| + |x2 - y2|

Example:

A = (2, 3)
B = (7, 9)

d = |7 - 2| + |9 - 3|

d = 5 + 6

d = 11

---

## 7. Euclidean vs Manhattan

Euclidean:
- Measures straight-line distance.
- Uses squared differences.
- Takes the square root.

Manhattan:
- Measures distance along each dimension.
- Uses absolute differences.
- Does not square the differences.

The best distance metric depends on the dataset.

---

## 8. Feature Scaling

Feature scaling is very important for KNN.

KNN is distance-based, so features with larger numerical ranges can dominate the distance.

Example:

Age:
20–60

Salary:
20,000–200,000

Salary has a much larger numerical scale and can dominate the distance calculation.

Therefore, scaling is usually applied before KNN.

---

## 9. Standardization

A common scaling method is StandardScaler.

Formula:

z = (x - mean) / standard deviation

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
