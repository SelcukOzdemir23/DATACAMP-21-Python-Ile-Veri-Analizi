import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib
import random

result = oku = open("istiklal.txt",encoding="UTF-8").read()


wordcloud = WordCloud(background_color="black",width=800,height=400,max_words=150).generate(oku)

plt.figure(figsize=(18,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("istiklal.png")

plt.show()