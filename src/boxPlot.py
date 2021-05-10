import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("./winequality-white.csv")

data=[2,9,11,14,23,28,43,99,45,150,299,500,1000]

# Alcohol values has no outliers
plt.boxplot(dataset['alcohol'])
plt.ylabel('Alcohol_values')
plt.title('BoxPlot for Alcohol values')
plt.show()

# pH values has outliers
plt.boxplot(dataset['pH'])
plt.ylabel('pH_values')
plt.title('BoxPlot for pH values')
plt.show()

plt.boxplot(data)
plt.ylabel('data values')
plt.title('BoxPlot for random data values')
plt.show()
