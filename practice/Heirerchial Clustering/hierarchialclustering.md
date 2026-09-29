# Hierarchical Clustering

## 1. What is Hierarchical Clustering?

Hierarchical Clustering is an **unsupervised machine learning algorithm** used to group similar data points into clusters.

Unlike K-Means, Hierarchical Clustering creates a hierarchy of clusters.

The hierarchy can be visualized using a **Dendrogram**.

The main idea is:

1. Start with individual data points.
2. Calculate distances between points/clusters.
3. Merge the closest clusters.
4. Continue merging.
5. Create a hierarchy of all the merges.
6. Cut the hierarchy at a particular level to obtain the final clusters.

---

# 2. Types of Hierarchical Clustering

There are two main approaches:

### Agglomerative Hierarchical Clustering

Bottom-up approach.

```text
Each observation starts as its own cluster
                ↓
Merge closest clusters
                ↓
Merge again
                ↓
Continue until one cluster remains

This is the approach we used with AgglomerativeClustering.
Divisive Hierarchical Clustering
Top-down approach.
Start with one large cluster
                ↓
Split the cluster
                ↓
Split again
                ↓
Continue until individual clusters are created

In practice, Agglomerative Hierarchical Clustering is much more commonly used with scikit-learn.
3. Agglomerative Clustering
Agglomerative clustering follows a bottom-up approach.
Suppose we have:
A   B   C   D

Initially:
Cluster 1 → A
Cluster 2 → B
Cluster 3 → C
Cluster 4 → D

The algorithm finds the closest clusters and merges them.
For example:
A + B

Now:
Cluster 1 → {A,B}
Cluster 2 → C
Cluster 3 → D

Then it continues:
{A,B} + C

and eventually:
{A,B,C,D}

The complete sequence of merges forms a hierarchy.
4. Why Do We Need Linkage?
When every observation is an individual cluster, calculating distance is simple.
But after clusters are formed, we need to answer:
How do we calculate the distance between two clusters?

This is where linkage comes in.
Linkage defines how the distance between two clusters is calculated.
The main linkage methods are:
1. Single Linkage
2. Complete Linkage
3. Average Linkage
4. Ward Linkage
5. Single Linkage
Single linkage uses the minimum distance between observations from two clusters.
Single Linkage
= minimum distance between two clusters

Example:
Cluster A = {A1, A2, A3}
Cluster B = {B1, B2, B3}

Calculate all pairwise distances between A and B.
Single linkage chooses the smallest distance.
Advantage
Can identify elongated or irregularly shaped clusters.
Disadvantage
Can suffer from the chaining effect.
A sequence of nearby observations can cause clusters to gradually connect together.
Memory Trick
Single → Closest

6. Complete Linkage
Complete linkage uses the maximum distance between observations from two clusters.
Complete Linkage
= maximum distance between two clusters

It considers the farthest pair of observations between the two clusters.
Complete linkage generally produces more compact clusters than single linkage.
Memory Trick
Complete → Farthest

7. Average Linkage
Average linkage calculates the average distance between all pairs of observations across the two clusters.
Average Linkage
= average pairwise distance between two clusters

It is between single and complete linkage because it doesn't only consider the closest or farthest pair.
Memory Trick
Average → Average distance

8. Ward Linkage
Ward linkage works differently from the other linkage methods.
It chooses the merge that causes the smallest increase in within-cluster variance.
The goal is to keep clusters as compact as possible.
Ward
→ minimize increase in within-cluster variance

Ward linkage is commonly used when clusters are expected to be relatively compact.
We used Ward linkage throughout our Iris dataset example.
Memory Trick
Ward → Variance

9. Linkage Comparison
Linkage	Main Idea
Single	Minimum distance
Complete	Maximum distance
Average	Average distance
Ward	Minimum increase in within-cluster variance


Easy way to remember:
Single   → Closest
Complete → Farthest
Average  → Average
Ward     → Variance

10. Dendrogram
A dendrogram is a tree-like diagram that shows the hierarchy of cluster merging.
It tells us:
- Which clusters were merged
- When they were merged
- The distance at which they were merged
- How the hierarchy was constructed
Example concept:
Distance
   |
   |             ┌─────────────┐
   |        ┌────┘             │
   |   ┌────┘                  │
   |   │                       │
   | ┌─┴─┐                 ┌───┴───┐
   | A   B                 C       D
   |
   +--------------------------------

The vertical height of a merge represents the distance at which the merge occurred.
11. Why is the Dendrogram Important?
The dendrogram helps us decide where to cut the hierarchy.
A horizontal line can be imagined across the dendrogram.
The number of vertical branches that the line intersects represents the number of clusters.
Conceptually:
Dendrogram
     ↓
Choose a horizontal cut
     ↓
Count branches
     ↓
Number of clusters

A large vertical gap between merges can be a useful place to consider making the cut.
12. Creating a Linkage Matrix
We used SciPy:
from scipy.cluster.hierarchy import linkageZ = linkage(    X_scaled,    method="ward")


Z stores information about the hierarchical merging process.
The fourth column of the linkage matrix contains the distance at which each merge occurs.
We inspected:
Z_ward[-15:, 2]


and obtained:
[2.01781256,
 2.14172453,
 2.30338940,
 2.69536867,
 2.86888385,
 3.44191215,
 3.93266869,
 3.95076988,
 4.06134011,
 4.22703313,
 4.24348495,
 6.60781224,
 8.00474726,
 12.63684352,
 27.24991146]

The large jumps near the end were:
4.2435 → 6.6078
8.0047 → 12.6368
12.6368 → 27.2499

The very large jump:
12.6368 → 27.2499

shows that the final merge happens at a much larger distance.
13. Plotting the Dendrogram
from scipy.cluster.hierarchy import dendrogramimport matplotlib.pyplot as pltplt.figure(figsize=(12, 6))dendrogram(Z)plt.xlabel("Data Points")plt.ylabel("Distance")plt.title("Hierarchical Clustering Dendrogram")plt.show()


Because Iris contains 150 observations, the complete dendrogram can become difficult to read.
We can use:
plt.figure(figsize=(12, 6))dendrogram(    Z,    truncate_mode="lastp",    p=20)plt.xlabel("Clusters / Data Points")plt.ylabel("Distance")plt.title("Hierarchical Clustering Dendrogram")plt.show()


Here:
truncate_mode="lastp"


shows the final portion of the hierarchy.
And:
p=20


controls approximately how many final groups/merges are displayed.
14. Standardization Before Hierarchical Clustering
Our Iris dataset has four features:
sepal length
sepal width
petal length
petal width

We removed target because clustering is unsupervised.
X = df.drop("target", axis=1)


Then standardized the features:
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()X_scaled = scaler.fit_transform(X)


The resulting shape was:
(150, 4)

Standardization is important because hierarchical clustering is distance-based.
Without scaling, features with larger numerical scales can have a larger influence on distance calculations.
15. AgglomerativeClustering in Scikit-Learn
We used:
from sklearn.cluster import AgglomerativeClustering


For 3 clusters:
model = AgglomerativeClustering(    n_clusters=3,    linkage="ward")labels = model.fit_predict(X_scaled)


Then we added the labels to our DataFrame:
df["Hierarchial Clustering"] = labels


Note:
The cluster numbers are arbitrary.
Cluster 0
Cluster 1
Cluster 2

do not inherently mean:
Cluster 0 = Target 0
Cluster 1 = Target 1
Cluster 2 = Target 2

Cluster IDs are simply labels assigned by the algorithm.
16. Cluster Sizes
We checked cluster sizes using:
df["Hierarchial Clustering"].value_counts().sort_index()


For K = 3, Ward linkage gave:
Cluster 0 → 71
Cluster 1 → 49
Cluster 2 → 30

Total:
71 + 49 + 30 = 150

So all 150 observations were assigned to a cluster.
17. Silhouette Score
The Silhouette Score measures how well each observation fits within its assigned cluster compared with other clusters.
It considers:
- How close a point is to points in its own cluster
- How far it is from points in other clusters
The score ranges approximately from:
-1 to +1

General interpretation:
Closer to +1
→ clusters are well separated

Around 0
→ clusters overlap

Negative values
→ observations may be assigned to the wrong/overlapping cluster

We calculated it using:
from sklearn.metrics import silhouette_scorescore = silhouette_score(    X_scaled,    labels)print("Silhouette Score:", score)


For our hierarchical clustering with:
K = 3
linkage = Ward

we obtained:
Silhouette Score = 0.4466890410285909

18. Cross-Tabulation
Because the Iris dataset has a known target, we can examine how the unsupervised clusters correspond to the target values AFTER clustering.
Important:
target was NOT used to train the clustering model.
We used:
pd.crosstab(    df["target"],    df["Hierarchial Clustering"])


Our K = 3 result was:
Target	Cluster 0	Cluster 1	Cluster 2
0	0	49	1
1	23	0	27
2	48	0	2


Interpretation:
Target 0
Cluster 0 → 0
Cluster 1 → 49
Cluster 2 → 1

Almost all Target 0 observations were placed in Cluster 1.
Target 1
Cluster 0 → 23
Cluster 1 → 0
Cluster 2 → 27

Target 1 was split between Cluster 0 and Cluster 2.
Target 2
Cluster 0 → 48
Cluster 1 → 0
Cluster 2 → 2

Target 2 was almost entirely placed in Cluster 0.
This shows that Target 1 and Target 2 have more overlap in the feature space than Target 0 versus the other groups.
19. Distance Threshold
So far we used:
n_clusters=3


This means:
Give me exactly 3 clusters.

Agglomerative clustering also allows us to use:
distance_threshold


Instead of directly specifying the number of clusters.
Example:
model = AgglomerativeClustering(    n_clusters=None,    distance_threshold=10,    linkage="ward")labels_threshold = model.fit_predict(X_scaled)


When using distance_threshold, we set:
n_clusters=None


The algorithm keeps merging clusters until the specified distance threshold is reached.
20. Relationship Between Distance Threshold and Number of Clusters
The important relationship is:
Lower distance threshold
        ↓
Stop merging earlier
        ↓
More clusters

and:
Higher distance threshold
        ↓
Allow more merging
        ↓
Fewer clusters

We tested this on our Iris dataset.
Threshold = 5
Number of clusters = 5

Cluster sizes:
30
26
29
45
20

Threshold = 10
Number of clusters = 3

Cluster sizes:
71
49
30

Threshold = 15
Number of clusters = 2

Cluster sizes:
101
49

Therefore:
Distance Threshold	Number of Clusters
5	5
10	3
15	2


21. Why Did Threshold = 10 Give 3 Clusters?
Our final Ward merge distances included:
8.0047
12.6368
27.2499

Our threshold was:
10

Therefore:
8.0047 < 10

so that merge is allowed.
But:
12.6368 > 10

so the next merge is not allowed.
Therefore, the algorithm stops with:
3 clusters

This is directly related to cutting the dendrogram at a particular height.
22. Why Did Threshold = 5 Give 5 Clusters?
We had:
4.2435
6.6078

Our threshold was:
5

Therefore:
4.2435 < 5

but:
6.6078 > 5

The hierarchy is cut earlier, so more clusters remain.
Result:
5 clusters

23. Why Did Threshold = 15 Give 2 Clusters?
We had:
12.6368
27.2499

Our threshold was:
15

Therefore:
12.6368 < 15

but:
27.2499 > 15

More merging is allowed than with threshold 10.
Result:
2 clusters

24. Silhouette Analysis for Different K Values
We tested:
results = []for k in range(2, 8):    model = AgglomerativeClustering(        n_clusters=k,        linkage="ward"    )    labels = model.fit_predict(X_scaled)    score = silhouette_score(        X_scaled,        labels    )    results.append(score)    print(        f"K = {k}, "        f"Silhouette = {score:.4f}"    )


Our results were:
K	Silhouette Score
2	0.5770
3	0.4467
4	0.4006
5	0.3306
6	0.3149
7	0.3170


The scores generally decreased as K increased.
The highest silhouette score among the tested values was:
K = 2
Silhouette = 0.5770

25. Hierarchical Clustering with K = 2
We created:
model = AgglomerativeClustering(    n_clusters=2,    linkage="ward")labels_hc_2 = model.fit_predict(X_scaled)df["HC_K2"] = labels_hc_2


The cross-tabulation was:
Target	HC Cluster 0	HC Cluster 1
0	1	49
1	50	0
2	50	0


Therefore:
Cluster 0 → 100 observations
Cluster 1 → 50 observations

The two clusters approximately separated:
Cluster 1
→ Target 0

Cluster 0
→ Target 1 + Target 2

This explains why the K = 2 solution had a relatively high silhouette score.
The data has a strong separation between Target 0 and the combined Target 1/Target 2 group.
26. Comparing K-Means and Hierarchical Clustering
Our K-Means results were:
K = 2
Silhouette = 0.58175

K = 3
Silhouette = 0.45995

Our Ward Hierarchical results were:
K = 2
Silhouette = 0.5770

K = 3
Silhouette = 0.4467

Comparison:
Algorithm	K	Silhouette
K-Means	2	0.58175
Hierarchical - Ward	2	0.5770
K-Means	3	0.45995
Hierarchical - Ward	3	0.4467


The two algorithms showed a similar pattern on the Iris dataset.
Both produced higher silhouette scores for K = 2 than K = 3.
27. Important Difference Between K-Means and Hierarchical Clustering
K-Means
K-Means works using cluster centroids.
General process:
Choose K
    ↓
Initialize centroids
    ↓
Assign points to nearest centroid
    ↓
Recalculate centroids
    ↓
Reassign points
    ↓
Repeat
    ↓
Final clusters

Hierarchical Clustering
Agglomerative clustering works by progressively merging clusters.
Each point starts as its own cluster
    ↓
Find closest clusters
    ↓
Merge
    ↓
Merge again
    ↓
Continue
    ↓
Hierarchy / Dendrogram
    ↓
Choose a cut
    ↓
Final clusters

28. Key Difference: K-Means vs Hierarchical
Feature	K-Means	Hierarchical
Type	Unsupervised	Unsupervised
Requires K	Yes	Can use K or distance threshold
Main concept	Centroids	Hierarchy
Output	Clusters	Hierarchy + clusters
Visualization	Scatter plots	Dendrogram
Distance concept	Point to centroid	Cluster-to-cluster linkage
Can use distance threshold	No	Yes
Main hyperparameter	n_clusters	n_clusters, linkage, distance_threshold


29. Important Practical Workflow
For Hierarchical Clustering, a good workflow is:
Load dataset
      ↓
Explore dataset
      ↓
Separate features and target
      ↓
Handle missing values if necessary
      ↓
Scale features
      ↓
Create linkage matrix
      ↓
Plot dendrogram
      ↓
Choose linkage method
      ↓
Investigate possible number of clusters
      ↓
Create AgglomerativeClustering model
      ↓
Generate labels
      ↓
Check cluster sizes
      ↓
Calculate Silhouette Score
      ↓
Visualize clusters
      ↓
Analyze cluster composition
      ↓
Compare different K values
      ↓
Interpret results

30. Important Code Template
A basic complete implementation:
import pandas as pdimport matplotlib.pyplot as pltfrom sklearn.preprocessing import StandardScalerfrom sklearn.cluster import AgglomerativeClusteringfrom sklearn.metrics import silhouette_scorefrom scipy.cluster.hierarchy import linkage, dendrogram# -----------------------------# 1. Separate features# -----------------------------X = df.drop("target", axis=1)# -----------------------------# 2. Standardize# -----------------------------scaler = StandardScaler()X_scaled = scaler.fit_transform(X)# -----------------------------# 3. Create linkage matrix# -----------------------------Z = linkage(    X_scaled,    method="ward")


31. Important Concepts to Remember
Hierarchical Clustering
Unsupervised clustering method that builds a hierarchy of clusters.
Agglomerative Clustering
Bottom-up hierarchical clustering.
Individual points
→ merge
→ merge
→ merge
→ hierarchy

Dendrogram
Visual representation of the hierarchy.
Linkage
Defines how distance between clusters is calculated.
Single Linkage
Minimum distance.
Complete Linkage
Maximum distance.
Average Linkage
Average distance.
Ward Linkage
Minimizes the increase in within-cluster variance.
n_clusters
Specifies the desired number of final clusters.
distance_threshold
Controls when hierarchical merging stops.
Silhouette Score
Measures cluster cohesion and separation.
32. Most Important Memory Summary
Hierarchical Clustering
        ↓
Agglomerative
        ↓
Start with individual points
        ↓
Merge clusters
        ↓
Linkage determines cluster distance
        ↓
Dendrogram shows hierarchy
        ↓
Cut hierarchy
        ↓
Final clusters

Linkage:
Single   → Minimum distance
Complete → Maximum distance
Average  → Average distance
Ward     → Minimum increase in variance

Threshold:
Lower threshold
→ Less merging
→ More clusters

Higher threshold
→ More merging
→ Fewer clusters

Evaluation:
Silhouette Score
→ Measures cohesion + separation
→ Higher value generally indicates better-separated clusters

33. Final Takeaway
The biggest difference from K-Means is that Hierarchical Clustering does not simply jump directly to a fixed set of clusters.
It first builds a hierarchy of merges.
The dendrogram lets us see that hierarchy.
We can then obtain clusters by:
1. Specifying n_clusters

or:
2. Specifying distance_threshold

For our Iris dataset, we observed:
Distance Threshold = 5
→ 5 clusters

Distance Threshold = 10
→ 3 clusters

Distance Threshold = 15
→ 2 clusters

And with Ward linkage:
K = 2 → Silhouette = 0.5770
K = 3 → Silhouette = 0.4467
K = 4 → Silhouette = 0.4006
K = 5 → Silhouette = 0.3306
K = 6 → Silhouette = 0.3149
K = 7 → Silhouette = 0.3170