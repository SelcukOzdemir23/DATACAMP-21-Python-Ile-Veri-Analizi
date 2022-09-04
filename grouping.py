import pandas as pd
path = "sales.csv"

df = pd.read_csv(path)
result = df.columns

#iloc ve loc arasındaki fark , i indeks oluyor

result = df.loc[:,["İl","Nicelik"]] # Ayrı bir indesleme türü loc[satır,sutün]
by_province = df[["İl","Nicelik"]].groupby("İl").sum()
# result = df.groupby("İl").min()
result = by_name= df.groupby("Ad").sum()
result = by_name_province = df.groupby(["İl","Ad"]).sum()

#map,filter,reduce



print(result)
