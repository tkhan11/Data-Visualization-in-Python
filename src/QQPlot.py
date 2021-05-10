import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('./winequality-white.csv')

test = np.random.normal(0,1,100)

sm.qqplot(test, line='45')      # Normally distributed
sm.qqplot(dataset['pH'], line='45')
plt.title("Q-Q Plot")
plt.show()
