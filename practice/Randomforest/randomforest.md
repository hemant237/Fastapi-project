# Random Forest

## 1. What is Random Forest?

Random Forest is an ensemble machine learning algorithm that combines
multiple Decision Trees to make a final prediction.

Instead of relying on one Decision Tree:

One Tree → Prediction

Random Forest:

Many Trees → Combine Predictions → Final Prediction

For classification:
→ Majority voting

For regression:
→ Average of predictions


--------------------------------------------------
## 2. Why Random Forest?
--------------------------------------------------

A single Decision Tree can have high variance and overfit.

Example:

Train Accuracy = 100%
Test Accuracy  = 90%

Random Forest reduces this problem by combining many diverse trees.

Main idea:

Multiple trees
      ↓
Different training samples
      +
Random feature selection
      ↓
Diverse trees
      ↓
Combine predictions
      ↓
Lower variance / better generalization


--------------------------------------------------
## 3. Ensemble Learning
--------------------------------------------------

Ensemble learning means combining multiple models to produce
a final prediction.

Instead of:

One model → Prediction

We use:

Multiple models → Combined prediction


--------------------------------------------------
## 4. Bagging
--------------------------------------------------

Bagging = Bootstrap Aggregating

It has two main steps:

1. Bootstrap sampling
2. Aggregating predictions


### Bootstrap Sampling

Samples are selected from the training data WITH replacement.

Example:

Original:

A B C D E

Bootstrap sample:

A C C E A

Notice:

A → appears multiple times
C → appears multiple times
B → not selected
D → not selected
E → selected


Important:

The bootstrap sample has the same number of selections
as the original dataset, but some observations repeat
and some are left out.


--------------------------------------------------
## 5. Out-of-Bag (OOB) Samples
--------------------------------------------------

Samples that are not selected for a particular bootstrap
sample are called Out-of-Bag samples.

For a large dataset:

Approximately:

63% → unique observations selected
37% → OOB observations

The ~37% result comes from:

(1 - 1/n)^n ≈ e^-1 ≈ 0.368


Important:

37% does NOT mean 37% of the entire Random Forest
training data is permanently unused.

The OOB samples are different for each tree.


--------------------------------------------------
## 6. OOB Score
--------------------------------------------------

Random Forest can use OOB samples to estimate model performance.

Example:

oob_score = 0.95

means:

Approximately 95% of the OOB predictions were correct.

It does NOT mean:

95% of the data was out-of-bag.


Example:

~37% → approximately OOB for each tree

95% → accuracy of OOB predictions


--------------------------------------------------
## 7. Random Feature Selection
--------------------------------------------------

At every split, Random Forest considers only a subset
of the available features.

Example:

Total features = 20

max_features = 5

At a particular split:

20 features
     ↓
5 selected features considered
     ↓
Best split among those 5


The selected feature subset can differ at different splits.


--------------------------------------------------
## 8. Why Random Feature Selection?
--------------------------------------------------

It creates diversity between trees.

Without random feature selection:

Trees may become very similar.

Similar trees
     ↓
Similar predictions
     ↓
Highly correlated errors

Random feature selection:

Different features
     ↓
Different trees
     ↓
Less correlated errors
     ↓
Better ensemble


Important:

Random feature selection is NOT primarily intended
to increase the accuracy of every individual tree.

The goal is to create diversity and reduce correlation.


--------------------------------------------------
## 9. Random Forest = Bagging + Random Features
--------------------------------------------------

Random Forest combines:

1. Bootstrap sampling
2. Random feature selection

Therefore:

Random Forest
=
Bagging
+
Random Feature Selection


--------------------------------------------------
## 10. Majority Voting
--------------------------------------------------

For classification, each tree gives a class prediction.

Example:

7 trees:

Tree 1 → Class 0
Tree 2 → Class 1
Tree 3 → Class 1
Tree 4 → Class 1
Tree 5 → Class 0
Tree 6 → Class 1
Tree 7 → Class 0

Class 0 → 3 votes
Class 1 → 4 votes

Final prediction:

Class 1


--------------------------------------------------
## 11. Vote Proportion
--------------------------------------------------

If:

100 trees

Class 0 → 42 votes
Class 1 → 58 votes

Then:

Class 0 ≈ 42%
Class 1 ≈ 58%

Prediction:

Class 1


--------------------------------------------------
## 12. Important Hyperparameters
--------------------------------------------------

### n_estimators

Number of Decision Trees in the forest.

Example:

RandomForestClassifier(n_estimators=100)

More trees generally make the ensemble more stable.

However, increasing trees does not guarantee continuous
improvement in test accuracy.

After a certain point, additional trees may provide
little improvement while increasing computation.


### max_depth

Maximum depth of each Decision Tree.

Lower max_depth:

→ Simpler trees
→ Higher bias
→ Lower variance
→ Lower overfitting risk

