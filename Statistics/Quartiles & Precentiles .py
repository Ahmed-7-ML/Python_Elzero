import numpy as np

values = [13, 21, 21, 40, 42, 48, 55, 72]

x = np.quantile(values, [0, 0.25, 0.5, 0.75, 1])
z = np.quantile(values,[0, 0.25])
a = np.quantile(values,[0, 0.25 , 0.5])
b = np.quantile(values,[0])
print(x)
print(z)
print(a)
print(b)

y = np.percentile(values, 65)

print(y)
