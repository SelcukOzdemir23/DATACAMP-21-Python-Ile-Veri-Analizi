import pandas as pd
import numpy as np

frame = pd.DataFrame(
    np.random.uniform(low=10, high=20,size=(7,4)) # Eşit ağırlıkta rastgele değer üret. Size sutün ve satir
    ,index=pd.date_range(start="20110101",periods=7)
,columns=list("ABCD"))

result = frame
result = frame.sort_index(axis=0,ascending=False)
result = frame.sort_index(axis=1,ascending=False)
result = frame.sort_values(by="C")
print(result)