n, p = [int(x) for x in input().split()]
import numpy as np
data = []
for i in range(n):
    list = [float(x) for x in input().split()]
    data.append(list)
X = np.array(data)
means = X.mean(axis=1).round(2)
print(means)