"""DBSCAN implemented from scratch with NumPy."""
import numpy as np


def region_query(X, idx, eps):
    """Return indices of all points within eps of X[idx]."""
    dists = np.linalg.norm(X - X[idx], axis=1)
    return np.where(dists <= eps)[0]
