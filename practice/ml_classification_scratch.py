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


class LogisticRegressionGD:
    def __init__(self, lr=0.1, epochs=500):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = 0.0
        self.losses = []

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        for _ in range(self.epochs):
            p = sigmoid(X @ self.w + self.b)
            grad = p - y
            self.w -= self.lr * (X.T @ grad) / len(X)
            self.b -= self.lr * grad.mean()
            self.losses.append(binary_cross_entropy(y, p))
        return self

    def predict_proba(self, X):
        return sigmoid(X @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


class KNNClassifier:
    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        self.X, self.y = X, y
        return self

    def predict(self, X):
        d = np.linalg.norm(X[:, None, :] - self.X[None, :, :], axis=2)
        nearest = np.argsort(d, axis=1)[:, : self.k]
        return np.array([np.bincount(self.y[row]).argmax() for row in nearest])


def confusion_matrix(y_true, y_pred):
    cm = np.zeros((2, 2), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    return cm
