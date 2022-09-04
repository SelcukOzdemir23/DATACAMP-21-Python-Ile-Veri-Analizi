import pandas as pd

path = "sales.csv"

df = pd.read_csv(path)

df["Tutar"] = df["Nicelik"]*df["Eder"]

result = df
print(df)