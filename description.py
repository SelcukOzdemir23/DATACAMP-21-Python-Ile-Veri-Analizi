import numpy as np
import pandas as pd
import scipy.stats as st
data = np.array([14.5,54.0,65.2,22.7,11.8,16.0,14.5,51.1,25.8,26.1])

result = descriptions = st.describe(data)
result = descriptions.nobs
result = descriptions.minmax
result = descriptions.mean
result = descriptions.variance
result = descriptions.skewness
result = np.sqrt(descriptions.variance)
result = descriptions.kurtosis
print(result)

