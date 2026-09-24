# 🚀 LightGBM — Complete Notes

## 1. What is LightGBM?

LightGBM is a gradient boosting framework developed by Microsoft.

It is based on:

> Gradient Boosted Decision Trees (GBDT)

Basic idea:

    Decision Trees
          ↓
    Gradient Boosting
          ↓
       LightGBM

LightGBM is designed to train gradient-boosted decision trees efficiently, especially on large datasets.

Important LightGBM concepts include:

- Leaf-wise tree growth
- Histogram-based learning
- `num_leaves`
- `max_depth`
- `max_bin`
- `learning_rate`
- `n_estimators`
- `min_child_samples`
- `subsample`
- `colsample_bytree`
- `reg_alpha`
- `reg_lambda`

---

# 2. LightGBM and Gradient Boosting

LightGBM is based on Gradient Boosted Decision Trees.

The general process is:

    Initial Model
          ↓
    Calculate Loss
          ↓
    Calculate Gradient
          ↓
    Build Decision Tree
          ↓
    Add Tree to Model
          ↓
    Repeat
          ↓
    Final Model

Each new tree attempts to improve the existing model.

---

# 3. LightGBM vs Traditional Gradient Boosting

One of the important differences is how trees are grown.

Traditional gradient boosting is commonly described as:

    Level-wise / Depth-wise Growth

LightGBM uses:

    Leaf-wise Growth

This is one of the most important concepts in LightGBM.

---

# 4. Level-wise Growth

With level-wise growth, the tree expands roughly level by level.

Example:

             Root
            /    \
           A      B
          / \    / \
         C   D  E   F

The tree grows across a level before moving deeper.

---

# 5. Leaf-wise Growth

LightGBM uses leaf-wise growth by default.

Instead of expanding every branch equally, LightGBM looks at the available leaves and chooses the leaf whose split provides the largest reduction in loss.

Example:

    Leaf A → loss reduction = 2
    Leaf B → loss reduction = 8
    Leaf C → loss reduction = 4
    Leaf D → loss reduction = 5

LightGBM chooses:

    Leaf B → 8

because it provides the largest loss reduction.

Basic process:

    Find leaf with largest loss reduction
              ↓
          Split leaf
              ↓
    Find next best leaf
              ↓
          Split leaf
              ↓
            Repeat

---

# 6. Why Leaf-wise Growth is Powerful

Leaf-wise growth can reduce loss aggressively.

Instead of:

    Grow every branch equally

LightGBM asks:

> Which available leaf will give the largest improvement?

Then it grows that leaf.

This can make LightGBM very efficient and powerful.

---

# 7. Disadvantage of Leaf-wise Growth

Because LightGBM keeps growing the most promising leaf, one branch can become much deeper than another.

Example:

             Root
            /    \
         Leaf    Node
                /    \
             Leaf    Node
                    /    \
                 Leaf    Leaf

The tree can become unbalanced.

This can increase overfitting risk, particularly on smaller datasets.

Therefore, parameters such as:

- `num_leaves`
- `max_depth`
- `min_child_samples`

are important for controlling complexity.

---

# 8. `num_leaves`

`num_leaves` controls the maximum number of leaves in each tree.

Example:

    num_leaves = 4

A tree can have at most 4 leaves.

Basic idea:

    num_leaves ↑
          ↓
    More complex trees
          ↓
    Higher overfitting risk

Therefore:

    num_leaves ↓
          ↓
    Simpler trees
          ↓
    Can reduce overfitting

---

# 9. `max_depth`

`max_depth` controls the maximum depth of the tree.

Example:

    max_depth = 5

The tree cannot grow deeper than depth 5.

Basic idea:

    max_depth ↑
          ↓
    More potential complexity

    max_depth ↓
          ↓
    Simpler trees

---

# 10. max_depth and num_leaves

These two parameters control tree complexity in different ways.

    max_depth
    → How deep can the tree go?

    num_leaves
    → How many leaves can the tree have?

