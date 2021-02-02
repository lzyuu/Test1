# my serial

import sys
import os
import serial
import serial.tools.list_ports

class COM:
    port_list = 0
    port_list = serial.tools.list_ports.comports()

    def __init__(self):
        print(u'到底有没有自动运行__init__啦')
        self.serial_search()


    def serial_open(self,port_name,bps = 9600):
        self.main_engine = serial.Serial(port_list[port_name],bps,timeout = 0.5)
        self.main_engine.open()

    def serial_close(self):
        self.main_engine.close()

    def serial_send(self):
        self.main_engine.write(data)

    def serial_search(self):
        if len(port_list) <= 0:
            print(u"不能找到串口呀")

        else:
            print(u"找到可用串口: ",len(port_list))
            port_num = 0
            for port_num in range(0,len(port_list)):
                port_frist = list(port_list[port_num])
                port_firts_name = port_frist[0]

                print(port_firts_name)
                print(port_frist)
    
    # 打印设备基本信息
    def Print_Name(self):
        print(self.main_engine.name) #设备名字
        print(self.main_engine.port)#读或者写端口
        print(self.main_engine.baudrate)#波特率
        print(self.main_engine.bytesize)#字节大小
        print(self.main_engine.parity)#校验位
        print(self.main_engine.stopbits)#停止位
        print(self.main_engine.timeout)#读超时设置
        print(self.main_engine.writeTimeout)#写超时
        print(self.main_engine.xonxoff)#软件流控
        print(self.main_engine.rtscts)#软件流控
        print(self.main_engine.dsrdtr)#硬件流控
        print(self.main_engine.interCharTimeout)#字符间隔超时

# 
import logging
import time


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
info_file_name = 'info-' + time.strftime(
    '%Y-%m-%d,%H-%M-%S', time.localtime(time.time())) + '.log'
handler = logging.FileHandler(info_file_name)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
 
console = logging.StreamHandler()
console.setLevel(logging.INFO)
 
logger.addHandler(handler)
logger.addHandler(console)
 


# 


if __name__ == "__main__":
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

    x = COM()
    chr = input(r"我觉得你得输入点啥")
    print(int(chr))
    x.serial_open(int(chr))
    # x.serial_open()
    x.Print_Name()
    # x.serial_search()
    # x.serial_open(input("你要打开几号呀"))
    
