from matplotlib import pyplot as plt
import random

random.seed(33)
y1=[random.randint(40,50) for i in range(5)]
y2=[random.randint(30,40) for i in range(5)]
y3=[random.randint(20,30) for i in range(5)]
y4=[random.randint(10,20) for i in range(5)]
y5=[random.randint(0,10) for i in range(5)]
y6=[i for i in range(2011,2016)]


x=[i*2-1 for i in range(1, 6)]

x2=[]
for i in range(len(x)):
    a=x[i]-0.5
    b=x[i]+0.5
    x2.append(a)
    x2.append(b)
y11=[]
for i in range(len(y1)):
    a=y1[i]
    b=y1[i]
    y11.append(a)
    y11.append(b)

y12=[]
for i in range(len(y1)):
    a=y2[i]
    b=y2[i]
    y12.append(a)
    y12.append(b)
y13=[]
for i in range(len(y1)):
    a=y3[i]
    b=y3[i]
    y13.append(a)
    y13.append(b)
y14=[]
for i in range(len(y1)):
    a=y4[i]
    b=y4[i]
    y14.append(a)
    y14.append(b)
y15=[]
for i in range(len(y1)):
    a=y5[i]
    b=y5[i]
    y15.append(a)
    y15.append(b)


fig = plt.figure(figsize=[10,7.5],facecolor=(239/255,248/255,253/255))
ax1=fig.add_subplot(1,1,1,facecolor=(239/255,248/255,253/255))

ax1.spines['top'].set_visible(False)#去掉左边边框
ax1.spines['bottom'].set_visible(False)#去掉下方边边框
ax1.spines['right'].set_visible(False)#去掉右边边框
ax1.spines['left'].set_visible(False)#去掉左边边框

ax1.grid(True, 'major', 'y', ls='--', lw=.5, c='black', alpha=.3)
#'x'是竖着的，y是横着的,both是都画，major是主坐标，minor是附坐标，linstyle，color，alpha
ax1.xaxis.set_major_formatter(plt.FuncFormatter(''.format)) #X轴不显示刻度
ax1.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))#Y轴显示为原有数字加%

plt.xticks(range(0, 11, 2), fontsize=14)#设置X轴的的刻度
plt.yticks(range(0, 90, 10), fontsize=14)#设置Y轴的刻度

ax1.stackplot(x2,y11,color=(253/255,222/255,194/255),alpha=1)
ax1.stackplot(x2,y12,color=(188/255,205/255,225/255),alpha=1)
ax1.stackplot(x2,y13,color=(239/255,194/255,188/255),alpha=1)
ax1.stackplot(x2,y14,color=(237/255,231/255,195/255),alpha=1)
ax1.stackplot(x2,y15,color=(215/255,215/255,215/255),alpha=1)

ax1.bar(x,y1,width=1,color=(243/255,133/255,36/255))
ax1.bar(x,y2,width=1,color=(65/255,113/255,156/255))
ax1.bar(x,y3,width=1,color=(200/255,35/255,52/255))
ax1.bar(x,y4,width=1,color=(195/255,169/255,48/255))
ax1.bar(x,y5,width=1,color=(100/255,100/255,100/255))

ax1.plot([0.5,9.5],[0,0],color='black',linewidth=5) # 人工做一个坐标轴

ax1.text(4,55,'Eurapo Central',ha='left',va='center',fontsize=14.5,color=(195/255,169/255,48/255))# 计算好文字的位置，ha表示文字左右对齐，left就是表示文字左边的位置和x值重合，center就是文字中间的位置


for a,b in zip(x,y6):
    ax1.text(a,-2,b,ha='center',va='bottom',fontsize=14.5)#在底部的坐标轴上写上年份


plt.show()
