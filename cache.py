import pandas as pd
import os.path

path = "sales.csv"
if os.path.exists(path):
    df = pd.read_csv(path)
else:
    url = "http://www.godoro.com/front-end/sales.csv"
    df = pd.read_csv(url)
    df.to_csv("sales.csv")
    

df.drop(columns=["Unnamed: 0.1","Unnamed: 0"],inplace=True)
result = df
print(result)