For a binary tree, the theoretical maximum number of leaves for a given depth is:

$$
2^{max\_depth}
$$

Example:

    max_depth = 3

Therefore:

$$
2^3 = 8
$$

So the simple theoretical maximum is:

    8 leaves

If:

    num_leaves = 15
    max_depth = 3

the depth constraint can be tighter than the leaf limit.

---

# 11. `max_bin`

LightGBM uses histogram-based learning.

`max_bin` controls the number of histogram bins used for continuous features.

Example:

    max_bin = 255

Continuous feature values are grouped into histogram bins.

Conceptually:

    Many continuous values
            ↓
       Histogram
            ↓
        Bins
            ↓
    Evaluate split candidates

---

# 12. Histogram-based Learning

Suppose a feature contains:

    10,000 unique numerical values

Instead of evaluating every possible numerical split individually, LightGBM can group values into a smaller number of bins.

Example:

    10,000 values
          ↓
    Histogram binning
          ↓
    256 bins
          ↓
    Evaluate splits using bins

This reduces the number of split candidates that need to be evaluated.

Benefits:

    Fewer split candidates
            ↓
       Less computation
            ↓
       Faster training
            ↓
       Lower memory usage

Important:

> Histogram binning improves computational efficiency; it does not automatically guarantee that the model cannot overfit.

---

# 13. Effect of max_bin

If:

    max_bin = 255

and we change it to:

    max_bin = 50

LightGBM uses fewer histogram bins.

Generally:

    Fewer bins
        ↓
    Fewer split candidates
        ↓
    Potentially less computation
        ↓
    Potentially faster training

Trade-off:

    Fewer bins
        ↓
    More coarse representation of feature values
        ↓
    Less precise split representation

---

# 14. `learning_rate`

`learning_rate` controls how much each new tree contributes to the existing model.

Example:

    learning_rate = 0.1

Each tree makes a relatively small contribution.

General relationship:

    Lower learning_rate
          ↓
    Smaller contribution per tree

    Higher learning_rate
          ↓
    Larger contribution per tree

---

# 15. `n_estimators`

`n_estimators` controls the number of boosting rounds/trees.

Example:

    n_estimators = 100

means the model can perform 100 boosting rounds.

Example:

    n_estimators = 200

means the model can perform 200 boosting rounds.

More trees give the model more opportunities to improve.

However:

> More trees do not automatically mean better test performance.

---

# 16. Learning Rate and n_estimators Relationship

There is an important relationship between:

- `learning_rate`
- `n_estimators`

Generally:

    Lower learning_rate
          ↓
    Smaller contribution per tree
          ↓
    Usually requires more trees

While:

    Higher learning_rate
          ↓
    Larger contribution per tree
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

Validation should be used to determine the better combination for a particular dataset.

---

# 17. `min_child_samples`

`min_child_samples` specifies the minimum number of data samples that a leaf should contain.

Example:

    min_child_samples = 20

means a leaf should contain at least 20 samples.

If a potential split would create a leaf containing fewer than the minimum allowed samples, that split is not allowed.

Example:

    min_child_samples = 20

    Potential new leaf = 8 samples

Since:

    8 < 20

the split is not allowed.

---

# 18. Effect of min_child_samples

Lower value:

    min_child_samples ↓
          ↓
    Smaller leaves allowed
          ↓
    More detailed trees
          ↓
    Potentially more overfitting

Higher value:

    min_child_samples ↑
          ↓
    Larger leaves required
          ↓
    More conservative trees
          ↓
    Can help reduce overfitting

Memory:

    min_child_samples
    → Minimum number of samples in a leaf

---

# 19. `subsample`

`subsample` controls the fraction of rows used for each boosting iteration.

Example:

    subsample = 0.8

means approximately 80% of the rows are used for each boosting iteration.

Examples:

    subsample = 1.0
    → approximately 100% rows

    subsample = 0.8
    → approximately 80% rows

    subsample = 0.7
    → approximately 70% rows

Using a value below 1 can introduce randomness and may help reduce overfitting.