Higher max_depth:

→ More complex trees
→ Lower bias
→ Higher variance
→ Higher overfitting risk


### min_samples_split

Minimum number of samples required for a node
to be considered for splitting.

Example:

min_samples_split = 10

Node = 12 samples

12 >= 10

→ Can attempt a split.


### min_samples_leaf

Minimum number of samples that must remain
in each resulting leaf.

Example:

min_samples_leaf = 5

Potential split:

Left  = 8
Right = 4

Right leaf violates:

4 < 5

Therefore:

→ Split is not allowed.


### max_features

Number of features considered when searching
for the best split.

Example:

20 total features
max_features = 5

→ Only 5 selected features are considered
at that split.


--------------------------------------------------
## 13. Random Forest and Variance
--------------------------------------------------

A single Decision Tree can have high variance.

Random Forest reduces variance by averaging/voting
across many diverse trees.

Conceptually:

One tree
    ↓
High variance

Many diverse trees
    ↓
Average / majority vote
    ↓
Lower variance
    ↓
Better generalization


--------------------------------------------------
## 14. Random Forest and Overfitting
--------------------------------------------------

Random Forest can still overfit depending on
the hyperparameters and dataset.

Important controls:

n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features


--------------------------------------------------
## 15. Your Random Forest Experiment
--------------------------------------------------

Your results:

Trees = 1
Train Accuracy ≈ 95.82%
Test Accuracy ≈ 93.86%

Trees = 5
Train Accuracy ≈ 98.24%
Test Accuracy ≈ 94.74%

Trees = 10
Train Accuracy ≈ 99.78%
Test Accuracy ≈ 95.61%

Trees = 50
Train Accuracy = 100%
Test Accuracy ≈ 96.49%

Trees = 100
Train Accuracy = 100%
Test Accuracy ≈ 96.49%

Trees = 500
Train Accuracy = 100%
Test Accuracy ≈ 96.49%


Observation:

Increasing the number of trees initially improved
test performance.

After around 50 trees in this experiment:

50  → 96.49%
100 → 96.49%
500 → 96.49%

Additional trees did not improve the test accuracy.


--------------------------------------------------
## 16. GridSearchCV
--------------------------------------------------

Random Forest hyperparameters can be tuned using GridSearchCV.

Example:

param_grid = {
    "n_estimators": [10, 50, 100],
    "max_depth": [5, 10, None],
    "min_samples_leaf": [1, 2]
}

GridSearchCV:

Training data
     ↓
Cross-validation
     ↓
Different parameter combinations
     ↓
Evaluate each combination
     ↓
Best parameters
     ↓
Train final model
     ↓
Evaluate once on test set


Important:

The test set should NOT be used during GridSearchCV.


--------------------------------------------------
## 17. Cross Validation
--------------------------------------------------

Cross-validation helps estimate how well the model
generalizes across different subsets of the training data.

Example:

5-fold CV

Training data:

Fold 1
Fold 2
Fold 3
Fold 4
Fold 5

Each fold gets a chance to act as validation data.

The scores are averaged.


--------------------------------------------------
## 18. Random Forest vs Decision Tree
--------------------------------------------------

Decision Tree:

One tree
→ Can have high variance
→ Can easily overfit

Random Forest:

Many trees
→ Bootstrap samples
→ Random feature selection
→ Majority voting
→ Lower variance
→ More robust


--------------------------------------------------
## 19. Random Forest Classification Workflow
--------------------------------------------------

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


--------------------------------------------------
## 20. Evaluation
--------------------------------------------------

Common metrics:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
ROC-AUC

For probability-based ROC-AUC:

y_prob = model.predict_proba(X_test)[:, 1]

roc_auc_score(y_test, y_prob)


--------------------------------------------------
## 21. Key Concepts to Remember
--------------------------------------------------

Random Forest
→ Many Decision Trees

Bagging
→ Bootstrap samples + aggregation

Bootstrap
→ Sampling with replacement

OOB
→ Samples not selected for a particular tree

~37%
→ Approximate OOB proportion per tree

OOB Score
→ Performance on OOB predictions

Random feature selection
→ Creates diversity between trees

Classification
→ Majority voting

Regression
→ Average predictions

n_estimators
→ Number of trees

max_depth
→ Maximum tree depth

min_samples_split
→ Minimum samples needed to split

min_samples_leaf
→ Minimum samples allowed in resulting leaves

max_features
→ Number of features considered at a split


--------------------------------------------------
## ⭐ One-Minute Revision
--------------------------------------------------

Decision Tree
→ One tree
→ High variance risk

Random Forest
→ Many Decision Trees

Random Forest uses:

Bootstrap sampling
+
Random feature selection
+
Majority voting / averaging

Main purpose:

Reduce variance
+
Improve generalization

For classification:

Trees vote
↓
Majority wins

For regression:

Trees predict
↓
Average predictions