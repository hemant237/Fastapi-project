#  XGBoost — Complete Notes

## 1. What is XGBoost?

XGBoost stands for:

> **Extreme Gradient Boosting**

XGBoost is an optimized and regularized implementation of Gradient Boosting.

It builds decision trees sequentially, where each new tree tries to improve the existing model.

Basic idea:

    Current Model
          ↓
    Calculate Loss
          ↓
    Find what needs correction
          ↓
    Build Next Tree
          ↓
    Add Correction
          ↓
    Repeat
          ↓
    Final Model

XGBoost builds on the Gradient Boosting concept but adds additional techniques for:

- Regularization
- Optimization
- Tree complexity control
- Row subsampling
- Feature subsampling
- Efficient training

---

# 2. Gradient Boosting vs XGBoost

## Gradient Boosting

Main idea:

> Sequentially add trees to reduce the loss.

## XGBoost

Main idea:

> Sequentially add trees to reduce the loss while explicitly controlling model complexity and optimizing the training process.

Think:

    Gradient Boosting
          ↓
    Sequential trees
          ↓
    XGBoost
          ↓
    Sequential trees
    +
    Regularization
    +
    Optimization
    +
    Subsampling
    +
    Complexity control

---

# 3. XGBoost and Overfitting

Like other tree-based algorithms, XGBoost can overfit.

For example:

    Very complex trees
          ↓
    Model learns training data extremely well
          ↓
    Model starts learning noise
          ↓
    Poor generalization
          ↓
    Overfitting

XGBoost provides several controls to reduce this risk.

Important controls include:

- `max_depth`
- `gamma`
- `min_child_weight`
- `subsample`
- `colsample_bytree`
- `reg_alpha`
- `reg_lambda`
- `learning_rate`
- `n_estimators`
- Early stopping

---

# 4. Objective Function

One of the most important concepts in XGBoost is the objective function.

Basic idea:

$$
\boxed{Objective = Loss + Regularization}
$$

The model tries to minimize the objective.

---

# 5. Loss

Loss measures how wrong the model's predictions are.

For classification, XGBoost commonly uses log loss.

If predictions are poor:

$$
Loss \uparrow
$$

If predictions improve:

$$
Loss \downarrow
$$

The model tries to minimize the loss.

---

# 6. Regularization

Regularization penalizes unnecessary model complexity.

So XGBoost doesn't simply ask:

> How can I reduce prediction error?

It asks:

> How can I reduce prediction error while also controlling model complexity?

Therefore:

$$
\boxed{Objective = Prediction\ Loss + Complexity\ Penalty}
$$

---

# 7. Objective Function Example

Suppose we have:

    Model A

    Loss = 10
    Regularization = 8

Then:

$$
Objective=10+8=18
$$

Now:

    Model B

    Loss = 12
    Regularization = 2

Then:

$$
Objective=12+2=14
$$

Therefore:

$$
14<18
$$

Model B has the lower objective.

Important:

> A model with slightly higher loss can still have a lower overall objective if its complexity penalty is much smaller.

---

# 8. `gamma`

`gamma` controls the minimum loss reduction required to make a split.

Basic idea:

> Is this split worth the additional complexity?

Conceptually:

$$
\boxed{\gamma = Minimum\ loss\ reduction\ required\ for\ a\ split}
$$

If a potential split gives an improvement smaller than `gamma`, the split can be rejected.

---

# 9. Gamma Example

Suppose a potential split provides an improvement of:

$$
4
$$

### Case 1

    gamma = 2

Since:

$$
4>2
$$

The improvement is sufficient.

The split can be made.

### Case 2

    gamma = 6

Since:

$$
4<6
$$

The improvement is not sufficient.

The split can be rejected.

Therefore:

$$
\boxed{Higher\ gamma \rightarrow More\ conservative\ splitting}
$$

Memory trick:

> `gamma` = "Is this split worth it?"

---

# 10. `max_depth`

`max_depth` controls how deep each decision tree can grow.

Example:

    max_depth = 1

creates a very simple tree.

    max_depth = 10

allows a much deeper and more complex tree.

Therefore:

$$
\boxed{Higher\ max\_depth \rightarrow More\ potential\ complexity}
$$

and:

$$
\boxed{Lower\ max\_depth \rightarrow Simpler\ trees}
$$

---

# 11. max_depth and Overfitting

If trees are allowed to become extremely deep:

    max_depth ↑
          ↓
    More complex trees
          ↓
    Can learn very specific patterns
          ↓
    Higher overfitting risk