---

# 20. `colsample_bytree`

`colsample_bytree` controls the fraction of features used for each tree.

Example:

    Number of features = 20

    colsample_bytree = 0.5

Approximately:

$$
20 \times 0.5 = 10
$$

features are used.

Memory:

    subsample
    → ROWS

    colsample_bytree
    → FEATURES

---

# 21. Example of Subsampling

Suppose:

    Rows = 1000
    Features = 20

and:

    subsample = 0.7
    colsample_bytree = 0.5

Rows:

$$
1000 \times 0.7 = 700
$$

Features:

$$
20 \times 0.5 = 10
$$

Therefore approximately:

    700 rows
    10 features

are used for the respective boosting iteration/tree.

---

# 22. `reg_alpha`

`reg_alpha` controls L1 regularization.

Memory:

    reg_alpha → L1

Increasing it strengthens the L1 regularization penalty.

General idea:

    reg_alpha ↑
          ↓
    Stronger L1 regularization
          ↓
    Can help control overfitting

---

# 23. `reg_lambda`

`reg_lambda` controls L2 regularization.

Memory:

    reg_lambda → L2

Increasing it strengthens L2 regularization.

General idea:

    reg_lambda ↑
          ↓
    Stronger L2 regularization
          ↓
    Can help control overfitting

---

# 24. L1 vs L2

| Parameter | Regularization |
|---|---|
| `reg_alpha` | L1 |
| `reg_lambda` | L2 |

Memory:

    alpha  → L1

    lambda → L2

---

# 25. LightGBM Parameter Map

| Parameter | What it controls |
|---|---|
| `num_leaves` | Maximum number of leaves |
| `max_depth` | Maximum tree depth |
| `max_bin` | Histogram bins |
| `learning_rate` | Contribution of each tree |
| `n_estimators` | Number of boosting rounds |
| `min_child_samples` | Minimum samples in a leaf |
| `subsample` | Fraction of rows |
| `colsample_bytree` | Fraction of features |
| `reg_alpha` | L1 regularization |
| `reg_lambda` | L2 regularization |

---

# 26. LightGBM Classification in Python

Import:

    from lightgbm import LGBMClassifier

Create model:

    lgbm = LGBMClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42,
        verbosity=-1
    )

Train:

    lgbm.fit(X_train, y_train)

Predict classes:

    y_pred = lgbm.predict(X_test)

Predict probabilities:

    y_prob = lgbm.predict_proba(X_test)[:, 1]

---

# 27. Baseline LightGBM Model

Our baseline model was:

    LGBMClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42,
        verbosity=-1
    )

Results:

    Accuracy = 0.956140350877193

    ROC-AUC = 0.9941041598427777

Confusion Matrix:

    [[39  4]
     [ 1 70]]

---

# 28. Baseline LightGBM Classification Report

              precision    recall    f1-score    support

    Class 0      0.97      0.91       0.94        43
    Class 1      0.95      0.99       0.97        71

    Accuracy                         0.96       114

    Macro Avg     0.96      0.95       0.95       114
    Weighted Avg  0.96      0.96       0.96       114

---

# 29. Baseline Confusion Matrix

    [[39  4]
     [ 1 70]]

Interpretation:

    39 → Class 0 correctly predicted
     4 → Class 0 predicted as Class 1
     1 → Class 1 predicted as Class 0
    70 → Class 1 correctly predicted

Correct predictions:

$$
39 + 70 = 109
$$

Total samples:

$$
114
$$

Accuracy:

$$
\frac{109}{114}=0.95614
$$

Therefore:

    Accuracy = 95.61%

---

# 30. Hyperparameter Tuning

We used GridSearchCV to search for better LightGBM parameters.

Parameter grid:

    param_grid = {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "num_leaves": [15, 31, 50],
        "max_depth": [-1, 3, 5],
        "min_child_samples": [10, 20, 30]
    }

