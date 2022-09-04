import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.random.uniform(low=10, high=20,size=(7,4)) # Eşit ağırlıkta rastgele değer üret. Size sutün ve satir
    ,index=pd.date_range(start="20110101",periods=7)
,columns=list("ABCD"))

print(frame)
print(frame["A"])
print(frame[3:6])
print(frame["20110101":"20110104"])
print(frame.loc["20110101":"20110104"])
print(frame.loc["20110101",["B","D"]])
print(frame.loc["20110101":"20110104",["B","D"]])

print(frame.iloc[2:5])
print(frame.iloc[2:5,1:3])