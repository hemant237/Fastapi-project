# PCA — Principal Component Analysis

## 1. What is PCA?

PCA stands for **Principal Component Analysis**.

PCA is an **unsupervised dimensionality reduction technique**.

It is used to reduce the number of features/dimensions in a dataset while trying to preserve as much important variation (information) as possible.

Example:

4 features
    ↓
   PCA
    ↓
2 Principal Components

Instead of working with:

- Feature 1
- Feature 2
- Feature 3
- Feature 4

we can work with:

- PC1
- PC2

---

## 2. Why do we use PCA?

PCA can be useful when a dataset has many features.

Problems with high-dimensional data:

- Difficult to visualize
- More computationally expensive
- Features may contain redundant information
- High-dimensional data can be harder to analyze

PCA can reduce:

100 features
    ↓
10 components

while retaining a large percentage of the important variation.

---

## 3. PCA does NOT simply select features

This is very important.

PCA does not simply choose the most important original features.

For example, if we have:

- Feature 1
- Feature 2
- Feature 3
- Feature 4

PCA creates new features called **Principal Components**.

Conceptually:

PC1 = combination of Feature 1 + Feature 2 + Feature 3 + Feature 4

PC2 = another combination of Feature 1 + Feature 2 + Feature 3 + Feature 4

Therefore:

Original features
        ↓
   Transformation
        ↓
Principal Components

The principal components are new dimensions created from combinations of the original features.

---

# 4. Principal Components

The new dimensions created by PCA are called **Principal Components**.

They are normally represented as:

PC1
PC2
PC3
PC4
...

### PC1

PC1 captures the maximum possible variance in the data.

### PC2

PC2 captures the maximum remaining variance while being orthogonal to PC1.

Then:

PC3
PC4
...

continue capturing the remaining variation.

Generally:

PC1 → most variance
PC2 → second most variance
PC3 → third most variance
...

---

# 5. Variance

Variance tells us how much the values vary.

Example:

A = [5, 5, 5, 5, 5]

There is almost no variation.

But:

B = [1, 5, 10, 20, 30]

has much more variation.

PCA looks for directions in the data where the variation is large.

---

# 6. Intuition of PCA

Imagine data points forming a diagonal pattern:

             ●
          ●
       ●
    ●
 ●

The data has a strong direction from bottom-left to top-right.

PCA tries to find that direction.

That direction becomes:

PC1

Another direction perpendicular to it becomes:

PC2

So PCA effectively transforms/rotates the coordinate system to find directions containing the most variation.

---

# 7. PCA vs Clustering

PCA and clustering are different techniques.

### K-Means

Used for clustering.

Question:

"Which observations belong together?"

### Hierarchical Clustering

Used for clustering.

Question:

"Which observations/clusters are similar?"

### DBSCAN

Used for density-based clustering.

Question:

"Where are the dense regions?"

### PCA

Used for dimensionality reduction.

Question:

"Can I represent high-dimensional data using fewer dimensions while preserving important variation?"

Therefore:

K-Means      → Clustering
Hierarchical → Clustering
DBSCAN       → Clustering
PCA          → Dimensionality Reduction

---

# 8. Dataset Used for PCA Practice

We used the Iris dataset.

The Iris dataset contains 150 observations and 4 numerical features:

- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)

The target contains three classes:

0
1
2

Feature matrix:

X.shape

Output:

(150, 4)

Meaning:

150 observations
4 features

---

# 9. Step 1 — Load the Iris Dataset

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris(as_frame=True)

df = iris.frame

df.head()

10. Step 2 — Separate Features and Target
X = df.drop("target", axis=1)y = df["target"]


Here:
X → input features
y → target/classes
Important:
PCA is unsupervised, so PCA itself does not use y.
11. Step 3 — Standardize the Features
Standardization is important before PCA.
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()X_scaled = scaler.fit_transform(X)


Check the shape:
X_scaled.shape


Output:
(150, 4)
Why standardize?
PCA is based on variance.
If features have different scales, a feature with a larger scale can have a larger influence.
Standardization puts the features onto a comparable scale.
12. Step 4 — Import PCA
from sklearn.decomposition import PCA


