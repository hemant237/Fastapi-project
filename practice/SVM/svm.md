# Support Vector Machine (SVM)

## 1. What is SVM?
- SVM is a supervised machine learning algorithm mainly used for classification.
- It finds a decision boundary (hyperplane) that separates different classes.
- Main objective: maximize the margin between the classes.

---

## 2. Decision Boundary
- The line/plane that separates the classes.
- Linear SVM → straight decision boundary.
- Kernel SVM → can create nonlinear decision boundaries.

---

## 3. Margin
- Margin = distance between the decision boundary and the closest training points.
- SVM tries to maximize the margin.
- Larger margin generally helps generalization.

For a linear SVM:

Margin width = 2 / ||w||

---

## 4. Support Vectors
- Support vectors are the critical training points closest to the decision boundary.
- They determine the margin and strongly influence the decision boundary.
- Moving a support vector can change the decision boundary.
- Distant points generally have much less influence.

---

## 5. Hard Margin
- Requires all training points to be correctly classified.
- No margin violations are allowed.
- Can be sensitive to noise and outliers.

---

## 6. Soft Margin
- Allows some classification errors/margin violations.
- More practical for real-world noisy data.
- Controlled mainly by the C parameter.

---

## 7. C Parameter
C controls how strongly classification errors are penalized.

### Low C
- More tolerant of errors.
- More regularization.
- Generally prefers a wider margin.
- Can cause underfitting if too low.

### High C
- Errors are penalized more strongly.
- Model tries harder to classify training points correctly.
- Can lead to a more flexible model.
- Higher overfitting risk.

Memory:
Low C  → "Some mistakes are okay."
High C → "I don't want mistakes."

---

## 8. Kernels
Kernels allow SVM to handle nonlinear relationships.

### Linear
kernel="linear"
- Used when data is approximately linearly separable.

### Polynomial
kernel="poly"
- Creates polynomial/nonlinear relationships.

### RBF
kernel="rbf"
- Radial Basis Function.
- Commonly used for nonlinear data.
- Can create complex nonlinear boundaries.

### Sigmoid
kernel="sigmoid"
- Uses a sigmoid transformation.

---

## 9. Kernel Trick
- Instead of explicitly creating many new features, the kernel allows SVM to operate as if the data were transformed into a higher-dimensional feature space.
- This can make nonlinear separation possible.

---

## 10. Gamma
Gamma controls how local the influence of individual points is when using the RBF kernel.

### Low gamma
- Larger influence area.
- Smoother decision boundary.
- Simpler model.
- Higher bias / lower variance.
- Too low → possible underfitting.

### High gamma
- Smaller influence area.
- More local patterns.
- More complex decision boundary.
- Lower bias / higher variance.
- Too high → possible overfitting.

Memory:
Low gamma  → Look broadly.
High gamma → Look locally.

---

## 11. C vs Gamma

C:
→ "How much do I care about classification errors?"

Gamma:
→ "How local should each point's influence be?"

Both can affect model complexity, so they are commonly tuned together.

---

## 12. Bias-Variance Connection

Low gamma:
→ simpler boundary
→ higher bias
→ lower variance

High gamma:
→ complex boundary
→ lower bias
→ higher variance
→ overfitting risk

---

## 13. Decision Function

SVM can produce decision scores using:

y_scores = model.decision_function(X_test)

- Negative score → Class 0 side
- Positive score → Class 1 side
- Larger positive value → stronger Class 1 side
- More negative value → stronger Class 0 side
- Score around 0 → close to decision boundary

Example:

[-2.5, -0.8, 0.2, 3.1]

3.1 → strongest Class 1 score.

---

## 14. ROC-AUC with SVM

Use decision scores instead of hard predictions:

y_scores = model.decision_function(X_test)

auc = roc_auc_score(y_test, y_scores)

ROC curve:
- X-axis → False Positive Rate (FPR)
- Y-axis → True Positive Rate (TPR)

AUC = Area Under the ROC Curve.

---

## 15. Feature Scaling

SVM is sensitive to feature scale because it relies on distances/margins.

Therefore, scaling is generally important.

Example:

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

Important:
- fit_transform() → training data
- transform() → test data
- Never fit the scaler separately on the test set.

---

## 16. GridSearchCV

Used to find good hyperparameter combinations.

Example:

param_grid = {
    "C": [0.1, 1, 10, 100],
    "gamma": [0.001, 0.01, 0.1, 1],
    "kernel": ["rbf"]
}

4 C values × 4 gamma values = 16 combinations.

With cv=5:
- Each combination is evaluated using 5-fold cross-validation.
- Average CV performance is used to compare combinations.

---

## 17. Correct ML Workflow

Training data
↓
Cross-validation
↓
Tune C + gamma + kernel
↓
Select best parameters
↓
Final model
↓
Untouched test set
↓
Final evaluation

Do NOT repeatedly select hyperparameters using test-set accuracy.

---

## 18. Important SVM Formula

Linear decision boundary:

wᵀx + b = 0

Margin boundaries:

wᵀx + b = +1
wᵀx + b = -1

Margin width:

2 / ||w||

---

## 19. Main Advantages
- Effective for classification.
- Works well in high-dimensional spaces.
- Can model nonlinear relationships using kernels.
- Margin-based approach can provide good generalization.

## 20. Main Limitations
- Can become computationally expensive on very large datasets.
- Sensitive to feature scaling.
- Choosing the right kernel and hyperparameters can require experimentation.
- High C/gamma combinations can lead to overfitting.

---

# ⭐ SVM One-Minute Revision

SVM:
→ Find a separating boundary.

Margin:
→ Distance from boundary to closest points.

Support vectors:
→ Critical points defining the margin.

C:
→ Controls penalty for errors.

Kernel:
→ Handles different types of relationships/boundaries.

RBF:
→ Common nonlinear kernel.

Gamma:
→ Controls how local each point's influence is.

GridSearchCV:
→ Tunes hyperparameters using cross-validation.

decision_function():
→ Gives continuous SVM scores.

ROC-AUC:
→ Can be calculated using decision scores.