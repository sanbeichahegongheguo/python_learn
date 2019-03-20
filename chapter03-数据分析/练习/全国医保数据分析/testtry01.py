import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 20, 20)
y1 = np.random.randint(50, 100, 20)
y2 = np.random.randint(50, 100, 20)
y3 = np.random.randint(50, 100, 20)

# 堆积柱状图
plt.barh(x, y1, color='r', label='语文')
plt.barh(x, y2, left=y1, color='g', label='数学')
plt.barh(x, y3, left=y1+y2, color='c', label='英语')

# 显示范围
plt.ylim(-2, 22)
plt.xlim(0, 300)

# 添加图例
plt.legend(loc='lower right')

plt.show()