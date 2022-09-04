import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

frame = pd.DataFrame(
    np.random.uniform(low=10, high=20,size=(7,4)) # Eşit ağırlıkta rastgele değer üret. Size sutün ve satir
    ,index=range(1,8)
,columns=["Kurs","Ders","Kitap","Video"])

result = frame

# frame.plot(title="Veri Çatimi",legend=False)
# frame.plot(title="Veri Çatimi")
# frame.plot(title="Veri Çatimi",kind="area")
frame.plot(title="Veri Çatimi",y="Kitap",kind="pie")
plot.show()
print(result)