# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

## 1. What is DBSCAN?

DBSCAN stands for:

**Density-Based Spatial Clustering of Applications with Noise**

It is an **unsupervised clustering algorithm** that groups data points based on **density**.

Unlike K-Means, DBSCAN does not primarily depend on cluster centroids.

DBSCAN looks for areas where points are densely packed together and identifies sparse points as noise.

### Main idea

```text
Dense region  → Cluster
Sparse region → Noise

DBSCAN is especially useful when clusters have irregular or non-circular shapes.
For example, K-Means can struggle with moon-shaped clusters, while DBSCAN can detect them because it follows the density/connectivity of the points.
2. Why DBSCAN?
K-Means works well when clusters are relatively compact and centroid-based.
For example:
      ● ● ●
    ● ● ● ●
      ● ● ●

                    ● ● ●
                  ● ● ● ●
                    ● ● ●

K-Means can work well here because each group has a clear center.
But consider:
      ● ● ● ●
    ●         ●
   ●           ●

             ● ● ● ●
           ●         ●
          ●           ●

These are curved/non-convex clusters.
DBSCAN can identify them because it looks at density and connectivity, rather than assuming that every cluster should have a central point.
3. Important DBSCAN Parameters
DBSCAN mainly has two important parameters:
1. eps
2. min_samples
4. eps
eps means the maximum distance around a point that DBSCAN considers its neighborhood.
Think of it as a radius.
             ●
        ●    ●    ●
             ●
          ← eps →

In simple words:
eps answers: "How far should I look around this point?"

A larger eps means a larger neighborhood.
A smaller eps means a smaller neighborhood.
5. min_samples
min_samples specifies the minimum number of points required in the eps neighborhood for a point to be considered a core point.
In simple words:
min_samples answers: "How many points do I need to find in that neighborhood?"

Example:
eps = 0.2
min_samples = 5

means DBSCAN looks within a radius of 0.2 and requires enough nearby points to satisfy the density requirement of 5.
6. Core Point
A core point is a point that has enough points within its eps neighborhood to satisfy min_samples.
Conceptually:
        ●
     ●  ●  ●
       ●●
        ●

If enough points are packed together, the point can be considered a core point.
Core points are the main building blocks of DBSCAN clusters.
7. Border Point
A border point does not have enough nearby points to be a core point itself, but it lies within the neighborhood of a core point.
Conceptually:
       Core region

      ● ● ●
    ● ● ● ● ●
      ● ● ●

             ●
          Border

The border point is not dense enough by itself, but it is close enough to a dense region to belong to that cluster.
8. Noise Point
A noise point is a point that does not belong to a sufficiently dense region and is not connected to a core point in the required way.
DBSCAN represents noise using:
-1


Example:
● ● ● ●
 ● ● ●
● ● ●

                 ●
                       ← Noise

Noise is one of the important advantages of DBSCAN.
K-Means generally assigns every point to a cluster, whereas DBSCAN can explicitly identify points as noise.
9. Basic DBSCAN Workflow
The overall process is:
Choose eps
     ↓
Choose min_samples
     ↓
Find neighborhoods
     ↓
Identify core points
     ↓
Connect density-connected points
     ↓
Assign border points
     ↓
Identify noise
     ↓
Create clusters

10. DBSCAN with Scikit-Learn
Basic implementation:
from sklearn.cluster import DBSCANmodel = DBSCAN(    eps=0.2,    min_samples=5)labels = model.fit_predict(X)


fit_predict():
1. Fits DBSCAN to the data.
2. Assigns a cluster label to every observation.
3. Returns those labels.
11. Understanding DBSCAN Labels
Suppose:
labels


contains:
[0, 0, 0, 1, 1, 1, -1]

Then:
0  → Cluster 0
1  → Cluster 1
-1 → Noise

Important:
DBSCAN cluster numbers are just labels. Cluster 0 is not inherently better or more important than Cluster 1.

12. Our Make-Moons Dataset
We practiced DBSCAN using a two-moon dataset.
The dataset had:
300 observations
2 features

The data had two curved structures.
This is a good example for DBSCAN because the clusters are not simple circular/centroid-shaped groups.
13. DBSCAN Visualization
Our DBSCAN plot showed two curved groups.
The important point was that DBSCAN successfully followed the shape of the two moon structures.
This demonstrates why density-based clustering can be useful for non-convex data.
14. Cluster Sizes
We used:
pd.Series(labels).value_counts().sort_index()


to inspect cluster sizes.
For our selected DBSCAN model:
0    150
1    150

So:
Cluster 0 → 150 points
Cluster 1 → 150 points

Total:
150 + 150 = 300

15. Counting the Number of Clusters
DBSCAN uses -1 for noise.
Therefore, when counting clusters, we should exclude -1.
We used:
n_clusters = len(    set(labels) - {-1})


Explanation:
set(labels)


gets the unique labels.
For example:
{-1, 0, 1}

Then:
set(labels) - {-1}


removes the noise label.
Result:
{0, 1}

Then:
len(...)


counts them.
Therefore:
Number of clusters = 2

16. Counting Noise Points
We used:
n_noise = (labels == -1).sum()


Explanation:
labels == -1


creates a Boolean array.
For example:
[False, False, True, False, True]

Then:
.sum()


counts the True values.
Therefore it tells us how many observations DBSCAN classified as noise.
17. Counting Core Points
DBSCAN stores the indices of its core points in:
model.core_sample_indices_


Therefore:
n_core = len(    model.core_sample_indices_)


gives the number of core points.
18. Our First DBSCAN Parameter Experiment: Changing eps
We tested:
for eps in [0.05, 0.10, 0.20, 0.30, 0.50]:


with:
min_samples = 5


Our results were:
eps = 0.05
Clusters     = 4
Core points  = 5
Noise points = 279


eps = 0.10
Clusters     = 19
Core points  = 170
Noise points = 60


eps = 0.20
Clusters     = 2
Core points  = 295
Noise points = 0


eps = 0.30
Clusters     = 2
Core points  = 300
Noise points = 0


eps = 0.50
Clusters     = 1
Core points  = 300
Noise points = 0

19. Effect of Very Small eps
At:
eps = 0.05

we obtained:
4 clusters
5 core points
279 noise points

The neighborhood is extremely small.
Therefore, most points cannot find enough neighbors.
Result:
Small eps
   ↓
Small neighborhoods
   ↓
Few core points
   ↓
Many noise points
   ↓
Clusters can become fragmented

20. eps = 0.10
At:
eps = 0.10

we obtained:
19 clusters
170 core points
60 noise points

The neighborhood is larger than 0.05, but it is still relatively small.
The data becomes fragmented into many smaller clusters.
21. eps = 0.20
At:
eps = 0.20

we obtained:
2 clusters
295 core points
0 noise points

Cluster sizes:
Cluster 0 → 150
Cluster 1 → 150

This successfully captured the two moon structures.
22. eps = 0.30
At:
eps = 0.30

we obtained:
2 clusters
300 core points
0 noise points

The clusters were still separated.
However, all 300 observations were now considered core points.
23. eps = 0.50
At:
eps = 0.50

we obtained:
1 cluster
300 core points
0 noise points

The neighborhood became too large.
Points from the two structures became density-connected.
Therefore:
Two clusters
     ↓
Connected together
     ↓
One cluster

24. Important eps Pattern
The overall pattern is:
eps too small
    ↓
Few connections
    ↓
Fragmented clusters + noise


eps appropriate
    ↓
Useful density connections
    ↓
Meaningful clusters


eps too large
    ↓
Too many connections
    ↓
Clusters merge

So choosing eps is important.
25. Second DBSCAN Parameter Experiment: min_samples
We kept:
eps = 0.2


and changed:
min_samples


We tested:
[3, 5, 10, 15, 20]


Results:
min_samples = 3
Clusters     = 2
Core points  = 300
Noise points = 0


min_samples = 5
Clusters     = 2
Core points  = 295
Noise points = 0


min_samples = 10
Clusters     = 2
Core points  = 258
Noise points = 1


min_samples = 15
Clusters     = 4
Core points  = 156
Noise points = 10


min_samples = 20
Clusters     = 6
Core points  = 14
Noise points = 159

26. Effect of min_samples
As min_samples increases:
min_samples increases
        ↓
Density requirement increases
        ↓
Fewer points qualify as core
        ↓
More points can become noise
        ↓
Clusters can become fragmented

27. min_samples = 3
Results:
Core points  = 300
Noise points = 0
Clusters     = 2

The density requirement is relatively low.
Therefore, every point became a core point.
28. min_samples = 5
Results:
Core points  = 295
Noise points = 0
Clusters     = 2

Only a few observations were not core points.
The two clusters remained:
150 + 150

29. min_samples = 10
Results:
Core points  = 258
Noise points = 1
Clusters     = 2

The density requirement increased.
Some points no longer qualified as core points.
One point became noise.
The two major structures were still preserved.
30. min_samples = 15
Results:
Core points  = 156
Noise points = 10
Clusters     = 4

Increasing the density requirement started breaking the original structures into smaller dense regions.
Cluster sizes:
Cluster 0 → 131
Cluster 1 → 127
Cluster 2 → 22
Cluster 3 → 10

Noise → 10

Important:
Increasing min_samples can cause clusters to become fragmented, not just increase the number of noise points.

31. min_samples = 20
Results:
Core points  = 14
Noise points = 159
Clusters     = 6

The density requirement became very strict.
Only 14 points qualified as core points.
Most of the dataset became noise.
159 / 300 ≈ 53%

So more than half of the observations were classified as noise.
32. eps vs min_samples
The easiest way to remember them:
eps
↓
"How far should I look?"

and:
min_samples
↓
"How many points do I need there?"

Together:
DBSCAN
 │
 ├── eps
 │     └── Neighborhood size
 │
 └── min_samples
       └── Density requirement

33. Choosing eps More Systematically
Instead of randomly trying many eps values, we used a k-distance graph.
The purpose is to find a reasonable candidate range for eps.
34. K-Distance Graph
We used:
from sklearn.neighbors import NearestNeighborsk = 5neighbors = NearestNeighbors(    n_neighbors=k)neighbors.fit(X)distances, indices = neighbors.kneighbors(X)


Because:
min_samples = 5

we used:
k = 5

35. Shape of the Distance Array
We obtained:
(300, 5)

because:
300 observations
×
5 nearest neighbors

The distances array contains the distances to the nearest neighbors for every point.
36. Selecting the 5th-Nearest Distance
Python uses zero-based indexing.
Therefore:
distances[:, 4]


means:
Take the 5th-nearest-neighbor distance for every observation.

We stored it as:
k_distances = distances[:, 4]


37. Sorting the Distances
We used:
k_distances = np.sort(k_distances)


This sorts the distances from smallest to largest.
Then we plotted them.
plt.figure(figsize=(8, 5))plt.plot(k_distances)plt.xlabel("Points sorted by distance")plt.ylabel("5th Nearest Neighbor Distance")plt.title("K-Distance Graph")plt.show()


38. Understanding the K-Distance Graph
Dense regions contain points that are close together.
Therefore:
Dense region
    ↓
Small 5th-neighbor distance

Sparse regions contain points that are farther apart.
Therefore:
Sparse region
    ↓
Large 5th-neighbor distance

After sorting the distances, we look for the point where the curve begins to rise sharply.
This is commonly called the:
Knee

or:
Elbow

39. Our K-Distance Graph
Our graph showed the curve beginning to rise more sharply around approximately:
0.18 – 0.20

This suggested a reasonable candidate range for:
eps ≈ 0.18 – 0.20

We had already tested:
eps = 0.20

and it produced:
2 clusters
295 core points
0 noise points
150 + 150

So the k-distance graph supported the result we observed experimentally.
Important:
The k-distance graph does not magically give one exact eps value. It gives a reasonable region to investigate, which should then be tested and validated.

40. DBSCAN Silhouette Score
We can evaluate DBSCAN using:
from sklearn.metrics import silhouette_scorescore = silhouette_score(    X,    labels)


For our selected model:
eps = 0.2
min_samples = 5

we obtained:
Silhouette Score = 0.32725577868299804

Approximately:
0.3273

41. Why Was the Silhouette Score Only About 0.327?
Our DBSCAN model correctly identified the two moon-shaped structures.
However, the Silhouette Score is based on distances between points.
The moon-shaped clusters are curved/non-convex.
Therefore, points from different clusters can sometimes be geometrically close even though they belong to different density-connected structures.
So:
Good density-based structure
        ≠
Necessarily very high Silhouette Score

Important:
A relatively modest Silhouette Score does not automatically mean DBSCAN failed.

For DBSCAN, we should also consider:
- cluster shape
- density connectivity
- noise points
- number of clusters
- visualization
- domain meaning
42. Noise and Silhouette Score
DBSCAN uses:
-1

for noise.
If noise exists, we should be careful when calculating the Silhouette Score because noise is not really a meaningful cluster.
We can exclude noise:
mask = labels != -1score = silhouette_score(    X[mask],    labels[mask])


This calculates the Silhouette Score using only points belonging to actual clusters.
For our selected model:
Noise points = 0

Therefore, there was no noise to remove.
43. Core Point Visualization
DBSCAN provides:
model.core_sample_indices_


This contains the indices of the core points.
We can create a Boolean mask:
core_mask = np.zeros(    len(X),    dtype=bool)core_mask[    model.core_sample_indices_] = True


Now:
core_mask = True

for core points and:
core_mask = False

for non-core points.
44. Non-Core / Border Mask
We can create:
border_mask = ~core_mask


The ~ operator means Boolean NOT.
Therefore:
True  → False
False → True

So border_mask identifies the observations that are not core points.
Important:
In a complete DBSCAN result, non-core points can include border points and noise points. Therefore, calling every non-core point a border point is not always technically correct.

45. Important Error We Encountered
We initially attempted to plot core and border points but got:
ValueError:
'c' argument has 295 elements, which is inconsistent
with 'x' and 'y' with size 5.

The problem was that the masks were mixed up.
The incorrect code effectively tried to plot:
X[border_mask]


while using:
labels[core_mask]


Those arrays have different numbers of observations.
For example:
X[border_mask]  → 5 points
labels[core_mask] → 295 labels

Matplotlib requires the number of colors/labels to match the number of plotted points.
46. General Rule for Boolean Masks
Whenever we write:
X[mask]


and:
labels[mask]


the same mask should normally be used if we want the labels to correspond to those points.
For example:
X[core_mask]labels[core_mask]


both refer to the same observations.
Similarly:
X[border_mask]labels[border_mask]


both refer to the same observations.
47. DBSCAN Complete Example
A basic DBSCAN implementation:
from sklearn.cluster import DBSCANimport pandas as pdimport numpy as npmodel = DBSCAN(    eps=0.2,    min_samples=5)labels = model.fit_predict(X)n_clusters = len(    set(labels) - {-1})n_noise = (    labels == -1).sum()n_core = len(    model.core_sample_indices_)print("No of Clusters:", n_clusters)print("No of Core Points:", n_core)print("No of Noise Points:", n_noise)print("Cluster Sizes:")print(    pd.Series(labels)    .value_counts()    .sort_index())


48. Our Final DBSCAN Result
For:
eps = 0.2min_samples = 5


we obtained:
Number of clusters = 2
Core points        = 295
Noise points       = 0
Cluster 0          = 150
Cluster 1          = 150
Silhouette Score   = 0.3273

The visualization showed that the two moon-shaped structures were successfully identified.
49. DBSCAN vs K-Means vs Hierarchical Clustering
K-Means
Main idea:
Centroids
   ↓
Assign points to nearest centroid
   ↓
Update centroids
   ↓
Repeat

Good for:
- compact clusters
- roughly spherical/convex clusters
- situations where a centroid-based partition makes sense
Requires:
Number of clusters K

Hierarchical Clustering
Main idea:
Individual points
       ↓
Merge similar points/clusters
       ↓
Build hierarchy
       ↓
Choose a cut

Can be visualized using a dendrogram.
Does not require choosing the final number of clusters in exactly the same way as K-Means at the start, because the hierarchy can be cut at different levels.
DBSCAN
Main idea:
Density
   ↓
Core points
   ↓
Density-connected regions
   ↓
Clusters
   ↓
Noise

Requires:
eps
min_samples

Can identify:
- irregularly shaped clusters
- dense regions
- noise/outliers
50. Most Important Comparison
K-Means
→ "Where are the centers?"

Hierarchical
→ "Which points/clusters are similar enough to merge?"

DBSCAN
→ "Where are the dense regions?"

51. When to Think About DBSCAN
DBSCAN is particularly useful when:
✓ Clusters have irregular shapes
✓ Data contains possible outliers/noise
✓ You want density-based clustering
✓ You don't want to force every point into a cluster

Be careful when:
✗ Density varies greatly between clusters
✗ Choosing eps is difficult
✗ High-dimensional distance becomes problematic

52. Final DBSCAN Cheat Sheet
DBSCAN
│
├── eps
│   └── Neighborhood radius
│
├── min_samples
│   └── Minimum density requirement
│
├── Core Point
│   └── Enough nearby points
│
├── Border Point
│   └── Near a core region but not dense enough itself
│
├── Noise
│   └── Label = -1
│
├── Clusters
│   └── Density-connected regions
│
└── K-Distance Graph
    └── Helps choose a candidate eps

53. Key Lessons From Our Practical
Lesson 1
DBSCAN is density-based, not centroid-based.
Lesson 2
eps controls:
How far DBSCAN looks around each point.

Lesson 3
min_samples controls:
How many nearby points are required for sufficient density.

Lesson 4
Small eps can cause:
Fragmentation + noise

Lesson 5
Large eps can cause:
Different clusters to merge

Lesson 6
Large min_samples makes the density requirement stricter.
Lesson 7
DBSCAN can identify noise using:
label = -1

Lesson 8
The k-distance graph can help select a reasonable candidate eps.
Lesson 9
Silhouette Score is useful, but it should not be the only consideration for DBSCAN, especially for non-convex clusters.
Lesson 10
DBSCAN is especially valuable when the cluster structure is based on density and shape rather than simply distance from a centroid.
54. Our Clustering Learning Progress
We have now practiced:
1. K-Means
   ↓
   - K
   - Inertia
   - Elbow Method
   - Silhouette Score
   - Cluster sizes
   - Centroids
   - Cluster vs target comparison

2. Hierarchical Clustering
   ↓
   - Agglomerative clustering
   - Number of clusters
   - Dendrogram concept
   - Silhouette Score
   - Cluster sizes
   - Cluster vs target comparison

3. DBSCAN
   ↓
   - eps
   - min_samples
   - Core points
   - Border points
   - Noise
   - Cluster sizes
   - K-distance graph
   - Silhouette Score
   - Density-based clustering

The most important conceptual distinction to remember is:
K-Means
→ Centroid-based

Hierarchical Clustering
→ Hierarchy/merging-based

DBSCAN
→ Density-based