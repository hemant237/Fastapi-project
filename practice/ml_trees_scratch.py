"""Tree-based models from scratch: decision tree and random forest."""
import numpy as np


def make_moons(n=300, noise=0.25, seed=0):
    rng = np.random.default_rng(seed)
    t = rng.uniform(0, np.pi, n // 2)
    X0 = np.c_[np.cos(t), np.sin(t)]
    X1 = np.c_[1 - np.cos(t), 0.5 - np.sin(t)]
    X = np.vstack([X0, X1]) + rng.normal(0, noise, (n - n % 2, 2))
    y = np.array([0] * (n // 2) + [1] * (n // 2))
    return X, y


def train_test_split(X, y, test_size=0.25, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    return X[idx[:cut]], X[idx[cut:]], y[idx[:cut]], y[idx[cut:]]


def accuracy(y_true, y_pred):
    return float(np.mean(y_true == y_pred))


def gini(y):
    if len(y) == 0:
        return 0.0
    p = np.bincount(y) / len(y)
    return float(1 - np.sum(p ** 2))


def entropy(y):
    if len(y) == 0:
        return 0.0
    p = np.bincount(y) / len(y)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def information_gain(y, left_mask, impurity=gini):
    n, n_l = len(y), left_mask.sum()
    if n_l == 0 or n_l == n:
        return 0.0
    child = (n_l * impurity(y[left_mask]) + (n - n_l) * impurity(y[~left_mask])) / n
    return impurity(y) - child


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf(self):
        return self.value is not None


class DecisionTreeClassifier:
    def __init__(self, max_depth=5, min_samples_split=2, max_features=None,
                 criterion="gini", seed=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.max_features = max_features
        self.impurity = gini if criterion == "gini" else entropy
        self.rng = np.random.default_rng(seed)
        self.root = None
