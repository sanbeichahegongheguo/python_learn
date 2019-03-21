import xlrd
import pprint
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def ls(path='*'):
    import glob
    return glob.glob(path)


def fraw_peopledata(file, title):
    path = file
    data_people = xlrd.open_workbook(path)
    table = data_people.sheets()[0]
    age = table.col_values(0, start_rowx=8, end_rowx=28)
    male = table.col_values(5, 8, 28)
    female = table.col_values(6, 8, 28)
    # 男性数量朝左。
    for i in range(len(male)):
        male[i] = -male[i]
    plt.figure(figsize=(20,10))
    plt.barh(age, female, color='r', label='女性')
    plt.barh(age, male, color='b', label='男性')

    for i in range(len(female)):
        plt.text(female[i]+0.1, i-0.05, "%.2f%%" % female[i], fontdict={'size': 14, 'color':  'red'})
        plt.text(male[i]-0.45, i-0.1, "%.2f%% "% abs(male[i]), fontdict={'size': 14, 'color':  'blue'})

    # 显示范围
    plt.ylim(-2, 22)
    plt.xlim(-6, 6)

    plt.xlabel("性别（男/女）", fontsize=20)
    plt.ylabel("年龄组（岁）", fontsize=20)
    plt.title("%d年中国人口年龄性别组成" % title, fontsize=25)

    # 添加图例
    plt.legend(loc='upper right')
    plt.pause(0.3)
    plt.show()

years = range(2004, 2014)
files = ls("./datas/国家统计局/*")

import matplotlib.animation as animation
ims = []
n = len(files)
for j in range(n):
    for i in years:
        if (str(i) in files[j]):            
            fraw_peopledata(files[j], i)

            # ims.append(im)
#             print(i)
#             print(files[j])
# ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)
# ani.save("test.gif",writer='pillow')