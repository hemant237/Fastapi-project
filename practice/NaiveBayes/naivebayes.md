# Naive Bayes

## 1. What is Naive Bayes?

- Naive Bayes is a supervised machine learning algorithm mainly used for classification.
- It is based on Bayes' theorem.
- It calculates the probability of a sample belonging to each class.
- The class with the highest probability/score is selected as the prediction.

---

## 2. Bayes' Theorem

Formula:

P(A | B) = [P(B | A) × P(A)] / P(B)

Where:

P(A | B)
→ Probability of A given B
→ Posterior

P(B | A)
→ Probability of B given A
→ Likelihood

P(A)
→ Probability of A before seeing the evidence
→ Prior

P(B)
→ Overall probability of the evidence
→ Evidence

---

## 3. Conditional Probability Direction

P(FREE | Spam)

→ Probability that an email contains FREE, given that it is Spam.

P(Spam | FREE)

→ Probability that an email is Spam, given that it contains FREE.

The direction matters.

The "|" symbol can be read as "given".

---

## 4. Naive Assumption

Naive Bayes assumes that features are conditionally independent given the class.

For example:

P(FREE, OFFER | Spam)

is approximated as:

P(FREE | Spam) × P(OFFER | Spam)

This assumption is often not perfectly true in real-world data.

The algorithm is called "Naive" because of this simplifying assumption.

---

## 5. Naive Bayes Classification

For multiple features:

P(Class | Features)
∝
P(Class) × P(Feature1 | Class)
× P(Feature2 | Class)
× ...

Process:

Training data
↓
Calculate prior probabilities
↓
Calculate feature likelihoods
↓
Calculate class scores
↓
Compare class scores
↓
Highest score = prediction

---

## 6. Prior Probability

Prior = probability of a class before considering the features.

Example:

80 Spam emails
120 Not Spam emails
200 total

P(Spam) = 80 / 200 = 0.40

P(Not Spam) = 120 / 200 = 0.60

---

## 7. Likelihood

Likelihood tells us how likely a feature is given a particular class.

Example:

50 Spam emails
35 contain FREE

P(FREE | Spam) = 35 / 50
               = 0.70

So 70% of Spam emails contain FREE.

---

## 8. Complete Example

Suppose:

P(Spam) = 0.30

P(FREE | Spam) = 0.80

P(OFFER | Spam) = 0.50

Then:

P(FREE, OFFER | Spam)

= 0.80 × 0.50
= 0.40

Spam score:

= P(Spam) × P(FREE | Spam) × P(OFFER | Spam)

= 0.30 × 0.80 × 0.50

= 0.12

The same calculation is performed for Not Spam.

The class with the higher score is selected.

---

## 9. Unnormalized Score

The calculated class score is initially not necessarily the final probability.

Example:

Spam score = 0.12
Not Spam score = 0.014

Spam is predicted because:

0.12 > 0.014

To convert these scores into normalized probabilities:

P(Spam | Features)
=
0.12 / (0.12 + 0.014)

≈ 0.8955

≈ 89.55%

---

## 10. Laplace Smoothing

### Problem

Suppose:

20 Spam emails
0 contain "Bitcoin"

Then:

P(Bitcoin | Spam) = 0 / 20 = 0

Because Naive Bayes multiplies probabilities, one zero probability can make the entire class score zero.

This is called the zero-frequency problem.

### Solution

Use Laplace smoothing.

Basic formula:

P(feature | class)
=
(count(feature,class) + 1)
/
(count(class) + N)

For a binary feature:

N = 2

Example:

10 Spam emails
2 contain FREE

P(FREE | Spam)
=
(2 + 1) / (10 + 2)

=
3 / 12

=
0.25

Without smoothing:

2 / 10 = 0.20

---

# 11. Main Naive Bayes Variants

## GaussianNB

Used mainly for continuous numerical features.

Examples:

- Age
- Height
- Weight
- Temperature
- Mean radius
- Mean area

GaussianNB assumes the feature values within each class can be modeled using a Gaussian/normal distribution.

Important values:

Mean (μ)
Variance (σ²)

Example:

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

---

## MultinomialNB

Commonly used for count-based data.

Especially useful for text classification.

Examples:

- Number of times a word appears
- Word counts
- Document-term frequencies

Example:

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

---

## BernoulliNB

Used for binary features.

Features are generally:

0 = absent
1 = present

or:

No = 0
Yes = 1

Example:

FREE = 1
OFFER = 1
MONEY = 0

Example:

from sklearn.naive_bayes import BernoulliNB

model = BernoulliNB()

---

## 12. Easy Memory Trick

Gaussian
→ Continuous numerical values

Multinomial
→ Counts

Bernoulli
→ Binary 0/1