Create PCA:
pca = PCA(    n_components=2)


Here:
n_components=2
means:
Reduce the original 4 features to 2 principal components.
13. Step 5 — Fit and Transform
X_pca = pca.fit_transform(X_scaled)


Check:
print(X_pca.shape)


Output:
(150, 2)
Before PCA:
150 × 4
After PCA:
150 × 2
So dimensionality was reduced from 4 dimensions to 2 dimensions.
14. PCA Data
Example:
print(X_pca[:5])


Output is approximately:
[
[-2.2647,  0.4800],
[-2.0810, -0.6741],
[-2.3642, -0.3419],
[-2.2994, -0.5974],
[-2.3898,  0.6468]
]
These numbers are NOT the original features.
Column 1 → PC1
Column 2 → PC2
For example:
[-2.2647, 0.4800]
means:
PC1 = -2.2647
PC2 = 0.4800
15. Explained Variance
One of the most important PCA concepts is explained variance.
Explained variance tells us how much of the total variation in the original data is captured by each principal component.
We can check it using:
print(pca.explained_variance_ratio_)


For our Iris dataset:
[0.72962445 0.22850762]

Meaning:
PC1 → 72.96%
PC2 → 22.85%
Together:
72.96% + 22.85%
= 95.81%
16. Total Explained Variance
print(    pca.explained_variance_ratio_.sum())


Output:
0.9581320720000166

Approximately:
95.81%
Therefore:
4 original features
    ↓
2 principal components
    ↓
95.81% variance retained
17. Explained Variance of All Components
To see all components:
pca_full = PCA()X_pca_full = pca_full.fit_transform(X_scaled)explained_variance = pca_full.explained_variance_ratio_print("Explained Variance:")print(explained_variance)


Our result:
PC1 → 0.72962445
PC2 → 0.22850762
PC3 → 0.03668922
PC4 → 0.00517871

In percentage:
PC1 → 72.962%
PC2 → 22.851%
PC3 → 3.669%
PC4 → 0.518%
18. Cumulative Explained Variance
Cumulative explained variance tells us how much variance is retained when we keep multiple components.
print(    pca_full.explained_variance_ratio_.cumsum())


Our result:
PC1                  → 72.96%
PC1 + PC2            → 95.81%
PC1 + PC2 + PC3      → 99.48%
PC1 + PC2 + PC3 + PC4 → 100%

In decimal form:
[0.72962445
 0.95813207
 0.99482129
 1.00000000]

19. Choosing the Number of Components
We can choose the number of components based on the amount of variance we want to retain.
For example, if we want at least 95% variance:
PC1 → 72.96% ❌
PC1 + PC2 → 95.81% ✅
Therefore:
2 components are enough to retain more than 95% variance.
20. PCA with n_components=0.95
Instead of manually deciding the number of components, we can tell PCA to retain 95% of the variance.
pca_95 = PCA(    n_components=0.95)X_pca_95 = pca_95.fit_transform(X_scaled)


Check:
print(X_pca_95.shape)


Output:
(150, 2)

Check explained variance:
print(    pca_95.explained_variance_ratio_)


Output:
[0.72962445 0.22850762]

Total:
print(    pca_95.explained_variance_ratio_.sum())


Output:
0.9581320720000166

Therefore PCA automatically selected 2 components because 2 components are enough to retain at least 95% variance.
21. PCA Visualization
We can visualize the reduced data.
import matplotlib.pyplot as pltplt.figure(figsize=(6, 4))plt.scatter(    X_pca[:, 0],    X_pca[:, 1],    c=y,    s=50)plt.xlabel("PC1")plt.ylabel("PC2")plt.title("Iris Data After PCA")plt.show()


Here:
X_pca[:, 0]


means:
Take every row from column 0 → PC1
And:
X_pca[:, 1]


means:
Take every row from column 1 → PC2
The target y is only used to color the observations.
PCA itself does NOT use y.
22. PCA Components / Loadings
We can inspect how the original features contribute to each principal component.
print(pca.components_)


