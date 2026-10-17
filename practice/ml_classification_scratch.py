"""Classification basics from scratch: logistic regression and KNN."""
import numpy as np


def make_blobs(n=200, seed=0):
    rng = np.random.default_rng(seed)
    X0 = rng.normal(loc=-1.5, scale=1.0, size=(n // 2, 2))
    X1 = rng.normal(loc=1.5, scale=1.0, size=(n // 2, 2))
    X = np.vstack([X0, X1])
    y = np.array([0] * (n // 2) + [1] * (n // 2))
    return X, y


def train_test_split(X, y, test_size=0.25, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    return X[idx[:cut]], X[idx[cut:]], y[idx[:cut]], y[idx[cut:]]


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def accuracy(y_true, y_pred):
    return float(np.mean(y_true == y_pred))


def binary_cross_entropy(y_true, p, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))
