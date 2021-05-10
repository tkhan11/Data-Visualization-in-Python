import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#np.random.seed(0)

# Creating random data
rd = pd.DataFrame(np.random.randn(100, 10))


# Calculating all the desired values
df = pd.DataFrame({'mean': rd.mean(),
                   '25th%': rd.quantile(0.25),
                   '50th%': rd.quantile(0.5),
                   '75th%': rd.quantile(0.75)})
# And plot it
df.plot()
plt.title('Quantile plot')
plt.xlabel('column number')
plt.ylabel('column values')
plt.show()
