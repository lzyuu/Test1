# my serial

import sys
import os
import serial
import serial.tools.list_ports

port_list = 0
port_list = serial.tools.list_ports.comports()


import logging
import time


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
info_file_name = 'info-' + time.strftime(
    '%Y-%m-%d,%H-%M-%S', time.localtime(time.time())) + '.log'
handler = logging.FileHandler(info_file_name,encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
 
console = logging.StreamHandler()
console.setLevel(logging.INFO)
 
logger.addHandler(handler)
logger.addHandler(console)




def serial_open(port_name,bps = 9600):
    main_engine = serial.Serial(port_name,bps,timeout = 0.5)
    if (False  == main_engine.is_open):
        main_engine.open()
    logger.info('serial_open')
    

def serial_send(port_name,data):
    logger.info('serial_trans')
    main_engine = serial.Serial(port_name)
    main_engine.write(data.encode("utf8"))

def serial_close(port_name):
    logger.info('serial_close')
    main_engine = serial.Serial(port_name)
    main_engine.close()

# 打印设备基本信息
def Print_Name(port_name):
    logger.info('Print_Name')
    main_engine = serial.Serial(port_name)

    print(main_engine.name) #设备名字
    print(main_engine.port)#读或者写端口
    print(main_engine.baudrate)#波特率
    print(main_engine.bytesize)#字节大小
    print(main_engine.parity)#校验位
    print(main_engine.stopbits)#停止位
    print(main_engine.timeout)#读超时设置
    print(main_engine.writeTimeout)#写超时
    print(main_engine.xonxoff)#软件流控
    print(main_engine.rtscts)#软件流控
    print(main_engine.dsrdtr)#硬件流控
    print(main_engine.interCharTimeout)#字符间隔超时


def serial_search():
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

 


# 


if __name__ == "__main__":
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

    serial_search()

    chr = input(r"我觉得你得输入点啥")

    logger.info(u"print(int(chr)) 打印输入内容整型 ")
    logger.info(port_list)
    logger.info(list(port_list[0]))
    logger.info(int(chr))
    Choosen = list(port_list[int(chr)])

    logger.info(Choosen)

    serial_close(Choosen[0])

    logger.info("Print_Name()\r\n" )
    Print_Name(Choosen[0])

    serial_open(Choosen[0])

    serial_send(Choosen[0],"data")

