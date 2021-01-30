import pyqtgraph as pg
import serial
import time
'''
上下位USB通信格式：元组
'''        
def ser_plot():
    start = time.time()
    global last_data
    data = ser.readline()
    data = data.decode("utf-8")
    data = str(data)[1:-3] # 将无关字符去除 “\n” 和 b'' 去除
    try:
        data = eval(data) # 转化回元组形式
    except SyntaxError:
        data = last_data
    print(data)
    encoder = data[0]
    encoder_list.append(encoder[1])
    plot1.setData(encoder_list, pen='g')
    accel = data[1]
    accel_list.append(accel[2])
    plot2.setData(accel_list, pen='r')
    last_data = data
    end = time.time()
    print("cost:", end-start)

if __name__ == '__main__':
    encoder_list = []
    accel_list = []
    last_data = 0

    # serial初始化
    ser = serial.Serial('COM9', 9600)
    if (ser.isOpen()):
        print("open success")
    else:
        print("open failed")

    # pyqtgragh初始化
    # 创建窗口
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph USB下位机串口波形显示工具')
    win.resize(800, 500)  # 小窗口大小
    # 创建图表
    historyLength = 100  # 横坐标长度
    p1 = win.addPlot()  # 把图p加入到窗口中
    p1.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p1.setRange(xRange=[0, historyLength], yRange=[0, 100], padding=0) # x轴和y轴的范围
    p1.setLabel(axis='left', text='编码器值')  # 靠左
    p1.setLabel(axis='bottom', text='时间')
    p1.setTitle('编码器实时数据')  # 表格的名字
    plot1 = p1.plot()
    
    p2 = win.addPlot()  # 把图p加入到窗口中
    p2.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p2.setRange(xRange=[0, historyLength], yRange=[0, 100], padding=0)
    p2.setLabel(axis='left', text='z')  # 靠左
    p2.setLabel(axis='bottom', text='时间')
    p2.setTitle('加速度计实时数据')  # 表格的名字
    plot2 = p2.plot()
    # 设置定时器
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(ser_plot) # 定时刷新数据显示
    timer.start(40) # 多少ms调用一次

    app.exec_()