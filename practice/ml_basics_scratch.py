"""Scratch ML basics: linear regression from scratch with NumPy."""
import numpy as np


def make_data(n=200, noise=1.0, seed=42):
    """Generate y = 3x + 4 + noise."""
    rng = np.random.default_rng(seed)
    X = rng.uniform(-5, 5, size=(n, 1))
    y = 3 * X[:, 0] + 4 + rng.normal(0, noise, size=n)
    return X, y
