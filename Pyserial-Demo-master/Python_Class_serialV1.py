# my serial
import logging2

import sys
import os
import serial
import serial.tools.list_ports


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
 
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

# 


class COM:
    def __init__(self):
        print(u'到底有没有自动运行__init__啦')
        self.serial_search()

    def serial_open(self,port_name,bps):
        self.Main_engine = serial.serial(port_name,9600,timeout = 0.5)
        self.Main_engine.open()

    def serial_open(self):
        self.Main_engine.close()

    def serial_send(self):
        self.Main_engine.write(data)

    def serial_search(self):
        port =  serial.tools.list_ports.comports()
        if len(port) <= 0:
            print(u"不能找到串口呀")

        else:
            print(u"找到可用串口: ",len(port))
            port_num = 0
            for port_num in range(0,len(port)):
                port_frist = list(port[port_num])
                port_firts_name = port_frist[0]

                print(port_firts_name)
                print(port_frist)
    

if __name__ == "__main__":
    x = COM()
    
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
    # x.serial_search()
    # x.serial_open(input("你要打开几号呀"))
    
