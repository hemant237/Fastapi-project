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

    def _best_split(self, X, y):
        n_feat = X.shape[1]
        k = self.max_features or n_feat
        features = self.rng.choice(n_feat, size=k, replace=False)
        best = (None, None, 0.0)
        for f in features:
            for t in np.unique(X[:, f]):
                gain = information_gain(y, X[:, f] <= t, self.impurity)
                if gain > best[2]:
                    best = (f, t, gain)
        return best

    def _grow(self, X, y, depth):
        if (depth >= self.max_depth or len(y) < self.min_samples_split
                or len(np.unique(y)) == 1):
            return Node(value=int(np.bincount(y).argmax()))
        f, t, gain = self._best_split(X, y)
        if f is None:
            return Node(value=int(np.bincount(y).argmax()))
        mask = X[:, f] <= t
        return Node(f, t, self._grow(X[mask], y[mask], depth + 1),
                    self._grow(X[~mask], y[~mask], depth + 1))

    def fit(self, X, y):
        self.root = self._grow(X, y, 0)
        return self

    def _walk(self, x, node):
        while not node.is_leaf():
            node = node.left if x[node.feature] <= node.threshold else node.right
        return node.value

    def predict(self, X):
        return np.array([self._walk(x, self.root) for x in X])

    def depth(self, node=None):
        node = node or self.root
        if node.is_leaf():
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
