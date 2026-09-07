## Decision Tree — Gini Impurity

A Decision Tree makes predictions by asking a series of if/else questions.

### Gini Impurity

Gini measures how mixed the classes are in a node.

Formula:

Gini = 1 - (p₀² + p₁² + ... + pₙ²)

For binary classification:

Gini = 1 - (p₀² + p₁²)

Where:
- p₀ = proportion of Class 0
- p₁ = proportion of Class 1

### Interpretation

Gini = 0 → Pure node (only one class)

Higher Gini → More mixed classes

For binary classification:
Maximum Gini = 0.5

### Weighted Gini

When evaluating a split:

Weighted Gini =
(N_left / N) × Gini_left
+
(N_right / N) × Gini_right

The Decision Tree chooses the split with the lowest weighted Gini.


## Decision Tree — Entropy & Information Gain

### Entropy

Measures the impurity/uncertainty of a node.

Formula:

Entropy = -Σ pᵢ log₂(pᵢ)

For binary classification:

Entropy = -(p₀ log₂p₀ + p₁ log₂p₁)

Entropy = 0 → Pure node
Entropy = 1 → Maximum impurity (binary classification)

### Information Gain

Measures how much a split reduces entropy.

Formula:

Information Gain =
Entropy_parent - Weighted Entropy_children

Higher Information Gain → Better split.

Decision Tree can use:
- Gini Impurity → minimize weighted Gini
- Entropy → maximize Information Gain