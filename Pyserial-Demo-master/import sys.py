# my serial

import sys
import os
import serial
import serial.tools.list_ports

def print_serial_port1():
    s = serial.tools.list_ports.comports()

    print(s)

    print(len(s))
    c=s[0]
    print(0,c)
    c=s[1]
    print(1,c)
'''
如果你不想让上面这段程序运行,那么就用一个小函数把他封装起来吧
顺便记得,不能跟下面的函数重命名哟
即使是重命名了
Python也不会报错
但是他会执行
与if__name__ == "__main__":
最近的那个

嘿嘿
'''


def print_serial_port():
    port = serial.tools.list_ports.comports()  #返回可用的串口信息对象列表
    #[<serial.tools.list_ports_common.ListPortInfo object at 0x000000ACEB8A0390>, <serial.tools.list_ports_common.ListPortInfo object at 0x000000ACEB939470>]

    if len(port) <= 0:
        #len(port)  返回可用串口总数
        print("找不到可用的端口")


    else:
        print('可用串口总数：',len(port))
        prot_0 = 0
        for port_0 in range(0,len(port)):
            port_1 = list(port[port_0])  #把可用的第0个串口以字符串列表形式返回
            #['COM3', 'USB-SERIAL CH340 (COM3)', 'USB VID:PID=1A86:7523 SER=5 LOCATION=1-1']

            port_serial_0 = port_1[0]  #返回串口名称
            #COM3

            print(port_serial_0)
            print(port_1)
    # serial_port = input("请输入你想打开的串口:")
    # ser=serial.Serial("COM4",9600)
    # print(ser.port) #打印设备名
    # print(ser.name) #打印设备名称
    # #ser.open()
    # result=ser.write("1111".encode("utf-8"))

    # return serial_port

def OpenYourSerialPort():
    ser=serial.Serial(port ,9600 ,Timeout =0.5)
    print(ser.port) #打印设备名
    print(ser.name) #打印设备名称
    ser.open()
    ser.write("its open")

def OpenSerialAndSend():
    ser = serial.Serial(
    port="COM9",              # number of device, numbering starts at
    # zero. if everything fails, the user
    # can specify a device string, note
    # that this isn't portable anymore
    # if no port is specified an unconfigured
    # an closed serial port object is created
    baudrate=9600,          # baud rate
    bytesize=serial.EIGHTBITS,     # number of databits
    parity=serial.PARITY_NONE,     # enable parity checking
    stopbits=serial.STOPBITS_ONE,  # number of stopbits
    timeout=None,           # set a timeout value, None for waiting forever
    xonxoff=0,              # enable software flow control
    rtscts=0,               # enable RTS/CTS flow control
    interCharTimeout=None   # Inter-character timeout, None to disable
    )
    ser.write("hello".encode("utf8"))
    b = 0
    while 1:
        A = ser.readline()
        print(A)
        ser.write(A)
        b = b + 1
        print(b)

        #推出死循环的诀窍,就是,先按CTRL+ C 然后再用串口发数据,然后他真的会一直卡在那
        #好像是因为我发中文的原因

def pyqtgraph_example():
    import pyqtgraph as pg
    import pyqtgraph.examples
    pg.plot(data)
    # pyqtgraph.examples.run()

if __name__ == "__main__":
    pyqtgraph_example()
    exit(1)
    print_serial_port()
    OpenSerialAndSend()
    # A = print_serial_port()
    # exit(1)
    # OpenYourSerialPort(A)
