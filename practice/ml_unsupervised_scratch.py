"""Unsupervised learning from scratch: k-means and PCA."""
import numpy as np


def make_clusters(n_per=100, centers=((0, 0), (5, 5), (0, 6)), std=0.8, seed=0):
    rng = np.random.default_rng(seed)
    X = np.vstack([rng.normal(c, std, size=(n_per, 2)) for c in centers])
    y = np.repeat(np.arange(len(centers)), n_per)
    return X, y
