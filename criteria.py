import pandas as pd
import numpy as np

path="sales.csv"
df = pd.read_csv(path)

result = df[df["İl"]=="İzmir"]
result= df[df["İl"]=="İzmir"][["Ad","Eder","Nicelik"]]
result = df[(df["Ad"]=="Dizüstü Bilgisayar") & (df["İl"]=="İzmir")]

print(result)