If trees are too shallow:

    max_depth ↓
          ↓
    Very simple trees
          ↓
    May fail to capture important patterns
          ↓
    Underfitting

Therefore, `max_depth` needs to be chosen appropriately.

---

# 12. `min_child_weight`

`min_child_weight` controls the minimum amount of accumulated weight/information required in a child node before a split is allowed.

For the usual tree objective, it is based on the sum of the instance weights (Hessian values) in the child node, rather than simply the number of rows.

Basic idea:

    min_child_weight ↓
          ↓
    Splits are easier
          ↓
    More complex trees possible

While:

    min_child_weight ↑
          ↓
    Splits become harder
          ↓
    More conservative model

Therefore:

$$
\boxed{Higher\ min\_child\_weight \rightarrow More\ conservative\ splitting}
$$

---

# 13. Difference Between max_depth, gamma and min_child_weight

| Parameter | Main question |
|---|---|
| `max_depth` | How deep can the tree go? |
| `gamma` | Is this split worth the improvement? |
| `min_child_weight` | Does the child node have enough weight/information? |

Memory:

    max_depth
    → How deep?

    gamma
    → Is the split worth it?

    min_child_weight
    → Does the child have enough information?

---

# 14. `subsample`

`subsample` controls the fraction of training rows used for each boosting iteration/tree.

Example:

    subsample = 0.8

means approximately:

    80% of training rows

are used for each boosting iteration.

Examples:

    subsample = 1.0
    → 100% rows

    subsample = 0.8
    → 80% rows

    subsample = 0.7
    → 70% rows

Using a fraction smaller than 1 introduces randomness and can help reduce overfitting.

---

# 15. `colsample_bytree`

`colsample_bytree` controls the fraction of features/columns used for each tree.

Example:

    Number of features = 20

    colsample_bytree = 0.5

Approximately:

$$
20\times0.5=10
$$

features are selected for the tree.

Memory:

    subsample
    → Rows

    colsample_bytree
    → Features

---

# 16. `reg_alpha`

`reg_alpha` controls **L1 regularization**.

L1 regularization penalizes model weights and can encourage some weights toward zero.

Basic idea:

    reg_alpha ↑
          ↓
    Stronger L1 regularization
          ↓
    More regularization
          ↓
    Can help reduce overfitting

Memory:

$$
\boxed{reg\_alpha=L1}
$$

---

# 17. `reg_lambda`

`reg_lambda` controls **L2 regularization**.

Basic idea:

    reg_lambda ↑
          ↓
    Stronger L2 regularization
          ↓
    More regularization
          ↓
    Can help reduce overfitting

Memory:

$$
\boxed{reg\_lambda=L2}
$$

---

# 18. L1 vs L2

| Parameter | Regularization |
|---|---|
| `reg_alpha` | L1 |
| `reg_lambda` | L2 |

Memory trick:

    alpha  → L1
    lambda → L2

Do not confuse these with `gamma`.

    gamma
    → Controls whether a split is worth making

    reg_alpha
    → L1 regularization

    reg_lambda
    → L2 regularization

---

# 19. `learning_rate`

`learning_rate` controls how much each new tree contributes to the existing model.

Suppose a new tree produces a correction of:

    10

If:

    learning_rate = 0.1

then the contribution is approximately:

$$
10\times0.1=1
$$

If:

    learning_rate = 0.5

then:

$$
10\times0.5=5
$$

Therefore:

$$
\boxed{Lower\ learning\ rate \rightarrow Smaller\ corrections}
$$

$$
\boxed{Higher\ learning\ rate \rightarrow Larger\ corrections}
$$

---

# 20. `n_estimators`

`n_estimators` controls the number of boosting rounds/trees.

Example:

    n_estimators = 100

means the model can perform 100 boosting rounds.

    n_estimators = 500

means the model can perform 500 boosting rounds.

More trees give the model more opportunities to learn corrections.

However:

> More trees do not automatically mean better test performance.

---

# 21. Learning Rate and n_estimators Relationship

There is an important relationship between:

- `learning_rate`
- `n_estimators`

Lower learning rate:

    Smaller correction per tree
          ↓
    Usually requires more trees

Higher learning rate:

    Larger correction per tree
          ↓
    May require fewer trees

Example:

    Model A:
    learning_rate = 0.01
    n_estimators = 500

    Model B:
    learning_rate = 0.1
    n_estimators = 100

