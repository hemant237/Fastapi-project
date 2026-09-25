CatBoost --- Complete Notes
1. What is CatBoost?
CatBoost is a Gradient Boosting algorithm based on Decision Trees. The
name comes from Categorical Boosting. It is designed to work especially
well with categorical features and can be used for classification,
regression, and ranking.
2. Why CatBoost?
Categorical features include City, Gender, Education, Product Type, and
Department. A major CatBoost advantage is specialized
categorical-feature handling without requiring the same manual encoding
workflow used by many other algorithms.
3. One-Hot Encoding
One-hot encoding converts categories into binary columns.
Example:
City_Mumbai  City_Delhi  City_Pune
1            0           0
0            1           0
0            0           1
It works well for low-cardinality features but can create many columns
when a feature has thousands of categories.
4. Target Encoding
Target Encoding represents a category using target information.
Example:
Mumbai targets: 1, 0
Mean = 0.5

Delhi targets: 1, 1
Mean = 1.0

Pune target: 0
Mean = 0.0
The problem is that naive target encoding can cause target leakage.
5. Target Leakage
If a row's own target is used while creating the feature for that same
row, the model receives information about the answer.
Example:
Row 1: Mumbai → 1
Row 2: Mumbai → 0
Row 3: Mumbai → 1
Using all rows:
Mumbai mean = (1 + 0 + 1) / 3 = 0.667
Row 3's own target was used to create its feature. That is leakage.
6. Ordered Target Statistics
CatBoost uses Ordered Target Statistics.
Basic idea:
Previous observations
        ↓
Calculate category statistic
        ↓
Encode current observation
Instead of using the whole dataset, CatBoost uses an ordered approach
that helps prevent the current observation's target from directly
determining its own categorical statistic.
This reduces target leakage.
7. Prior / Smoothing
When a category has few or no previous observations, prior information
is used to make the statistic more stable.
Conceptually:
Previous category information + Prior
                ↓
       Categorical statistic
8. Ordered Boosting
Ordered Boosting is different from Ordered Target Statistics.
Ordered Target Statistics: → categorical features → reduce target
leakage
Ordered Boosting: → boosting process → reduce prediction shift
Memory trick:
Ordered Target Statistics → Categories
Ordered Boosting → Boosting
9. Prediction Shift
During training, a model learns from training observations. During
prediction, it receives unseen observations.
CatBoost's ordered boosting approach attempts to reduce the difference
between the training and prediction situations. This is related to
prediction shift.
10. CatBoost and Gradient Boosting
CatBoost is still Gradient Boosting.
Training Data
      ↓
Initial Model
      ↓
Calculate Loss
      ↓
Calculate Gradient
      ↓
Build Decision Tree
      ↓
Add Tree
      ↓
Repeat
      ↓
Final Model
The CatBoost-specific ideas are mainly specialized categorical handling,
Ordered Target Statistics, and Ordered Boosting.
11. Important Parameters
iterations
learning_rate
depth
l2_leaf_reg
random_strength
bagging_temperature
loss_function
eval_metric
cat_features
12. iterations
Controls the number of boosting rounds.
iterations ↑
     ↓
More boosting rounds
     ↓
More model capacity
Too many iterations can increase overfitting risk.
Comparison:
XGBoost  → n_estimators
LightGBM → n_estimators
CatBoost → iterations
Memory: iterations → How many boosting rounds?
13. learning_rate
Controls how much each new tree contributes.
learning_rate ↓
      ↓
Smaller contribution per tree
      ↓
Usually requires more iterations
Memory: learning_rate → How much does each tree contribute?
14. depth
Controls tree depth.
depth ↑
   ↓
More complex trees
   ↓
Higher overfitting risk
Comparison:
XGBoost  → max_depth
LightGBM → max_depth
CatBoost → depth
Memory: depth → How deep can the tree grow?
15. l2_leaf_reg
Controls L2 regularization.
l2_leaf_reg ↑
      ↓
Stronger regularization
      ↓
