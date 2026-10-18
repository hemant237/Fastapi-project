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

    def _assign(self, X):
        return pairwise_sq_dist(X, self.centroids).argmin(axis=1)

    def _update(self, X, labels):
        return np.array([
            X[labels == j].mean(axis=0) if np.any(labels == j) else self.centroids[j]
            for j in range(self.k)
        ])

    def fit(self, X):
        self.centroids = self._init_centroids(X)
        for _ in range(self.max_iter):
            labels = self._assign(X)
            new = self._update(X, labels)
            shift = np.linalg.norm(new - self.centroids)
            self.centroids = new
            if shift < self.tol:
                break
        self.labels_ = self._assign(X)
        self.inertia_ = float(pairwise_sq_dist(X, self.centroids).min(axis=1).sum())
        return self

    def predict(self, X):
        return self._assign(X)


def elbow(X, ks=range(1, 8)):
    return {k: KMeans(k=k).fit(X).inertia_ for k in ks}


def silhouette_score(X, labels):
    D = np.sqrt(pairwise_sq_dist(X, X))
    scores = []
    for i in range(len(X)):
        same = labels == labels[i]
        a = D[i, same].sum() / max(same.sum() - 1, 1)
        b = min(D[i, labels == c].mean() for c in np.unique(labels) if c != labels[i])
        scores.append((b - a) / max(a, b))
    return float(np.mean(scores))


class PCA:
    def __init__(self, n_components=2):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None
        self.explained_variance_ratio_ = None

    def fit(self, X):
        self.mean_ = X.mean(axis=0)
        Xc = X - self.mean_
        cov = np.cov(Xc, rowvar=False)
        vals, vecs = np.linalg.eigh(cov)
        order = np.argsort(vals)[::-1]
        vals, vecs = vals[order], vecs[:, order]
        self.components_ = vecs[:, : self.n_components].T
        self.explained_variance_ratio_ = vals[: self.n_components] / vals.sum()
        return self