Neither combination is automatically better.

The correct combination must be determined using validation.

---

# 22. Early Stopping

Early stopping allows training to stop when validation performance stops improving.

Suppose:

    n_estimators = 500

but the model reaches its best validation score at iteration 150.

If:

    early_stopping_rounds = 20

and there is no improvement for 20 consecutive rounds, training stops.

Conceptually:

    Tree 1   → Improving
    Tree 2   → Improving
    ...
    Tree 150 → Best score
    Tree 151 → No improvement
    Tree 152 → No improvement
    ...
    Tree 170 → No improvement

    20 rounds without improvement
              ↓
           Stop training

Therefore:

> `n_estimators` is the maximum number of boosting rounds, while early stopping can stop training earlier.

---

# 23. XGBoost Parameter Map

| Parameter | What it controls |
|---|---|
| `learning_rate` | Size of each tree's contribution |
| `n_estimators` | Number of boosting rounds |
| `max_depth` | Maximum tree depth |
| `gamma` | Minimum improvement required for a split |
| `min_child_weight` | Minimum child-node weight |
| `subsample` | Fraction of rows |
| `colsample_bytree` | Fraction of features |
| `reg_alpha` | L1 regularization |
| `reg_lambda` | L2 regularization |

---

# 24. XGBoost Classification in Python

Import:

    from xgboost import XGBClassifier

Create the model:

    xgb = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

Train:

    xgb.fit(X_train, y_train)

Predict classes:

    y_pred = xgb.predict(X_test)

Predict probabilities:

    y_prob = xgb.predict_proba(X_test)[:, 1]

---

# 25. Baseline XGBoost Model

Our baseline model was:

    XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

Results:

    Accuracy = 0.956140350877193

    ROC-AUC = 0.9931215198165738

Confusion Matrix:

    [[40  3]
     [ 2 69]]

---

# 26. Baseline XGBoost Classification Report

              precision    recall    f1-score    support

    Class 0      0.95      0.93       0.94        43
    Class 1      0.96      0.97       0.97        71

    Accuracy                         0.96       114

    Macro Avg     0.96      0.95       0.95       114
    Weighted Avg  0.96      0.96       0.96       114

---

# 27. XGBoost Hyperparameter Tuning

We used GridSearchCV.

Parameter grid:

    param_grid = {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [2, 3, 5],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0]
    }

GridSearchCV:

    grid_search = GridSearchCV(
        XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        ),
        param_grid,
        cv=5,
        scoring="accuracy",
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    print("Best Parameters:", grid_search.best_params_)
    print("Best CV Score:", grid_search.best_score_)

---

# 28. Important GridSearchCV Concept

We used:

    scoring="accuracy"

Therefore GridSearchCV selected the best hyperparameters based on:

$$
\boxed{Cross\text{-}Validation\ Accuracy}
$$

It did NOT select them based on test-set accuracy.

If we use:

    scoring="roc_auc"

then GridSearchCV optimizes:

$$
\boxed{Cross\text{-}Validation\ ROC\text{-}AUC}
$$

---

# 29. Correct ML Workflow

The correct workflow is:

    Training Data
          ↓
    GridSearchCV
          ↓
    Cross-Validation
          ↓
    Select Best Parameters
          ↓
    Train/Refit Final Model
          ↓
    Test Set
          ↓
    Final Evaluation

The test set should remain separate from hyperparameter selection.

---

# 30. Tuned XGBoost Results

After tuning, our model achieved:

    Accuracy = 0.9649122807017544

    ROC-AUC = 0.9931215198165739

Confusion Matrix:

    [[41  2]
     [ 2 69]]

Correct predictions:

$$
41+69=110
$$

Total test samples:

$$
114
$$

Accuracy:

$$
\frac{110}{114}
=
0.964912
$$

Therefore:

$$
\boxed{Accuracy=96.49\%}
$$

---

# 31. Tuned XGBoost Classification Report

              precision    recall    f1-score    support

    Class 0      0.95      0.95       0.95        43
    Class 1      0.97      0.97       0.97        71

    Accuracy                         0.96       114

    Macro Avg     0.96      0.96       0.96       114
    Weighted Avg  0.96      0.96       0.96       114

---

# 32. XGBoost Baseline vs Tuned

| Metric | Baseline | Tuned |
|---|---:|---:|
| Accuracy | 95.61% | 96.49% |
| ROC-AUC | 0.9931 | 0.9931 |
| Correct Predictions | 109/114 | 110/114 |

