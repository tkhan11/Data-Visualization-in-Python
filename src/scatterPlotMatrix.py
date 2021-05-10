import plotly.express as px
import pandas as pd

dataset = pd.read_csv("./winequality-white.csv")
reduced_data = dataset[['alcohol','pH', 'sulphates','chlorides','density']]
#fig = px.scatter_matrix(dataset,dimensions = ['alcohol','pH', 'sulphates','chlorides','density'], color= 'quality')
fig = px.scatter_matrix(reduced_data)
fig.show()

