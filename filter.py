import pandas as pd
import numpy as np

#DataFrame = Tablo
#Series = Sutün
frame = pd.DataFrame(
    {
        "A":list(range(0,10)),
        "B":[10,11,12,13,14,15,16,17,18,19],
        "C":pd.Series([10,11,12,13,14,15,16,17,18,19]),
        "D":pd.date_range("20100101",periods=10),
        "E":np.random.uniform(low=30,high=40,size=(10)),
        "F":pd.Categorical(["Yesil","Gokce","Yesil","Al","Yesil","Al","Gokce","Yesil","Yesil","Al"]),
        "G":0
    }
)

result = frame[frame["C"]>15]
result = frame[frame.F.isin(["Al","Gokce","Ak"])]
print(result)