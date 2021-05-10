import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

normal_distribution = np.random.normal(80,10,500)  # here our values will concentrate around 80  and standarad deviation is 10 for a total of 500 values

dataset = pd.read_csv("./winequality-white.csv")

data=[2,9,11,14,23,28,43,49,66,66,66,67,68,69,72,84,98,99,110,110,111,112,150,299,500,1000]

# normally distributed histogram

plt.hist(normal_distribution)
plt.xlabel('data values')
plt.ylabel('frequency')
plt.title('Normally distributed Histogram')
plt.show()

# pH values Histogram
plt.hist(dataset['pH'])
plt.xlabel('pH_values')
plt.ylabel('frequency')
plt.title('Histogram for pH values')
plt.show()

plt.hist(data)
plt.xlabel(' data values')
plt.ylabel('frequency')
plt.title('Histogram for data values')
plt.show()
