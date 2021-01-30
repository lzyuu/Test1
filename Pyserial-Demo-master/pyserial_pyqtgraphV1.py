import array
import serial
import threading
import pyqtgraph as pg
import numpy as np
import time


i = 0
def Serial():
    while(True):
        n = mSerial.inWaiting()
        if(n):
            dattt = mSerial.readline()
            print(dattt)
            dattt = int(dattt)
            print(dattt)

            dat =  dattt # 格式转换
            data.append(dat)


            print(dat)


def plotData():
    curve.setData(data)
    print(data)


if __name__ == "__main__":
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph逐点画波形图')
    win.resize(800, 500)  # 小窗口大小
    data = list(0)
    historyLength = 60000  # 横坐标长度
    a = 0

    p = win.addPlot()  # 把图p加入到窗口中
    p.showGrid(x=True, y=True)  # 把X和Y的表格打开
    #p.setRange(xRange=[0, historyLength], yRange=[0, 256*100], padding=0)
    p.setLabel(axis='left', text='y / V')  # 靠左
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('semg')  # 表格的名字
    curve = p.plot()  # 绘制一个图形
    curve.setData(data)
    portx = 'COM9'
    bps = 9600
    # 串口执行到这已经打开 再用open命令会报错
    mSerial = serial.Serial(portx, int(bps))
    if (mSerial.isOpen()):
        print("open success")
        mSerial.write("hello".encode()) # 向端口些数据 字符串必须译码
        mSerial.flushInput()  # 清空缓冲区
    else:
        print("open failed")
        serial.close()  # 关闭端口
    th1 = threading.Thread(target=Serial)#目标函数一定不能带（）被这个BUG搞了好久
    th1.start()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)  # 定时刷新数据显示
    timer.start(1000)  # 多少ms调用一次
    app.exec_()