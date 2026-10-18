"""Unsupervised learning from scratch: k-means and PCA."""
import numpy as np


def make_clusters(n_per=100, centers=((0, 0), (5, 5), (0, 6)), std=0.8, seed=0):
    rng = np.random.default_rng(seed)
    X = np.vstack([rng.normal(c, std, size=(n_per, 2)) for c in centers])
    y = np.repeat(np.arange(len(centers)), n_per)
    return X, y


def standardize(X):
    mu, sd = X.mean(axis=0), X.std(axis=0)
    return (X - mu) / np.where(sd == 0, 1, sd)


def pairwise_sq_dist(A, B):
    return ((A[:, None, :] - B[None, :, :]) ** 2).sum(axis=2)


class KMeans:
    def __init__(self, k=3, max_iter=100, tol=1e-6, seed=0):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.seed = seed
        self.centroids = None
        self.inertia_ = None

    def _init_centroids(self, X):
        rng = np.random.default_rng(self.seed)
        centroids = [X[rng.integers(len(X))]]
        for _ in range(1, self.k):
            d = pairwise_sq_dist(X, np.array(centroids)).min(axis=1)
            centroids.append(X[rng.choice(len(X), p=d / d.sum())])
        return np.array(centroids)
