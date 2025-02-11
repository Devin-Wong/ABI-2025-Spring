import numpy as np

data = np.array([0, -3, -32, 10, 7, 9])

s = data.sum()
minimum = data.min()
maximum = data.max()
mean = data.mean()
std = data.std()


Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

print(Q1, Q2, Q3)