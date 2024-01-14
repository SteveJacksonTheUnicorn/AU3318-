from config import *

if __name__ == "__main__":
    x = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200, 3600, 4000]
    y = [6393, 6418, 6712, 6702, 6752, 6677, 6821, 7159, 7568, 7577]

    f1 = np.polyfit(x, y, 4)
    p1 = np.poly1d(f1)
    print(p1)#打印出拟合函数
    yvals1 = p1(x)  #拟合y值

    plot1 = plt.plot(x, y, 's',label='original values')
    plot2 = plt.plot(x, yvals1, 'r',label='polyfit values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="best", borderaxespad = 0.)
    plt.title('polyfitting')
    plt.savefig("report images/fitting4.png")
    plt.show()