"""Scratch ML basics: linear regression from scratch with NumPy."""
import numpy as np


def make_data(n=200, noise=1.0, seed=42):
    """Generate y = 3x + 4 + noise."""
    rng = np.random.default_rng(seed)
    X = rng.uniform(-5, 5, size=(n, 1))
    y = 3 * X[:, 0] + 4 + rng.normal(0, noise, size=n)
    return X, y


def train_test_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    return X[idx[:cut]], X[idx[cut:]], y[idx[:cut]], y[idx[cut:]]


def standardize(X_train, X_test):
    mu, sigma = X_train.mean(axis=0), X_train.std(axis=0)
    return (X_train - mu) / sigma, (X_test - mu) / sigma
