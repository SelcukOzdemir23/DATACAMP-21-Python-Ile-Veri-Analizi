from turtle import color
from unittest import result
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#1.Bölüm
liste1 = np.arange(10,50,5)
liste2 = [300,200,150,500,600,500,150,200]
# plt.plot(liste1,liste2,color="r")
# plt.xlabel("X")
# plt.title("Baslik")
# plt.ylabel("Y")




dizi1 = np.linspace(0,100,10)
dizi2 = dizi1**2
# plt.plot(dizi1,dizi2,"g--")


#2.Bölüm
dizi1 = np.linspace(1,10,10)
dizi2 = dizi1 **2

# figure1 = plt.figure()
# figure2 = figure1.add_axes([0.2,0.2,1,1])

figure1 = plt.figure(dpi=100)
ax1 = figure1.add_axes([0.1,0.1,0.8,0.8])
ax2 = figure1.add_axes([0.3,0.3,0.4,0.4])
ax1.plot(dizi1,dizi2,color="red",label="Kare")




plt.show()
print(result)


