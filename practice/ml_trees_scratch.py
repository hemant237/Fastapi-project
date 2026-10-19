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
