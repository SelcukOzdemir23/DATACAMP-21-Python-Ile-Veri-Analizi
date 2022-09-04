from base64 import encode
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud

result = oku = open("istiklal.txt",encoding="UTF-8").read()
wordCloud = WordCloud(background_color="black",
                        width=1200,
                        height=1000
                        ).generate(oku)

plt.figure(figsize=(18,10))
plt.imshow(wordCloud)
plt.show()

print(result)