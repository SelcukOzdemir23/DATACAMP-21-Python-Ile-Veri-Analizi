import pandas as pd
left = pd.DataFrame([
    [301,2,"Ankara"],
    [303,1,"Istanbul"],
    [304,3,"Adana"],
    [305,1,"Izmir"]
],columns=["Ozdeslik","Nicelik","Il"])

right = pd.DataFrame([
    [301,"Cep Telefonu",1300.0],
    [302,"Masaustu Bilgisayar",3560.0],
    [305,"Dizustu Bilgisayar",5530.0],
    [307,"Fritoz",175.0]
],columns=["Ozdeslik","Ad","Eder"])

result = pd.merge(left,right,on="Ozdeslik").fillna(0)
result = pd.merge(left,right,on="Ozdeslik",how="left")
#Soldaki değerler gelecek sağdakiler özellik olarak eklenecek
print(left)
print(right)
print(result)