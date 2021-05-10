import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv("./winequality-white.csv")


alcohol = dataset['alcohol']
pH = dataset['pH']

"""
# plot 1
xpoints = np.array([2,4,6,8,10])
ypoints = np.array([21,44,67,89,100])

plt.subplot(1,2,1)
plt.plot(xpoints, ypoints)

# Plot 2
xpoints = np.array([2,4,6,8,10])
ypoints = np.array([7,34,89,54,82])

plt.subplot(1,2,1)
plt.plot(xpoints, ypoints)
plt.show()

"""


# plot 1
plt.subplot(1,2,1)
plt.plot(alcohol)

# plot 2
plt.subplot(1,2,2)
plt.plot(pH)
plt.savefig('plot')
plt.show()

