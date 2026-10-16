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


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return 1 - ss_res / ss_tot


class LinearRegressionGD:
    """Linear regression trained with batch gradient descent."""

    def __init__(self, lr=0.05, epochs=500):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        self.history = []
        for _ in range(self.epochs):
            err = X @ self.w + self.b - y
            self.w -= self.lr * (2 / n) * (X.T @ err)
            self.b -= self.lr * (2 / n) * err.sum()
            self.history.append(np.mean(err ** 2))
        return self

    def predict(self, X):
        return X @ self.w + self.b
