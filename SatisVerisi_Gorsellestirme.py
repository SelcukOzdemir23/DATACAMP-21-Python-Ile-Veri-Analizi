import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("data.csv")
df = df[0:100]
result = df
result = df.shape
result = df.isnull().sum()
result = df.columns

x = range(0,100)

y = df["Unit price"]

plt.figure(figsize=(15,8))
plt.bar(x,y,color="red",width=0.5)
plt.xticks(np.arange(0,100))
plt.xlabel("Günler")
plt.ylabel("Fiyatlar")
plt.title("Günlük Değişen Birim Fiyat")
plt.show()
print(result)