from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = open('github.txt', 'r').read()

wc = WordCloud(stopwords=STOPWORDS).generate(text)
plt.imshow(wc)
plt.axis("off")
plt.show()

