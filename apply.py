import pandas as pd
import numpy as np
df = pd.DataFrame([
    [301,"Cep",1300,2,"Ankara"],
    [302,"Masaüstü",3560,1,"İstanbul"],
    [305,"Dizüstü",5530,3,"Adana"],
    [307,"Fritöz",175,1,"İzmir"]
],columns=["Ozdeslik","Ad","Eder","Nicelik","Il"])



df["Tutar"] = df["Eder"]*df["Nicelik"]

exchange = 18.5
def my_function(value):
    return value/exchange

df["Tutar"] = df["Tutar"].apply(my_function)
df["Dolar"] = df["Tutar"].apply(my_function)



df["Vergili"] = df["Tutar"].apply(lambda value:value *1.06)


result = df[["Tutar","Vergili","Dolar"]].apply(np.cumsum)
# result = df

print(result)