"""DBSCAN implemented from scratch with NumPy."""
import numpy as np


def region_query(X, idx, eps):
    """Return indices of all points within eps of X[idx]."""
    dists = np.linalg.norm(X - X[idx], axis=1)
    return np.where(dists <= eps)[0]


def dbscan(X, eps=0.5, min_samples=5):
    """Cluster X; returns labels where -1 means noise."""
    n = len(X)
    labels = np.full(n, -1)
    visited = np.zeros(n, dtype=bool)
    cluster_id = 0

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        neighbors = region_query(X, i, eps)
        if len(neighbors) < min_samples:
            continue  # noise (may later become a border point)
        _expand_cluster(X, labels, visited, i, neighbors, cluster_id, eps, min_samples)
        cluster_id += 1

    return labels


def _expand_cluster(X, labels, visited, point, neighbors, cluster_id, eps, min_samples):
    """Grow a cluster outward from a core point via density reachability."""
    labels[point] = cluster_id
    queue = list(neighbors)
    while queue:
        j = queue.pop()
        if labels[j] == -1:
            labels[j] = cluster_id  # core or border point joins cluster
        if visited[j]:
            continue
        visited[j] = True
        j_neighbors = region_query(X, j, eps)
        if len(j_neighbors) >= min_samples:
            queue.extend(j_neighbors)  # j is a core point, keep expanding


if __name__ == "__main__":
    from sklearn.datasets import make_moons
    from sklearn.cluster import DBSCAN

    X, _ = make_moons(n_samples=300, noise=0.07, random_state=42)
    ours = dbscan(X, eps=0.2, min_samples=5)
    theirs = DBSCAN(eps=0.2, min_samples=5).fit_predict(X)

    print("Clusters (ours):   ", len(set(ours) - {-1}), "| noise:", (ours == -1).sum())
    print("Clusters (sklearn):", len(set(theirs) - {-1}), "| noise:", (theirs == -1).sum())
