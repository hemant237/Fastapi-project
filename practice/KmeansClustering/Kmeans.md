# K-Means Clustering

## 1. What is K-Means Clustering?

K-Means is an **unsupervised machine learning algorithm** used for **clustering**.

Clustering means grouping similar observations together.

Unlike supervised learning, K-Means does not require a target variable (`y`) during training.

### Supervised Learning

```text
X + y
 ↓
Model
 ↓
Prediction

Example:
Features → House Price

Unsupervised Learning
X
 ↓
Model
 ↓
Groups / Clusters

Example:
Customer data
     ↓
K-Means
     ↓
Customer segments

2. What Does K-Means Try to Do?
K-Means tries to divide the dataset into K groups called clusters.
Each cluster has a centroid.
The centroid represents the center of that cluster.
Conceptually:
             Cluster 1
          ● ● ● ● ●
        ● ● ● ● ● ●
             X
          Centroid

                    Cluster 2
                 ● ● ● ● ●
               ● ● ● ● ●
                    X
                 Centroid

The algorithm tries to assign each observation to the nearest centroid.
3. What is K?
K represents the number of clusters we want.
For example:
K = 2


means:
Create 2 clusters

And:
K = 3


means:
Create 3 clusters

Choosing K is one of the important parts of K-Means.
4. What is a Cluster?
A cluster is a group of observations that are relatively similar to each other.
Example:
Cluster 1:
● ● ● ●
 ● ● ●

Cluster 2:

                 ● ● ●
               ● ● ● ●

The observations inside a cluster should generally be close to each other, while different clusters should ideally be reasonably separated.
5. What is a Centroid?
A centroid is the mean position of the observations belonging to a cluster.
Suppose we have three points:
(2, 4)
(4, 6)
(6, 8)

The centroid is:
x = (2 + 4 + 6) / 3 = 4

y = (4 + 6 + 8) / 3 = 6

Therefore:
Centroid = (4, 6)

So the centroid is essentially the average location of the points in that cluster.
6. How K-Means Works
The basic K-Means algorithm works like this:
1. Choose K
       ↓
2. Initialize K centroids
       ↓
3. Calculate distance from every point
   to every centroid
       ↓
4. Assign each point to the nearest centroid
       ↓
5. Calculate the mean of each cluster
       ↓
6. Move the centroids to those means
       ↓
7. Repeat steps 3–6
       ↓
8. Stop when the centroids/assignments converge

7. K-Means Intuition
Suppose we choose:
K = 3

Initially, we have three centroids.
The algorithm calculates the distance from every observation to these centroids.
Each observation is assigned to the closest centroid.
Then the centroid is moved to the average position of its assigned points.
This process repeats until the clusters stabilize.
8. Distance in K-Means
K-Means commonly uses Euclidean distance.
For two points:
A = (x1, y1)

B = (x2, y2)

Euclidean distance is:
distance = √[(x1 - x2)² + (y1 - y2)²]

Example:
A = (2, 3)
B = (5, 7)

Then:
distance
= √[(2 - 5)² + (3 - 7)²]

= √[(-3)² + (-4)²]

= √[9 + 16]

= √25

= 5

9. Why Feature Scaling is Important
K-Means is a distance-based algorithm.
Therefore, feature scale can affect the result.
Suppose:
Feature A → 0 to 1000

Feature B → 0 to 5

Feature A can have a much larger influence on Euclidean distance.
Therefore, we generally scale features before applying K-Means.
10. StandardScaler
A common approach is:
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()X_scaled = scaler.fit_transform(X)


StandardScaler transforms each feature approximately so that:
Mean ≈ 0
Standard deviation ≈ 1

The transformation is:
z = (x - mean) / standard_deviation

11. Why We Don't Give the Target to K-Means
K-Means is an unsupervised algorithm.
Therefore, during training:
X = df.drop("target", axis=1)


We do NOT use the target as a training input.
The workflow is:
Dataset
   ↓
Separate target
   ↓
X = features
y = target
   ↓
K-Means uses X only

The target can be used later for analysis if the original labels are available.
12. Choosing K
One of the main questions in K-Means is:
How many clusters should we create?

Two useful methods are:
1. Elbow Method
2. Silhouette Score
13. Elbow Method
The Elbow Method uses inertia.
Inertia
Inertia is the:
Sum of squared distances between each observation and the centroid of the cluster it belongs to.

Conceptually:
Point
  ↓
Distance to assigned centroid
  ↓
Square distance
  ↓
Repeat for all points
  ↓
Add everything
  ↓
Inertia

Lower inertia means observations are, overall, closer to their assigned centroids.
14. Why Can't We Simply Choose the Lowest Inertia?
Because increasing K generally decreases inertia.
For example:
K = 1 → high inertia

K = 2 → lower inertia

K = 3 → lower

K = 4 → lower

...

K = 10 → even lower

If we simply chose the lowest inertia, we would keep increasing K.
Therefore, we look for an elbow where the improvement begins to become smaller.
15. Elbow Method Code
from sklearn.cluster import KMeansimport matplotlib.pyplot as pltinertia = []for k in range(1, 11):    kmeans = KMeans(        n_clusters=k,        init="k-means++",        n_init=10,        random_state=42    )    kmeans.fit(X_scaled)    inertia.append(kmeans.inertia_)


Plot:
plt.figure(figsize=(7, 5))plt.plot(    range(1, 11),    inertia,    marker="o")plt.xlabel("Number of Clusters (K)")plt.ylabel("Inertia")plt.title("Elbow Method")plt.show()


We look for the point where the curve starts to flatten.
16. Silhouette Score
The Silhouette Score measures how well each observation fits within its cluster compared with other clusters.
It considers:
- How close an observation is to observations in its own cluster
- How close it is to observations in neighboring clusters
The score generally ranges from:
-1 to +1

Interpretation:
Closer to +1
→ Stronger separation

Around 0
→ Clusters overlap / observation is near a boundary

Negative
→ Observation may be assigned to an inappropriate cluster

A higher average silhouette score generally indicates stronger cluster separation and cohesion.
17. Silhouette Score Code
from sklearn.metrics import silhouette_scoresilhouette_scores = []for k in range(2, 11):    kmeans = KMeans(        n_clusters=k,        init="k-means++",        n_init=10,        random_state=42    )    labels = kmeans.fit_predict(X_scaled)    score = silhouette_score(        X_scaled,        labels    )    silhouette_scores.append(score)


Plot:
plt.figure(figsize=(7, 5))plt.plot(    range(2, 11),    silhouette_scores,    marker="o")plt.xlabel("Number of Clusters (K)")plt.ylabel("Silhouette Score")plt.title("Silhouette Score vs Number of Clusters")plt.show()


18. Elbow vs Silhouette
Elbow Method and Silhouette Score can suggest different values of K.
This is not necessarily an error.
They measure different aspects.
Elbow Method
Looks at:
Inertia
↓
Within-cluster squared distances

Silhouette Score
Looks at:
Cluster cohesion
+
Cluster separation

Therefore:
Elbow → may suggest K = 3

Silhouette → may suggest K = 2

This can happen in real datasets.
The decision should consider the metric results, data structure, visualization, domain knowledge, and practical purpose.
19. K-Means++ Initialization
In our implementation we used:
init="k-means++"


K-Means++ is an initialization strategy designed to choose initial centroids in a more effective way than simply choosing arbitrary points.
It generally spreads the initial centroids apart rather than placing them all very close together.
20. n_init
We used:
n_init=10


K-Means can produce different results depending on its initial centroid positions.
n_init=10 means the initialization/training process is attempted multiple times and the best result is selected.
This helps reduce the effect of a poor initialization.
21. random_state
We used:
random_state=42


This makes the random initialization reproducible.
If we run the same code with the same data and settings, we can reproduce the same result.
The number 42 has no special mathematical meaning here.
22. Complete K-Means Workflow
The general workflow is:
Load data
   ↓
EDA
   ↓
Check missing values
   ↓
Separate target if present
   ↓
Select features
   ↓
Scale features
   ↓
Test different K values
   ↓
Elbow Method
   ↓
Silhouette Score
   ↓
Choose K
   ↓
Train K-Means
   ↓
Get cluster labels
   ↓
Analyze cluster sizes
   ↓
Analyze centroids
   ↓
Visualize clusters
   ↓
Interpret clusters

23. Iris Dataset — Practical Project
We practiced K-Means using the Iris dataset.
The dataset contained:
150 rows
5 columns

The columns were:
sepal length (cm)
sepal width (cm)
petal length (cm)
petal width (cm)
target

The first four columns were features.
The target column represented the known Iris classes.
24. Initial Data Check
We checked:
df.shape


Result:
(150, 5)

We checked:
df.info()


There were:
4 float features
1 integer target

We also checked missing values:
df.isnull().sum()


Result:
sepal length (cm)    0
sepal width (cm)     0
petal length (cm)    0
petal width (cm)     0
target               0

Therefore, there were no missing values.
25. Separate Features
We created:
X = df.drop("target", axis=1)


Then:
X.shape


gave:
(150, 4)

So:
150 observations
4 features

26. Pairplot
We used:
import seaborn as snsimport matplotlib.pyplot as pltsns.pairplot(    df,    hue="target")plt.show()


This was used only for visualization.
We did NOT use target during K-Means training.
The pairplot showed that:
- One group was relatively well separated.
- The other two groups had more overlap.
- Petal length and petal width were particularly informative.
27. Scale the Features
We used:
from sklearn.preprocessing import StandardScalerscaler = StandardScaler()X_scaled = scaler.fit_transform(X)


Then:
X_scaled.shape


gave:
(150, 4)

Example of the first row:
Original:

5.1   3.5   1.4   0.2

After scaling, approximately:
-0.90   1.02   -1.34   -1.32

28. Elbow Method on Iris
We calculated inertia for:
K = 1 to 10

Our inertia values were:
K = 1  → 600.00
K = 2  → 222.36
K = 3  → 139.82
K = 4  → 114.09
K = 5  → 90.93
K = 6  → 81.54
K = 7  → 72.63
K = 8  → 62.54
K = 9  → 55.12
K = 10 → 47.39

The elbow appeared approximately around:
K ≈ 3

29. Silhouette Score on Iris
We calculated:
K = 2 → 0.58175
K = 3 → 0.45995
K = 4 → 0.38694
K = 5 → 0.34590
K = 6 → 0.31708
K = 7 → 0.32020
K = 8 → 0.33869
K = 9 → 0.34236
K = 10 → 0.35179

The highest silhouette score occurred at:
K = 2

This was an important observation because the Elbow Method suggested approximately 3 while the silhouette score was highest at 2.
This difference occurs because the metrics evaluate different aspects of clustering.
30. Comparing K = 2 and K = 3
We correctly calculated:
K = 2

Inertia:
222.36170496502308

Silhouette:
0.5817500491982808

Cluster sizes:
0 → 100
1 → 50

For K = 3:
K = 3

Inertia:
139.82049635974982

Silhouette:
0.45994823920518635

Cluster sizes:
0 → 53
1 → 50
2 → 47

Interpretation
K = 2 produced stronger separation according to the silhouette score.
K = 3 produced three relatively balanced clusters and corresponded well with the three known Iris classes for the purpose of our experiment.
For this practical, we used:
n_clusters=3


to investigate whether K-Means could discover the three known groups without seeing the target.
31. Final K-Means Model
We trained:
kmeans = KMeans(    n_clusters=3,    init="k-means++",    n_init=10,    random_state=42)kmeans.fit(X_scaled)


Then obtained the labels:
cluster_labels = kmeans.labels_


And added them to the dataframe:
df["Cluster"] = cluster_labels


Now the dataframe contained:
sepal length
sepal width
petal length
petal width
target
Cluster

32. Important Difference: target vs Cluster
These are different.
target
↓
Original known class

Cluster
↓
Group discovered by K-Means

K-Means never saw the target during training.
33. Cluster Centroids
We checked:
kmeans.cluster_centers_


Because K-Means was trained on X_scaled, these centroid values were standardized values.
Our standardized centroids were approximately:
Cluster 0:
[-0.050220, -0.883376,  0.347738,  0.281527]

Cluster 1:
[-1.014579,  0.853263, -1.304987, -1.254893]

Cluster 2:
[ 1.135970,  0.088422,  0.996155,  1.017526]

34. Cluster Means in Original Units
We used:
df.groupby("Cluster")[X.columns].mean()


Result:
Cluster 0:
sepal length = 5.801887
sepal width  = 2.673585
petal length = 4.369811
petal width  = 1.413208

Cluster 1:
sepal length = 5.006000
sepal width  = 3.428000
petal length = 1.462000
petal width  = 0.246000

Cluster 2:
sepal length = 6.780851
sepal width  = 3.095745
petal length = 5.510638
petal width  = 1.972340

This made the clusters easier to interpret.
35. Cluster Interpretation
Cluster 1
Approximately:
Petal length = 1.46 cm
Petal width  = 0.25 cm

This represents the small-petal group.
It was highly distinct.
Cluster 0
Approximately:
Petal length = 4.37 cm
Petal width  = 1.41 cm

This represents an intermediate group.
Cluster 2
Approximately:
Petal length = 5.51 cm
Petal width  = 1.97 cm

This represents the large-petal group.
Therefore, approximately:
Cluster 1 → small petals
Cluster 0 → medium petals
Cluster 2 → large petals

The cluster numbers themselves have no inherent meaning.
36. Visualizing the Clusters
We plotted:
plt.figure(figsize=(8, 6))plt.scatter(    df["petal length (cm)"],    df["petal width (cm)"],    c=df["Cluster"],    s=50)plt.xlabel("Petal Length (cm)")plt.ylabel("Petal Width (cm)")plt.title("K-Means Clusters")plt.show()


The plot showed three visually distinct regions.
Petal length and petal width were especially useful for visualizing the clusters.
37. Plotting Centroids
The model was trained on standardized features, but the visualization used the original measurements.
Therefore, we converted the centroids back to the original scale:
centers_original = scaler.inverse_transform(    kmeans.cluster_centers_)


Then:
centers_original_df = pd.DataFrame(    centers_original,    columns=X.columns)


The original-scale centroids corresponded approximately to the cluster means.
38. Visualizing Centroids
We plotted the centroids using:
plt.scatter(    centers_original[:, 2],    centers_original[:, 3],    marker="X",    s=250,    edgecolor="black")


Here:
[:, 2]

represents:
Petal length

and:
[:, 3]

represents:
Petal width

The large X markers represented the cluster centroids.
They appeared approximately in the center of their respective groups.
39. How K-Means Assigns a New Point
Suppose a new flower has:
Petal length = 4.5 cm
Petal width  = 1.5 cm

K-Means calculates its distance to each centroid.
It assigns the observation to the cluster whose centroid is closest.
Conceptually:
New point
    ↓
Distance to Centroid 0
Distance to Centroid 1
Distance to Centroid 2
    ↓
Find minimum distance
    ↓
Assign that cluster

The actual model uses all four standardized features, not just the two features shown in our visualization.
40. Four-Dimensional Distance
Our actual K-Means model used:
1. Sepal length
2. Sepal width
3. Petal length
4. Petal width

after scaling.
Therefore, internally the model calculates distances in a four-dimensional feature space.
The 2D petal-length/petal-width plot is only a visualization.
41. Cross-Tabulation With Original Target
After training, we compared the discovered clusters with the known target labels:
pd.crosstab(    df["target"],    df["Cluster"])


We obtained:
Cluster      0   1   2

target
0            0  50   0
1           39   0  11
2           14   0  36

42. Interpretation of the Cross-Tabulation
Target 0
Target 0:
Cluster 1 → 50

All 50 observations from target 0 were assigned to Cluster 1.
This shows strong separation of that group.
Target 1
Target 1:
Cluster 0 → 39
Cluster 2 → 11

Most were assigned to Cluster 0, but 11 were assigned to Cluster 2.
Target 2
Target 2:
Cluster 0 → 14
Cluster 2 → 36

Most were assigned to Cluster 2, but 14 were assigned to Cluster 0.
This shows overlap between target 1 and target 2.
43. Why Target 1 and Target 2 Were Harder to Separate
From the pairplot, target 1 and target 2 had more overlapping feature distributions.
Therefore:
Target 0
↓
More distinct
↓
Easy for K-Means to separate

Target 1 ←→ Target 2
↓
More overlap
↓
Harder to separate

This also helps explain why the three-cluster silhouette score was lower than the two-cluster silhouette score.
44. Cluster Labels Are Arbitrary
Suppose we have:
Target 0 → Cluster 1
Target 1 → Cluster 0
Target 2 → Cluster 2

There is nothing wrong with this.
K-Means does not know that:
0 = class 0
1 = class 1
2 = class 2

The cluster IDs are arbitrary.
Another valid run could label the same groups differently:
Cluster 0 → Target 2
Cluster 1 → Target 0
Cluster 2 → Target 1

What matters is the grouping, not the numerical cluster ID.
45. K-Means vs Classification
This is a major difference.
Classification
X + y
 ↓
Model
 ↓
Predicted class

The model learns from known labels.
K-Means
X
 ↓
K-Means
 ↓
Discovered clusters

There is no target used during training.
46. Cluster Purity in Our Iris Experiment
We can use the cross-tabulation for a post-hoc comparison with the known labels.
For each cluster, we take the largest target count.
Cluster 0:
max(39, 14) = 39

Cluster 1:
max(50) = 50

Cluster 2:
max(11, 36) = 36

Total:
39 + 50 + 36 = 125

Total observations:
150

Purity:
125 / 150
= 0.8333

Approximately:
83.33%

Important:
This is not K-Means accuracy.
It is a post-hoc cluster purity calculation using labels that K-Means did not see during training.
47. Why We Should Not Call Cluster Purity "Accuracy"
Classification accuracy assumes a direct mapping between predicted classes and actual classes.
K-Means produces arbitrary cluster IDs.
For example:
Target 0 → Cluster 1
Target 1 → Cluster 0
Target 2 → Cluster 2

Therefore, directly calculating:
accuracy_score(target, cluster_labels)


would not necessarily make sense without first accounting for the arbitrary mapping.
Clustering and classification are different tasks.
48. Important K-Means Parameters
Example:
KMeans(    n_clusters=3,    init="k-means++",    n_init=10,    random_state=42)


n_clusters
Number of clusters.
n_clusters=3


means 3 clusters.
init
Controls centroid initialization.
init="k-means++"


is a commonly used initialization strategy.
n_init
Number of initialization attempts.
n_init=10


helps reduce dependence on one initialization.
random_state
Makes the result reproducible.
random_state=42


49. Advantages of K-Means
- Simple to understand
- Easy to implement
- Relatively fast
- Works well with numerical data
- Useful for segmentation
- Easy to visualize in low dimensions
- Can work well when clusters are reasonably compact and separated
50. Limitations of K-Means
1. Need to choose K
We need to decide how many clusters to create.
2. Sensitive to scaling
Because K-Means uses distance, feature scale matters.
3. Sensitive to initialization
Different starting centroids can lead to different solutions.
This is why k-means++ and n_init are useful.
4. Sensitive to outliers
An extreme observation can affect the centroid because the centroid is based on the mean.
5. Works best for certain cluster shapes
K-Means tends to work better when clusters are reasonably compact and separated.
It may struggle with:
- Highly elongated clusters
- Irregular shapes
- Complex densities
- Strongly overlapping groups
6. Primarily numerical data
K-Means relies on numerical distances, so categorical variables require appropriate encoding or a different clustering approach.
51. Common Mistakes
Mistake 1: Giving the target to K-Means
Wrong:
X = df


when df contains the target.
Better:
X = df.drop("target", axis=1)


Mistake 2: Forgetting scaling
For distance-based algorithms, unscaled features can cause some variables to dominate.
Use:
scaler = StandardScaler()X_scaled = scaler.fit_transform(X)


when appropriate.
Mistake 3: Choosing K only because the dataset description says so
For example:
"Iris has 3 species, therefore K=3."

That isn't how we should approach an unsupervised problem.
Instead investigate:
- Elbow
- Silhouette
- Visualization
- Cluster structure
- Domain knowledge
Mistake 4: Choosing the lowest inertia
Inertia generally decreases as K increases.
Therefore, the lowest inertia isn't automatically the best K.
Mistake 5: Assuming cluster numbers have meaning
Cluster 0
Cluster 1
Cluster 2

are arbitrary identifiers.
They don't inherently correspond to:
Class 0
Class 1
Class 2

Mistake 6: Confusing clustering with classification
K-Means:
Unsupervised

Classification:
Supervised

They solve different problems.
52. Important Python Variable Mistake We Encountered
We originally wrote:
labels = model.fit_predict(X_scaled)


but later used:
silhouette_score(X_scaled, label)


and:
pd.Series(label)


The problem was:
labels

and:
label

are different Python variables.
Because the notebook still had an older label variable from a previous calculation, it produced misleading results using old labels.
Correct:
labels = model.fit_predict(X_scaled)silhouette_score(    X_scaled,    labels)pd.Series(labels)


This is an important Jupyter/Python debugging lesson:
Variables remain in memory between notebook cells.

Always make sure you're using the variable you actually created.
53. Complete K-Means Code — Iris
import pandas as pdimport matplotlib.pyplot as pltfrom sklearn.preprocessing import StandardScalerfrom sklearn.cluster import KMeansfrom sklearn.metrics import silhouette_score# -----------------------------# 1. Separate features# -----------------------------X = df.drop("target", axis=1)# -----------------------------# 2. Scale features# -----------------------------scaler = StandardScaler()X_scaled = scaler.fit_transform(X)# -----------------------------# 3. Elbow Method# -----------------------------inertia = []for k in range(1, 11):    kmeans = KMeans(        n_clusters=k,        init="k-means++",        n_init=10,


54. K-Means Cheat Sheet
K-Means
↓
Unsupervised clustering algorithm

Input
↓
Numerical features

Target
↓
Not used during training

Main idea
↓
Assign points to nearest centroid

Centroid
↓
Mean position of cluster points

Distance
↓
Usually Euclidean distance

Scaling
↓
Important because K-Means is distance-based

K
↓
Number of clusters

Elbow Method
↓
Uses inertia

Inertia
↓
Sum of squared distances from points
to their assigned centroids

Silhouette Score
↓
Measures cluster cohesion and separation

k-means++
↓
Better centroid initialization

n_init
↓
Multiple initialization attempts

random_state
↓
Reproducibility

Cluster labels
↓
Arbitrary IDs

Main limitations
↓
Need to choose K
↓
Sensitive to scaling
↓
Sensitive to initialization
↓
Sensitive to outliers
↓
Can struggle with irregular/overlapping clusters

55. Final Mental Model
The simplest way to remember K-Means:
Choose K
   ↓
Create K centroids
   ↓
Measure distances
   ↓
Assign each point
to nearest centroid
   ↓
Calculate mean of
each cluster
   ↓
Move centroids
   ↓
Repeat
   ↓
Final clusters

And the complete practical reasoning:
EDA
 ↓
Separate target
 ↓
Scale features
 ↓
Try different K
 ↓
Elbow + Silhouette
 ↓
Choose/justify K
 ↓
Train K-Means
 ↓
Get cluster labels
 ↓
Analyze cluster sizes
 ↓
Analyze centroids
 ↓
Visualize
 ↓
Interpret clusters
 ↓
If labels are available,
compare them AFTER training

56. Key Concepts to Remember
1. K-Means is unsupervised.
2. K means number of clusters.
3. Centroid = mean position of a cluster.
4. K-Means assigns points to the nearest centroid.
5. Euclidean distance is commonly used.
6. Scaling is important because K-Means is distance-based.
7. Inertia measures within-cluster squared distances.
8. Elbow Method helps identify a reasonable K.
9. Silhouette measures cluster cohesion and separation.
10. Cluster numbers are arbitrary.
11. Do not use the target during K-Means training.
12. K-Means can struggle with overlapping or irregularly shaped clusters.
13. k-means++ improves centroid initialization.
14. n_init helps reduce dependence on one initialization.
15. Always interpret clusters using their feature characteristics, not just their cluster IDs.
57. K-Means Practical — What We Have Completed
For the Iris dataset, we completed:
✓ Loaded dataset
✓ Checked shape
✓ Checked data types
✓ Checked missing values
✓ Examined descriptive statistics
✓ Separated features and target
✓ Checked feature shape
✓ Visualized the data
✓ Applied StandardScaler
✓ Calculated inertia
✓ Used Elbow Method
✓ Calculated Silhouette Scores
✓ Compared K = 2 and K = 3
✓ Trained K-Means
✓ Generated cluster labels
✓ Checked cluster sizes
✓ Examined standardized centroids
✓ Converted centroids back to original scale
✓ Calculated cluster feature means
✓ Visualized clusters
✓ Visualized centroids
✓ Compared clusters with original targets
✓ Understood cluster overlap
✓ Understood arbitrary cluster labels
✓ Understood cluster purity
✓ Reviewed K-Means parameters
✓ Reviewed limitations
✓ Reviewed common mistakes

58. What Comes Next
The next clustering algorithm in our learning path is:
Hierarchical Clustering
We will start it from the beginning rather than jumping directly into code.
Learning flow:
Hierarchical Clustering
        ↓
What is hierarchical clustering?
        ↓
Agglomerative vs Divisive
        ↓
Distance between observations
        ↓
Linkage
        ↓
Single linkage
        ↓
Complete linkage
        ↓
Average linkage
        ↓
Ward linkage
        ↓
Dendrogram
        ↓
How to read a dendrogram
        ↓
Choosing number of clusters
        ↓
AgglomerativeClustering
        ↓
Apply it to Iris
        ↓
Visualize clusters
        ↓
Compare with K-Means
        ↓
Practice questions

The key difference we will focus on is:
K-Means
→ Starts with K
→ Creates centroids
→ Iteratively assigns points

Hierarchical Clustering
→ Builds a hierarchy of observations/clusters
→ Uses distances and linkage
→ Produces a dendrogram
→ We can decide where to cut the hierarchy

This will be our next topic.