Controls model complexity
Comparison:
XGBoost  → reg_lambda
LightGBM → reg_lambda
CatBoost → l2_leaf_reg
Memory: l2_leaf_reg → L2 regularization
16. random_strength
Controls randomness used during split selection.
random_strength ↑
        ↓
More randomness in split selection
Memory: random_strength → Randomness during split selection
17. bagging_temperature
Controls randomness associated with Bayesian bootstrap/bagging.
bagging_temperature ↑
          ↓
More sampling randomness
Memory: bagging_temperature → Bagging randomness
18. loss_function
Defines the training objective.
Binary classification:
loss_function="Logloss"
Multiclass:
loss_function="MultiClass"
Regression:
loss_function="RMSE"
Memory: loss_function → What is the model optimizing?
19. eval_metric
Defines the evaluation/monitoring metric.
Example:
eval_metric="AUC"
Therefore:
loss_function → Training objective
eval_metric   → Evaluation/monitoring metric
20. Logloss
Logloss evaluates predicted probabilities. A prediction of 0.90 for an
actual class of 1 is much better than a prediction of 0.10.
It considers both the correct class and confidence.
21. ROC-AUC
Mental model:
Accuracy → How many final predictions are correct?
ROC-AUC  → How well does the model distinguish/rank classes?
Logloss  → How good are predicted probabilities?
22. CatBoost Classification
Import:
from catboost import CatBoostClassifier
Example:
cat_model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    depth=5,
    loss_function="Logloss",
    eval_metric="AUC",
    random_seed=42,
    verbose=False
)
Train:
cat_model.fit(X_train, y_train)
Predict:
y_pred = cat_model.predict(X_test)
Probabilities:
y_prob = cat_model.predict_proba(X_test)[:, 1]
Categorical features can be supplied with:
cat_features = ["city", "gender", "education"]

cat_model.fit(
    X_train,
    y_train,
    cat_features=cat_features
)
23. Baseline Model
Our baseline configuration:
iterations=100
learning_rate=0.1
depth=5
loss_function="Logloss"
eval_metric="AUC"
random_seed=42
Purpose:
Baseline
   ↓
Evaluate
   ↓
Tune
   ↓
Evaluate again
24. Our Baseline Results
Accuracy:
0.9736842105263158
= 97.37%
ROC-AUC:
0.9967245332459875
Confusion Matrix:
[[41  2]
 [ 1 70]]
Interpretation:
41 → Class 0 correctly predicted
 2 → Class 0 predicted as Class 1
 1 → Class 1 predicted as Class 0
70 → Class 1 correctly predicted
Correct predictions:
41 + 70 = 111
Total:
114
Accuracy:
111 / 114 = 0.973684
Classification report:
Class 0:
Precision = 0.98
Recall    = 0.95
F1        = 0.96
Support   = 43

Class 1:
Precision = 0.97
Recall    = 0.99
F1        = 0.98
Support   = 71
25. Hyperparameter Tuning
We used GridSearchCV.
Parameter grid:
param_grid = {
    "iterations": [100, 200],
    "depth": [4, 5, 6],
    "learning_rate": [0.05, 0.1],
    "l2_leaf_reg": [3, 5, 10]
}
Number of combinations:
2 × 3 × 2 × 3 = 36
With 5-fold CV:
36 × 5 = 180 model fits
Workflow:
Training Data
      ↓
GridSearchCV
      ↓
5-Fold Cross Validation
      ↓
Test parameter combinations
      ↓
Select parameters using CV
      ↓
Refit best model
      ↓
Final test evaluation
Important: Do not use the test set to choose hyperparameters.
26. Best CatBoost Parameters
Our GridSearchCV returned:
{
    'depth': 6,
    'iterations': 100,
    'l2_leaf_reg': 5,
    'learning_rate': 0.1
}
Best CV score:
0.9927708816573981
Approximately:
99.28% CV score
These are the best parameters among the combinations searched for this
dataset and CV setup. They are not universally best CatBoost parameters.
27. Tuned Model
Configuration:
depth=6
iterations=100
l2_leaf_reg=5
learning_rate=0.1
loss_function="Logloss"
eval_metric="AUC"
Tuned results:
Accuracy = 0.9649122807017544
Accuracy = 96.49%

