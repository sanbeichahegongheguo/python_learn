import re
import jieba
import wordcloud
import collections
import matplotlib.pyplot as plt

data_txt = open(r"./lesson01.txt", encoding="utf-8").read()
pattern = re.compile(u'\t|\n')
data_txt = re.sub(pattern, '', data_txt)

cut_txt = jieba.cut(data_txt)
object_list = []

for word in cut_txt:
    object_list.append(word)

word_counts = collections.Counter(object_list)

wd = wordcloud.WordCloud(font_path="simkai.ttf",background_color="white",width=800, height=660
    ).generate(cut_txt)

plt.imshow(wd)
plt.axis("off")
plt.show()




