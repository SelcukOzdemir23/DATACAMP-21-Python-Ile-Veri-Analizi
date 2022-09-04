from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

result = df = pd.read_csv("netflix_titles.csv")

result = df.shape # Kaç satır kaç kolon
result = df.info() # NAN'lara bakıyoruz
result = df.isnull().sum() #NAN sayısına bakıyoruz
ülkeler =df["country"].value_counts() #Hangi ülkeden ne kadar değer var
result = ülkeler = pd.DataFrame({"Yapim Sayisi":df["country"].value_counts()})
result = x = ülkeler.head(13).index

result = y = ülkeler["Yapim Sayisi"].head(13)

# figure1 = plt.figure(figsize=(15,8))
# plt.bar(x,y,color="green")
# plt.title("En çok Netflix yapımına sahip 12 ülke")
# plt.xlabel("Ülkeler")
# plt.ylabel("Yapım Sayisi")
# plt.show()


#YERLİ YAPIMLARIN DETAYLARI:

result = turk_yapimlari=df[df["country"]=="Turkey"]
result = turk_yapimlari.sort_values(by="release_year").head()

result = yonetmen = pd.DataFrame({"Yapım Sayisi":turk_yapimlari["director"]}).value_counts()

#Yönetmenler hangi filmler çekti?

result = turk_yapimlari[turk_yapimlari["director"]=="Burak Aksak"]
print(result["title"])