from turtle import color
import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

#Correlation  = ilinti
data = np.array([[12,14,11,26,30,23,41,56,72,46],[12,14,11,26,30,23,41,56,72,46]])

plt.scatter(data[0],data[1],color="green")
plt.show()
result = np.corrcoef(data)
result = data.T
 
print(result)
