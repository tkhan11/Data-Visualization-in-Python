import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("./winequality-white.csv")

#2D Scatter plott 
#fig = plt.figure(figsize = (10, 9))


plt.scatter(dataset['alcohol'],dataset['pH'], color='blue')
plt.xlabel('Alcohol_value')
plt.ylabel('pH_value')
plt.title('2D scatter plot')
plt.show()

#3D Scatter plot
#fig = plt.figure(figsize = (10, 9))
                 
axes = plt.axes(projection ="3d")

# Creating color map
my_cmap = plt.get_cmap('hsv')

#axes.scatter3D(dataset['alcohol'],dataset['pH'],dataset['sulphates'],color='green')
axes.scatter3D(dataset['alcohol'],dataset['pH'],dataset['sulphates'], c = (dataset['alcohol']+dataset['pH']+dataset['sulphates']),cmap=my_cmap)

plt.title('3D scatter plot')
axes.set_xlabel('alcohol')
axes.set_ylabel('pH')
axes.set_zlabel('sulphates')
plt.show()

