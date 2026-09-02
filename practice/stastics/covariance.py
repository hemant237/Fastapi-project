import numpy as np

x = [1, 2, 3, 4, 5]
y = [50, 40, 30, 20, 10]

covariance = np.cov(x, y)[0, 1]

print("Covariance:", covariance)



a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

covariance = np.cov(a, b)[0, 1]

print("Covariance:", covariance)