Our result was:
[
 [ 0.52106591, -0.26934744,  0.58041310,  0.56485654],
 [ 0.37741762,  0.92329566,  0.02449161,  0.06694199]
]

The columns correspond to:
1. sepal length
2. sepal width
3. petal length
4. petal width
Conceptually:
                         PC1        PC2

sepal length           0.521      0.377
sepal width           -0.269      0.923
petal length           0.580      0.024
petal width            0.565      0.067

These values are called component loadings/coefficients.
A larger absolute value means that the feature contributes more strongly to that component.
23. Understanding Our Components
PC1 has relatively large contributions from:
- sepal length
- petal length
- petal width
PC2 is strongly influenced by:
- sepal width
The exact signs are not the most important thing.
PCA component directions can have their signs flipped and still represent the same underlying direction.
24. Reconstruction / Inverse Transform
After reducing:
4 dimensions
    ↓
2 dimensions
we can approximately reconstruct the original standardized data.
X_reconstructed = pca_95.inverse_transform(    X_pca_95)


Check:
print(X_reconstructed.shape)


Output:
(150, 4)

The reconstructed data has 4 columns because we are reconstructing the original feature space.
25. Original vs Reconstructed Data
Example:
Original:
[-0.90068117,
  1.01900435,
 -1.34022653,
 -1.31544430]

Reconstructed:
[-0.99888895,
  1.05319838,
 -1.30270654,
 -1.24709825]

They are close but not identical.
Why?
Because we kept only:
PC1 + PC2 = 95.81% variance
and discarded:
PC3 + PC4 = approximately 4.19% variance.
Therefore reconstruction is an approximation.
26. If We Keep All Components
If we keep all 4 components:
pca = PCA(n_components=4)


we retain:
100% variance.
The inverse transformation will then approximately reproduce the original standardized data.
27. Complete PCA Workflow
The complete practical workflow is:
Load dataset
      ↓
Separate X and y
      ↓
Select numerical features
      ↓
Standardize features
      ↓
Create PCA
      ↓
Fit + Transform
      ↓
Check number of components
      ↓
Check explained variance
      ↓
Check cumulative explained variance
      ↓
Choose number of components
      ↓
Visualize PC1 vs PC2
      ↓
Inspect components/loadings
      ↓
Inverse transform if required

28. Complete PCA Practice Code
from sklearn.datasets import load_irisimport pandas as pdimport matplotlib.pyplot as pltfrom sklearn.preprocessing import StandardScalerfrom sklearn.decomposition import PCA# Load datasetiris = load_iris(as_frame=True)df = iris.frame# Separate features and targetX = df.drop("target", axis=1)y = df["target"]# Standardizescaler = StandardScaler()X_scaled = scaler.fit_transform(X)# PCA — retain 95% variancepca_95 = PCA(    n_components=0.95)X_pca = pca_95.fit_transform(X_scaled)# Check shapeprint("Original Shape:", X.shape)print("PCA Shape:", X_pca.shape)


29. Important PCA Points to Remember
1. PCA is a dimensionality reduction technique.
2. PCA is unsupervised.
3. PCA creates new features/components rather than simply selecting original features.
4. PC1 captures the maximum variance.
5. PC2 captures the maximum remaining variance while being orthogonal to PC1.
6. PCA is sensitive to feature scale, so standardization is usually important.
7. explained_variance_ratio_ tells us how much variance each component explains.
8. .cumsum() gives cumulative explained variance.
9. n_components=0.95 tells PCA to keep enough components to retain at least 95% variance.
10. PCA can be useful for visualization because it can reduce many dimensions to 2 or 3.
11. PCA does not use the target variable.
12. PCA does not perform clustering.
13. Inverse transformation reconstructs an approximation of the original data.
14. If components are discarded, reconstruction will not be exactly identical to the original data.
15. PCA can help reduce computational complexity and remove some redundant information.
30. Our Iris PCA Result
Original:
150 observations
4 features

After PCA:
150 observations
2 components

Variance:
PC1 → 72.96%
PC2 → 22.85%

Total:
95.81%

Therefore:
4 dimensions
      ↓
     PCA
      ↓
2 dimensions
      ↓
95.81% variance retained