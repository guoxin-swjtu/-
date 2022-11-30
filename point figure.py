import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def draw_scatter(n, s):
    path =r'D:\desktop\yhl-rg prediction\train_data_2.xlsx'
    data = pd.read_excel(path)#r转义斜杠
    # x = pd.read_excel(path, index_col='areasol')
    # y = pd.read_excel(path, index_col='bio')
    x1 = data['areasol_1']
    y1 = data['bio_1']
    x0 = data['areasol_0']
    y0 = data['bio_0']
    # print(x)
    # 创建画图窗口
    fig = plt.figure()
    # 将画图窗口分成1行1列，选择第一块区域作子图
    ax1 = fig.add_subplot(1, 1, 1)
    # 设置标题
    ax1.set_title('photo')
    # 设置横坐标名称
    ax1.set_xlabel('area')
    # 设置纵坐标名称
    ax1.set_ylabel('bio')
    # 画散点图
    ax1.scatter(x0, y0, s=s, c='r', marker='v')
    # 画直线图
    #ax1.plot(x2, y2, c='b', ls='--')
    # 调整横坐标的上下界
    # plt.xlim(xmax=5, xmin=0)
    # 显示

    plt.show()
    #
    # x = np.random.randn(N)
    # y = np.random.randn(N)
    # plt.scatter(x, y)
    # plt.show()
if __name__ == "__main__":
        # 运行
        draw_scatter(n=600, s=20)