GridSearchCV:

    grid_search = GridSearchCV(
        LGBMClassifier(
            random_state=42,
            verbosity=-1
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

# 31. GridSearchCV

We used:

    scoring="accuracy"

Therefore GridSearchCV selected parameters based on:

    Cross-Validation Accuracy

It did not select parameters using test-set accuracy.

If we use:

    scoring="roc_auc"

then GridSearchCV would optimize:

    Cross-Validation ROC-AUC

---

# 32. Correct ML Workflow

The correct workflow is:

    Training Data
          ↓
    GridSearchCV
          ↓
    5-Fold Cross-Validation
          ↓
    Test parameter combinations
          ↓
    Select best parameters
          ↓
    Refit best model
          ↓
    Test Set
          ↓
    Final Evaluation

The test set should remain separate from hyperparameter selection.

---

# 33. Best LightGBM Parameters

Our GridSearchCV selected:

    learning_rate = 0.1
    max_depth = 3
    min_child_samples = 10
    n_estimators = 200
    num_leaves = 15

Best CV Score:

    0.9692307692307693

Approximately:

    96.92% CV Accuracy

---

# 34. Meaning of the Selected Parameters

## learning_rate = 0.1

Each tree makes a moderate contribution.

## max_depth = 3

Trees are kept relatively shallow.

This helps control complexity.

## min_child_samples = 10

Leaves can contain at least 10 samples.

## n_estimators = 200

The model uses up to 200 boosting rounds.

Our baseline used:

    n_estimators = 100

The tuned model used:

    n_estimators = 200

## num_leaves = 15

The model allows up to 15 leaves per tree.

However, with:

    max_depth = 3

the depth constraint can be tighter for a binary tree.

---

# 35. Tuned LightGBM Results

Our tuned model achieved:

    Accuracy = 0.9649122807017544

    ROC-AUC = 0.9947592531935802

Confusion Matrix:

    [[40  3]
     [ 1 70]]

---

# 36. Tuned Confusion Matrix

    [[40  3]
     [ 1 70]]

Interpretation:

    40 → Class 0 correctly predicted
     3 → Class 0 predicted as Class 1
     1 → Class 1 predicted as Class 0
    70 → Class 1 correctly predicted

Correct predictions:

$$
40 + 70 = 110
$$

Total:

$$
114
$$

Accuracy:

$$
\frac{110}{114}=0.964912
$$

Therefore:

    Accuracy = 96.49%

---

# 37. Tuned Classification Report

              precision    recall    f1-score    support

    Class 0      0.98      0.93       0.95        43
    Class 1      0.96      0.99       0.97        71

    Accuracy                         0.96       114

    Macro Avg     0.97      0.96       0.96       114
    Weighted Avg  0.97      0.96       0.96       114

---

# 38. Baseline vs Tuned LightGBM

| Metric | Baseline | Tuned |
|---|---:|---:|
| Accuracy | 95.61% | 96.49% |
| ROC-AUC | 0.9941 | 0.9948 |
| Correct Predictions | 109/114 | 110/114 |

Accuracy:

    95.61% → 96.49%

ROC-AUC:

    0.9941 → 0.9948

So tuning improved both accuracy and ROC-AUC on our test set.

---

# 39. CV Score vs Test Accuracy

Our results:

    Best CV Accuracy = 0.9692

    Test Accuracy = 0.9649

This is normal.

The two metrics are calculated using different data.

CV score:

    Training data
          ↓
    Cross-validation
          ↓
    Average validation performance

Test accuracy:

    Held-out test set
          ↓
    Final evaluation

Therefore:

> CV accuracy and test accuracy do not have to be identical.

The test accuracy also does not have to be higher than the CV score.

---

# 40. Important GridSearchCV Lesson

Do not say:

> "These are the best LightGBM parameters."

Instead say:

> "These parameters produced the best cross-validation score among the parameter combinations searched for this dataset and CV setup."

This distinction is important.

Hyperparameter values are dataset-dependent.

---

# 41. LightGBM vs XGBoost

Both are gradient boosting tree algorithms.

Common concepts:

    learning_rate
    n_estimators
    max_depth
    subsampling
    feature sampling
    L1/L2 regularization

Important difference:

    XGBoost
    → commonly described with level-wise/depth-wise growth

    LightGBM
    → leaf-wise growth by default

LightGBM also uses histogram-based learning.

---

# 42. LightGBM vs XGBoost — Key Concept

XGBoost-style level-wise growth:

             Root
            /    \
          Node   Node
          / \    / \
        Leaf Leaf Leaf Leaf

LightGBM leaf-wise growth:

             Root
            /    \
         Leaf    Node
                /    \
             Leaf    Node
                    / \
                  Leaf Leaf

LightGBM chooses the leaf that provides the largest loss reduction.

---

# 43. LightGBM Overall Flow

    Training Data
          ↓
    Initial Model
          ↓
    Calculate Loss
          ↓
    Calculate Gradient
          ↓
    Evaluate possible splits
          ↓
    Select leaf with largest loss reduction
          ↓
    Split leaf
          ↓
    Apply learning rate
          ↓
    Add tree
          ↓
    Repeat
          ↓
    Final LightGBM Model

---

# 44. LightGBM Cheat Sheet

    LightGBM
    → Gradient Boosted Decision Trees

    Leaf-wise growth
    → Grow the leaf with largest loss reduction

    num_leaves
    → Maximum leaves

    max_depth
    → Maximum depth

    max_bin
    → Histogram bins

    learning_rate
    → Contribution of each tree

    n_estimators
    → Number of boosting rounds

    min_child_samples
    → Minimum samples in a leaf

    subsample
    → Row sampling

    colsample_bytree
    → Feature sampling

    reg_alpha
    → L1

    reg_lambda
    → L2

    GridSearchCV
    → Hyperparameter search using cross-validation

---

# 45. LightGBM Memory Tricks

## Tree Growth

    LightGBM
    → Leaf-wise

    Leaf-wise
    → Choose largest loss reduction

## Tree Complexity

    num_leaves
    → How many leaves?

    max_depth
    → How deep?

    min_child_samples
    → How many samples per leaf?

## Histogram

    max_bin
    → How many bins?

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
    → Contribution per tree

    n_estimators
    → Number of trees

---

# 46. Our Model Results

| Model | Test Accuracy | ROC-AUC |
|---|---:|---:|
| AdaBoost | 97.37% | 0.9961 |
| XGBoost — Tuned | 96.49% | 0.9931 |
| LightGBM — Tuned | 96.49% | 0.9948 |
| Gradient Boosting | 95.61% | 0.9951 |
| LightGBM — Baseline | 95.61% | 0.9941 |
| XGBoost — Baseline | 95.61% | 0.9931 |

These results are specific to our dataset and test split.

They should not be interpreted as universal rankings of the algorithms.

---

# 47. Important Lessons

1. LightGBM is based on Gradient Boosted Decision Trees.
2. LightGBM uses leaf-wise growth by default.
3. Leaf-wise growth chooses the leaf with the largest loss reduction.
4. Leaf-wise growth can create deep and unbalanced trees.
5. `num_leaves` controls the maximum number of leaves.
6. `max_depth` controls maximum tree depth.
7. `max_bin` controls histogram binning.
8. Histogram binning reduces the number of split candidates.
9. `learning_rate` controls each tree's contribution.
10. `n_estimators` controls the number of boosting rounds.
11. Lower learning rates generally require more trees.
12. `min_child_samples` controls the minimum samples in a leaf.
13. `subsample` controls row sampling.
14. `colsample_bytree` controls feature sampling.
15. `reg_alpha` is L1 regularization.
16. `reg_lambda` is L2 regularization.
17. GridSearchCV selects parameters according to the chosen scoring metric.
18. The test set should remain separate from hyperparameter selection.
19. Hyperparameter values are dataset-dependent.
20. A more advanced algorithm does not automatically produce better results on every dataset.

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
- [x] LightGBM

## Next

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