---

## 13. Gaussian Naive Bayes

GaussianNB models the distribution of each feature for each class.

For every feature/class combination, it estimates:

Mean
Variance

Then it calculates how likely a particular feature value is under each class.

Example:

Class 0:
mean radius = 10

Class 1:
mean radius = 20

New sample:
mean radius = 19

19 is closer to Class 1's mean, so the feature is more likely under Class 1, assuming similar variance.

---

## 14. Feature Independence

Real-world features are often related.

For example:

mean radius
↕
mean perimeter
↕
mean area

These features are not completely independent.

But Naive Bayes can still work well because classification can remain effective even when the independence assumption isn't perfectly true.

Important:

The probability estimates may not be perfectly accurate,
but the model can still rank the classes correctly.

---

## 15. Feature Scaling

GaussianNB does not require feature scaling in the same way distance-based algorithms such as KNN or margin-based SVM workflows do.

However, scaling can still be used consistently in a preprocessing pipeline.

Example:

scaler.fit_transform(X_train)

scaler.transform(X_test)

Never fit the scaler separately on the test set.

---

## 16. GaussianNB Implementation

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

---

## 17. Evaluation

Accuracy:

accuracy_score(y_test, y_pred)

Confusion Matrix:

confusion_matrix(y_test, y_pred)

Classification Report:

classification_report(y_test, y_pred)

ROC-AUC:

y_prob = model.predict_proba(X_test_scaled)[:, 1]

roc_auc_score(y_test, y_prob)

---

## 18. predict() vs predict_proba()

predict():

Returns the final class.

Example:

[0, 1, 1, 0]

predict_proba():

Returns probabilities for each class.

Example:

[[0.90, 0.10],
 [0.20, 0.80],
 [0.05, 0.95],
 [0.85, 0.15]]

For binary classification:

[:, 1]

selects the probability of Class 1.

---

## 19. ROC-AUC and Naive Bayes

ROC-AUC can be calculated using probability scores:

y_prob = model.predict_proba(X_test)[:, 1]

roc_auc_score(y_test, y_prob)

Accuracy uses final class predictions.

ROC-AUC evaluates how well the model separates/ranks the classes across different thresholds.

Therefore, accuracy and ROC-AUC can have different values.

---

# 20. Your GaussianNB Results

On the Breast Cancer dataset:

Accuracy:

96.49%

Confusion Matrix:

[[40  1]
 [ 3 70]]

Classification Report:

Class 0:
Precision = 0.93
Recall = 0.98
F1 = 0.95

Class 1:
Precision = 0.99
Recall = 0.96
F1 = 0.97

ROC-AUC:

99.74%

---

# 21. SVM vs GaussianNB

Your results:

SVM RBF:
Test Accuracy ≈ 98.25%

GaussianNB:
Test Accuracy ≈ 96.49%

GaussianNB:
ROC-AUC ≈ 99.74%

Remember:

These results are specific to your dataset and experimental setup.

Do not conclude that one algorithm is universally better.

---

# 22. Advantages of Naive Bayes

- Simple and fast.
- Easy to train.
- Works well for classification.
- Can work well with relatively small datasets.
- Particularly useful for text classification.
- Produces probability estimates.
- Computationally efficient.

---

# 23. Limitations

- Strong conditional-independence assumption.
- Features may not actually be independent.
- Probability estimates can sometimes be poorly calibrated.
- Zero-frequency problem without smoothing.
- GaussianNB assumes a Gaussian distribution for continuous features.

---

# 24. Important Terms

Prior
→ Probability of the class before seeing features.

Likelihood
→ Probability of features given the class.

Posterior
→ Probability of the class given the features.

Evidence
→ Overall probability of the observed features.

Naive assumption
→ Features are conditionally independent given the class.

Laplace smoothing
→ Prevents zero probabilities.

GaussianNB
→ Continuous numerical features.

MultinomialNB
→ Counts/frequencies.

BernoulliNB
→ Binary features.

---

# ⭐ One-Minute Naive Bayes Revision

Naive Bayes
→ Probability-based classification algorithm.

Bayes' theorem
→ Connects prior, likelihood, evidence and posterior.

Naive
→ Assumes conditional independence between features.

Prior
→ P(Class)

Likelihood
→ P(Feature | Class)

Posterior
→ P(Class | Features)

Classification:

Prior × Likelihoods
↓
Class score
↓
Compare scores
↓
Highest score wins

Laplace smoothing
→ Prevents zero probabilities.

GaussianNB
→ Continuous values.

MultinomialNB
→ Counts.

BernoulliNB
→ Binary 0/1.

predict()
→ Class prediction.

predict_proba()
→ Probability of each class.

ROC-AUC
→ Can use probability scores.