ROC-AUC = 0.9941041598427777
Confusion Matrix:
[[40  3]
 [ 1 70]]
Correct predictions:
40 + 70 = 110
Accuracy:
110 / 114 = 0.964912
Classification report:
Class 0:
Precision = 0.98
Recall    = 0.93
F1        = 0.95
Support   = 43

Class 1:
Precision = 0.96
Recall    = 0.99
F1        = 0.97
Support   = 71
28. Baseline vs Tuned
  Metric                  Baseline     Tuned
  Accuracy                  97.37%    96.49%
  ROC-AUC                   0.9967    0.9941
  Correct Predictions      111/114   110/114
Important lesson:
Hyperparameter tuning does not guarantee that the final held-out test
metric will increase.
The tuning process selects parameters using the validation/CV procedure.
29. CV Score vs Test Score
Best CV score:
0.9927708816573981
Tuned test accuracy:
0.9649122807017544
They measure different things.
CV score
→ average validation performance during cross-validation

Test score
→ performance on the held-out test set
Therefore:
CV Score ≠ Test Score
This is normal.
30. Early Stopping
Basic idea:
Maximum Iterations
        ↓
   Train Model
        ↓
Monitor Validation Performance
        ↓
Performance stops improving
        ↓
   Stop Training
Early stopping can prevent unnecessary additional boosting rounds and
can help control overfitting.
31. Our Early-Stopping Experiment
Best iteration:
20
Best validation information:
Logloss = 0.14273731658159652
AUC     = 0.9865841073271414
Test results:
Accuracy = 0.956140350877193
Accuracy = 95.61%

ROC-AUC = 0.9941041598427776
Confusion Matrix:
[[40  3]
 [ 2 69]]
Correct predictions:
40 + 69 = 109
Total:
114
Accuracy:
109 / 114 = 0.956140
Classification report:
Class 0:
Precision = 0.95
Recall    = 0.93
F1        = 0.94
Support   = 43

Class 1:
Precision = 0.96
Recall    = 0.97
F1        = 0.97
Support   = 71
32. Our CatBoost Experiment Summary
  Experiment             Accuracy   ROC-AUC
  Baseline                 97.37%    0.9967
  GridSearchCV Tuned       96.49%    0.9941
  Early Stopping           95.61%    0.9941
These results are specific to our dataset, features, train/test split,
hyperparameters, and validation setup.
33. CatBoost vs XGBoost
Both are Gradient Boosting Tree algorithms.
  Concept              XGBoost         CatBoost
  Number of trees      n_estimators    iterations
  Learning rate        learning_rate   learning_rate
  Tree depth           max_depth       depth
  L2 regularization    reg_lambda      l2_leaf_reg
  Training objective   objective       loss_function
  Evaluation metric    eval_metric     eval_metric
Important CatBoost-specific concepts:
- Categorical Feature Handling
- Ordered Target Statistics
- Ordered Boosting
34. CatBoost vs LightGBM
LightGBM:
Leaf-wise Growth
+
Histogram-based Learning
CatBoost:
Categorical Feature Handling
+
Ordered Target Statistics
+
Ordered Boosting
All are Gradient Boosting Tree frameworks, but their internal approaches
differ.
35. XGBoost vs LightGBM vs CatBoost
  Algorithm   Important Concept
  XGBoost     Gradient Boosting + optimized tree learning
  LightGBM    Leaf-wise growth + histogram-based learning
  CatBoost    Categorical handling + ordered techniques
Performance depends on:
- Dataset
- Features
- Preprocessing
- Hyperparameters
- Validation setup
36. Complete CatBoost Workflow
Raw Dataset
      ↓
Understand Features
      ↓
