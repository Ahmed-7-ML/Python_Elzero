import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Simulate throwing a fair six-sided die 1 million times
sample_size = 10**3
die_throws = np.random.randint(1, 7, size=sample_size)

# Plot the distribution
plt.hist(die_throws, bins=np.arange(0.5, 7.5, 1),align='mid', edgecolor='black')
plt.title('Distribution of Die Throws')
plt.xlabel('Die Face')
plt.ylabel('Frequency')
plt.xticks(range(1, 7))
plt.show()
