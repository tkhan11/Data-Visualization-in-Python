# Importing packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# generating data
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("graph plot")
plt.show()

xpoints = np.array([1,4,6,8,10,21,33])
ypoints = np.array([2,6,4,12,34,10,13])
plt.plot(xpoints, ypoints)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("graph plot")
plt.show()