Accuracy improved:

$$
95.61\%\rightarrow96.49\%
$$

Improvement:

$$
\boxed{0.88\ percentage\ points}
$$

ROC-AUC remained essentially unchanged.

---

# 33. Why Did Accuracy Improve?

Baseline:

    [[40  3]
     [ 2 69]]

Tuned:

    [[41  2]
     [ 2 69]]

The tuned model correctly classified one additional Class 0 sample.

Therefore:

    Baseline:
    109 correct out of 114

    Tuned:
    110 correct out of 114

This produced the accuracy improvement.

---

# 34. Comparison of Our Models

| Model | Test Accuracy | ROC-AUC |
|---|---:|---:|
| AdaBoost | 97.37% | 0.9961 |
| XGBoost — Tuned | 96.49% | 0.9931 |
| Gradient Boosting | 95.61% | 0.9951 |
| Gradient Boosting — Tuned | 94.74% | 0.9941 |

These results are specific to our dataset and this particular train/test split.

They do NOT mean that AdaBoost is always better than XGBoost or that XGBoost is always better than Gradient Boosting.

---

# 35. Important XGBoost Lessons

1. XGBoost is an optimized and regularized form of gradient boosting.
2. XGBoost builds trees sequentially.
3. Each new tree contributes to improving the existing model.
4. The objective combines loss and regularization.
5. Higher `gamma` makes splitting more conservative.
6. Higher `max_depth` allows more complex trees.
7. Higher `min_child_weight` makes splitting more conservative.
8. `subsample` controls the fraction of rows used.
9. `colsample_bytree` controls the fraction of features used.
10. `reg_alpha` is L1 regularization.
11. `reg_lambda` is L2 regularization.
12. Lower `learning_rate` generally requires more trees.
13. `n_estimators` controls the number of boosting rounds.
14. Early stopping can stop training when validation performance stops improving.
15. GridSearchCV chooses parameters based on the selected CV scoring metric.
16. The test set should be kept separate for final evaluation.
17. A more advanced algorithm does not automatically produce better results on every dataset.

---

# 36. Memory Tricks

## Tree Complexity

    max_depth
    → How deep?

    gamma
    → Is the split worth it?

    min_child_weight
    → Does the child have enough information?

## Sampling

    subsample
    → Rows

    colsample_bytree
    → Features

## Regularization

    reg_alpha
    → L1

    reg_lambda
    → L2

## Boosting

    learning_rate
    → Size of each tree's contribution

    n_estimators
    → Number of boosting rounds

## Training Control

    early_stopping_rounds
    → Stop if validation performance stops improving

---

# 37. XGBoost Overall Flow

    Training Data
          ↓
    Initial Model
          ↓
    Calculate Loss
          ↓
    Calculate Gradient
          ↓
    Build Tree
          ↓
    Control Tree Complexity
          ↓
    Apply Learning Rate
          ↓
    Add Tree
          ↓
    Check Validation Performance
          ↓
    Continue / Early Stop
          ↓
    Final XGBoost Model

---

# ⭐ Final XGBoost Cheat Sheet

    XGBoost
    → Optimized + Regularized Gradient Boosting

    Objective
    → Loss + Regularization

    max_depth
    → Tree depth

    gamma
    → Minimum improvement for split

    min_child_weight
    → Minimum child-node weight

    subsample
    → Row sampling

    colsample_bytree
    → Feature sampling

    reg_alpha
    → L1

    reg_lambda
    → L2

    learning_rate
    → Contribution of each tree

    n_estimators
    → Number of trees/boosting rounds

    early_stopping_rounds
    → Stop when validation performance stops improving

---

# 🗺️ Current ML Progress

## Completed

- [x] Linear Regression
- [x] Logistic Regression
- [x] KNN
- [x] SVM
- [x] Naive Bayes
- [x] Decision Trees
- [x] Random Forest
- [x] AdaBoost
- [x] Gradient Boosting
- [x] XGBoost

## Next

- [ ] LightGBM
- [ ] CatBoost
- [ ] Unsupervised Learning
- [ ] Dimensionality Reduction
- [ ] Remaining ML topics
- [ ] Deep Learning
- [ ] NLP
- [ ] Transformers
- [ ] LLMs
- [ ] RAG
- [ ] AI Agents
- [ ] Production AI Engineering
- [ ] Final AI Engineer Projects