Separate X and y
      ↓
Train/Test Split
      ↓
Identify Categorical Features
      ↓
CatBoost Classifier
      ↓
Ordered Categorical Processing
      ↓
Build Decision Trees
      ↓
Boosting
      ↓
Final CatBoost Model
      ↓
Predict
      ↓
Evaluate
      ↓
Hyperparameter Tuning
      ↓
Cross Validation
      ↓
Final Test Evaluation
37. Cheat Sheet
CatBoost
→ Gradient Boosting

CatBoost
→ Decision Trees

CatBoost
→ Categorical Boosting

Ordered Target Statistics
→ Reduce target leakage

Ordered Boosting
→ Reduce prediction shift

iterations
→ Number of boosting rounds

learning_rate
→ Contribution of each tree

depth
→ Tree depth

l2_leaf_reg
→ L2 regularization

random_strength
→ Randomness during split selection

bagging_temperature
→ Bagging randomness

loss_function
→ Training objective

eval_metric
→ Evaluation metric

GridSearchCV
→ Hyperparameter tuning

Cross Validation
→ Estimate validation performance

Test Set
→ Final evaluation

Early Stopping
→ Stop when validation performance stops improving
38. Memory Tricks
CAT
↓
Categorical

iterations
→ How many?

learning_rate
→ How much?

depth
→ How deep?

l2_leaf_reg
→ How much regularization?

Ordered Target Statistics
→ Categories

Ordered Boosting
→ Boosting
39. Important Lessons
1. CatBoost is a Gradient Boosting algorithm.
2. CatBoost uses Decision Trees.
3. CatBoost is particularly useful for categorical features.
4. Arbitrary integer encoding of categories can create misleading
   numerical relationships.
5. One-Hot Encoding is one way to represent categorical variables.
6. Target Encoding uses target information to represent categories.
7. Naive Target Encoding can cause target leakage.
8. CatBoost uses Ordered Target Statistics to reduce this leakage.
9. Ordered Target Statistics and Ordered Boosting are different.
10. Ordered Target Statistics deal with categorical feature statistics.
11. Ordered Boosting deals with the boosting process.
12. iterations controls the number of boosting rounds.
13. learning_rate controls each tree's contribution.
14. Lower learning rates generally require more iterations.
15. depth controls tree depth.
16. Larger depth increases model complexity.
17. l2_leaf_reg controls L2 regularization.
18. random_strength controls randomness during split selection.
19. bagging_temperature controls bagging randomness.
20. loss_function defines the training objective.
21. eval_metric defines the evaluation/monitoring metric.
22. GridSearchCV searches hyperparameter combinations.
23. GridSearchCV uses cross-validation.
24. Best CV score is not necessarily the final test score.
25. The test set should remain separate from hyperparameter selection.
26. Early stopping can stop training when validation performance stops
    improving.
27. Hyperparameters are dataset-dependent.
28. A more advanced algorithm does not automatically produce better
    results on every dataset.
40. Final CatBoost Mental Model
CATBOOST
    ↓
Gradient Boosting
    ↓
Decision Trees
    ↓
Categorical Features
    ↓
Ordered Target Statistics
    ↓
Reduce Target Leakage
    ↓
Ordered Boosting
    ↓
Reduce Prediction Shift
    ↓
Final Model
    ↓
Hyperparameter Tuning
    ↓
Cross Validation
    ↓
Final Test Evaluation
41. ML Progress
Completed:
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
- [x] CatBoost
Next:
- [ ] Unsupervised Learning
- [ ] K-Means Clustering
- [ ] Hierarchical Clustering
- [ ] DBSCAN
- [ ] Dimensionality Reduction
- [ ] PCA
- [ ] Remaining ML topics
- [ ] Deep Learning
- [ ] NLP
- [ ] Transformers
- [ ] LLMs
- [ ] RAG
- [ ] AI Agents
- [ ] Production AI Engineering
- [ ] Final AI Engineer Projects
CATBOOST COMPLETE