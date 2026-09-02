# Variance measures how spread out values are from the mean.
# Steps:
# 1. Calculate mean
# 2. Calculate difference from mean
# 3. Square the differences
# 4. Calculate their average

data = [2, 4, 6]

mean = sum(data) / len(data)

squared_differences = []

for value in data:
    difference = value - mean
    squared_difference = difference ** 2
    squared_differences.append(squared_difference)

variance = sum(squared_differences) / len(data)

print("Mean:", mean)
print("Squared differences:", squared_differences)
print("Variance:", variance)

import math

# Standard deviation = square root of variance

standard_deviation = math.sqrt(variance)

print("Variance:", variance)
print("Standard deviation:", standard_deviation)

import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("25th percentile:", np.percentile(data, 25))
print("50th percentile:", np.percentile(data, 50))
print("75th percentile:", np.percentile(data, 75))

# Percentile tells us the value below which a given
# percentage of observations fall.
# 50th percentile = median
# 25th percentile = Q1
# 75th percentile = Q3


hours = [1, 2, 3, 4, 5]
scores = [40, 50, 60, 70, 80]

correlation = np.corrcoef(hours, scores)[0, 1]

print("Correlation:", correlation)


x = [1, 2, 3, 4, 5]
y = [50, 40, 30, 20, 10]

correlation = np.corrcoef(x, y)[0, 1]

print("Correlation:", correlation)