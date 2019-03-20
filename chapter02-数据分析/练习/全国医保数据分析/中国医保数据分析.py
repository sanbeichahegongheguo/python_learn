import xlrd
import pprint
from matplotlib import pyplot as plt


def read_revenue(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]

    years = table.col_values(0, start_rowx=11, end_rowx=39)
    total = table.col_values(1, start_rowx=11, end_rowx=39)
    basic_pension_insurance = table.col_values(2, 11, 39)
    unemployment_insurance = table.col_values(3, 11, 39)
    urban_basic_medical_insurance = table.col_values(4, 15, 39)
    work_injury_insurance = table.col_values(5, 15, 39)
    maternity_insurance = table.col_values(6, 15, 39)

    return years, total, basic_pension_insurance,\
           unemployment_insurance, urban_basic_medical_insurance,\
           work_injury_insurance, maternity_insurance


def draw_excel(path):
    years, total, basic_pension, unemployment, urban_bsic_medical, work_injury, maternity = read_revenue(path)

    # 获取年份数据
    x1 = []
    for i in range(28):
        a = int(years[i]) - 0.2
        b = int(years[i]) + 0.2
        x1.append(a)
        x1.append(b)

    # 获取总量数值
    y1 = []
    a = len(total)
    for i in range(a):
        a = total[i]
        b = total[i]
        y1.append(a)
        y1.append(b)

    # 获取基本养老保险数值
    y2 = []
    a = len(basic_pension)
    for i in range(a):
        a = basic_pension[i]
        b = basic_pension[i]
        y2.append(a)
        y2.append(b)

    y3 = []
    a = len(unemployment)
    for i in range(a):
        a = unemployment[i]
        b = unemployment[i]
        y3.append(a)
        y3.append(b)

    fig = plt.figure(figsize=[10, 7.5], facecolor=(239 / 255, 248 / 255, 253 / 255))
    ax1 = fig.add_subplot(1, 1, 1, facecolor=(239 / 255, 248 / 255, 253 / 255))

    ax1.spines['top'].set_visible(False)  # 去掉左边边框
    ax1.spines['bottom'].set_visible(False)  # 去掉下方边边框
    ax1.spines['right'].set_visible(False)  # 去掉右边边框
    ax1.spines['left'].set_visible(False)  # 去掉左边边框

    ax1.grid(True, 'major', 'y', c='black', ls='--', lw=.5, alpha=.3)  # 绘制网格图
    """
    # matplotlin.pyplot.grid(b, which, axis, color, linestyle, linewidth， **kwargs)
    # 第一个参数是是否绘制网格图。
    # 第二个参数，major是主坐标，minor是副坐标，both是都画。
    # 第三个参数，输入'x'是画竖线，输入'y'是画横线, both是都画。
    # 第四个参数，设置网格线的颜色，也可以用c来代替color。
    # 第五个参数，设置网格线的风格，也可以用ls来代替linestyle，有连续实线，虚线或者其它不同的线条，可选的有： | '-' | '--' | '-.' | ':' | 'None' | ' ' | '']
    # 第六个参数，设置网格线的宽度。
    # 再往后的参数，如alpha，设置透明度。
    """
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(''.format))  # X轴不显示刻度
    ax1.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))  # Y轴显示为原有数字加%

    # plt.xticks(range(0, 30, 2), fontsize=14)  # 设置X轴的的刻度
    # plt.yticks(range(0, 90, 10), fontsize=14)  # 设置Y轴的刻度



    # ax1.plot(years, total, color=(253 / 255, 222 / 255, 194 / 255), alpha=1)
    # ax1.stackplot(x1, y2, y3, alpha=1)
    # ax1.stackplot(years, y3, color=(239 / 255, 194 / 255, 188 / 255), alpha=1)
    # ax1.stackplot(x1, y3, color=(237 / 255, 231 / 255, 195 / 255), alpha=1)
    # ax1.stackplot(x1, y1, color=(215 / 255, 215 / 255, 215 / 255), alpha=1)

    # ax1.plot([1988, 2016], [0, 0], color='black', linewidth=5)  # 人工做一个坐标轴
    # ax1.set(xlim=(1988, 2016), xlabel="Year", ylabel="Revenue")
    ax1.bar(years, basic_pension, width=2, color=(243 / 255, 133 / 255, 36 / 255))
    ax1.text(100, 120, 'Eurapo Central', ha='left', va='center', fontsize=44.5, color=(195/255, 169/255, 48/255))
    plt.xticks(range(28), years, fontsize=7.5)
    # for a, b in zip(x1, years):
    #     ax1.text(a, 1, b, ha='center', va='bottom', fontsize=4.5)  # 在底部的坐标轴上写上年份

    plt.show()


if __name__ == "__main__":
    path = "./datas/人社部/09-01.xls"
    draw_excel(path)
